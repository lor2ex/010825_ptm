""" 01 Фабрика функций округления

Создайте функцию make_rounder(), которая
 - принимает количество знаков для округления
 - и возвращает другую функцию.

Полученная функция должна принимать число и возвращать его,
округлённое до указанного ранее количества знаков после запятой.

Пример вызова:
print(round2(3.14159))
print(round2(2.71828))
print(round0(9.999))

Пример вывода:
3.14
2.72
10.0
"""
from typing import Callable


def make_rounder(num_digits: int) -> Callable:
    def rounder(val: float) -> float:
        return round(val, num_digits)
    return rounder


round2 = make_rounder(2)
round0 = make_rounder(0)

print(round2(3.14159))
print(round2(2.71828))
print(round0(9.999))

# 3.14
# 2.72
# 10.0


############ 2

# from functools import partial
#
# round2 = partial(round, ndigits=2)
# round0 = partial(round, ndigits=0)
#
# print(round2(3.14159))  # 3.14
# print(round2(2.71828))  # 2.72
# print(round0(9.999))    # 10.0

############ 3

# make_rounder = lambda num_digits: lambda val: round(val, num_digits)
#
# round2 = make_rounder(2)
# round0 = make_rounder(0)
