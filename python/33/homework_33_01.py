""" 01 Среднее время выполнения

Создайте декоратор measure_time, который
- измеряет и выводит среднее время выполнения функции за 5 вызовов.

Функция может быть любой:
    например, сортировка списка, чтение из файла или расчёты.

Пример применения:
@measure_time
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

Пример вывода:
Среднее время выполнения для 5 вызовов: 0.21 секунд
Результат: 49999995000000

"""

import time
import functools


def measure_time(func):
    REPEATS = 5

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        total_time = 0
        last_result = None

        for _ in range(REPEATS):
            start_time = time.time()
            last_result = func(*args, **kwargs)
            end_time = time.time()
            total_time += (end_time - start_time)

        average_time = total_time / REPEATS

        print(f"Среднее время выполнения для {REPEATS} вызовов: {average_time:.2f} секунд")
        print(f"Результат: {last_result}")

        return last_result

    return wrapper


@measure_time
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

compute()

# Среднее время выполнения для 5 вызовов: 0.47 секунд
# 49999995000000



##############  2

# import time
#
# def measure_time(func):
#     def wrapper(*args, **kwargs):
#         count = sum_time = 0
#
#         start_time = time.time()
#
#         for _ in range(5):
#             result = func(*args, **kwargs)
#             count += 1
#
#         sum_time += time.time() - start_time
#
#         print(f"Среднее время выполнения для {count} вызовов: {(sum_time / count):.2f} секунд.")
#
#         return result
#     return wrapper