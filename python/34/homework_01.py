""" 01 Класс Rectangle

Создайте класс Rectangle, который описывает прямоугольник.
У каждого объекта должны быть два поля:
- width
- и height.
Добавьте метод get_area(), который возвращает площадь прямоугольника.
Создайте объект прямоугольника с произвольными значениями.
Выведите его площадь.
Измените ширину и высоту.
Выведите новую площадь.

Пример вывода:
Площадь: 20
Новая площадь: 35

"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

# Создаем объект прямоугольника
rect = Rectangle(4, 5)
print("Площадь:", rect.get_area())

# Изменяем ширину и высоту
rect.width = 7
rect.height = 5
print("Новая площадь:", rect.get_area())

# Площадь: 20
# Новая площадь: 35
