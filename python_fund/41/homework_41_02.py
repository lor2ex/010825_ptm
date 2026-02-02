""" 02 Города выбранной страны

Добавьте к предыдущей программе возможность выбора страны.
Пользователь должен ввести название страны.
Далее выведите все города этой страны и их численность населения.

Пример вывода:
Введите страну: Germany
Berlin — 3386667
Hamburg — 1704735
Munich [München] — 1194560
...

"""

import mysql.connector
from local_settings import dbconfig

q_countries = "SELECT Name FROM world.country;"

q_cities = '''SELECT 
    c.Name, c.District, c.Population
FROM 
    world.city c
    JOIN 
    world.country co ON c.CountryCode = co.Code
WHERE 
    co.Name = %(country)s;
'''

class DatabaseError(Exception):
    """Общее исключение слоя доступа к данным"""
    pass


class MySQLConnection:
    """Контекстный менеджер для подключения к MySQL с поддержкой commit/rollback"""

    def __init__(self, db_config, autocommit: bool = False):
        self.dbconfig = db_config
        self.autocommit = autocommit
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = mysql.connector.connect(**self.dbconfig)
        self.connection.autocommit = self.autocommit
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            if not self.autocommit:
                if exc_type is None:
                    self.connection.commit()  # фиксируем изменения при отсутствии ошибок
                else:
                    self.connection.rollback()  # откат при ошибке
        finally:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
        return False  # не подавляем исключения


class WorldDB(MySQLConnection):
    def fetch_countries(self):
        """Получить список всех стран"""
        try:
            self.cursor.execute(q_countries)
            return [name[0] for name in self.cursor.fetchall()]
        except mysql.connector.Error as e:
            raise DatabaseError(f"Ошибка при выборке страны: {e}") from e


    def fetch_cities_by_country(self, country_name):
        """Получить все города выбранной страны с их населением"""
        try:
            params = {'country': country_name}
            cursor = self.connection.cursor(dictionary=True)

            cursor.execute(q_cities, params)
            return cursor.fetchall()

        except mysql.connector.Error as e:
            raise Exception(f"Ошибка при выборке городов: {e}")



if __name__ == "__main__":
    try:
        with WorldDB(dbconfig) as db:
            # Список всех стран
            countries = db.fetch_countries()
            print("Список стран:")
            for i, name in enumerate(countries, start=1):
                print(f"{i}. {name}")

            # Ввод страны пользователем
            country_input = input("\nВведите страну: ").strip()

            # Получаем города выбранной страны
            cities = db.fetch_cities_by_country(country_input)
            if not cities:
                print(f"Для страны '{country_input}' нет данных о городах.")
            else:
                for city in cities:
                    # Формируем строку с названием города и населением
                    city_name = city['Name']
                    district = city['District']
                    population = city['Population']
                    # Если нужно — можно добавить район/альтернативное имя
                    print(f"{city_name} — {population}")

    except DatabaseError as e:
        print(f"❌ {e}")
