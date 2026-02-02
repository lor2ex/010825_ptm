""" 01 Список всех стран

Используя базу данных world, вывести названия всех стран из таблицы country.
Каждое название должно отображаться с новой строки и иметь номер.
Пример вывода:
1. Aruba
2. Afghanistan
3. Angola
...
239. Zimbabwe

При решении задачи используйте подход Data Access Object (DAO).
"""

import mysql.connector
from local_settings import dbconfig

q_countries = "SELECT Name FROM world.country;"

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

if __name__ == "__main__":
    try:
        with WorldDB(dbconfig, autocommit=True) as db:
            countries = db.fetch_countries()
            for i, name in enumerate(countries, start=1):
                print(f"{i}. {name}")
    except DatabaseError as e:
        print(f"❌ {e}")
