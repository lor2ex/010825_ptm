""" 02 Проверка размеров фигур

Доработайте фигуры:
Добавьте проверку в инстанцирование Circle и Rectangle,
чтобы значения были строго положительными.
Если передано отрицательное или нулевое значение,
выбрасывайте пользовательское исключение InvalidSizeError.
"""


from abc import ABC, abstractmethod
import math


class InvalidSizeError(Exception):
    pass


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise InvalidSizeError("Радиус должен быть положительным числом.")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise InvalidSizeError("Ширина и высота должны быть положительными числами.")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


if __name__ == "__main__":
    try:
        c = Circle(-5)
    except InvalidSizeError as e:
        print("Ошибка:", e)

    try:
        r = Rectangle(3, 0)
    except InvalidSizeError as e:
        print("Ошибка:", e)


# Ошибка: Радиус должен быть положительным числом.
# Ошибка: Ширина и высота должны быть положительными числами.
