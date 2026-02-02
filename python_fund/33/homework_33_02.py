""" 02 Среднее время выполнения с количеством вызовов

Доработайте декоратор measure_time, чтобы он
- принимал параметр repeats — количество вызовов функции.

Декоратор должен
- выполнять функцию указанное число раз
- и выводить среднее время выполнения.

Пример применения:
@measure_time(10)
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

Пример вывода:
Среднее время выполнения для 10 вызовов: 0.21 секунд
Результат: 49999995000000

"""
import time
import functools


def measure_time(repeats):

    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            total_time = 0
            last_result = None

            for _ in range(repeats):
                start_time = time.time()
                last_result = func(*args, **kwargs)
                end_time = time.time()
                total_time += (end_time - start_time)

            average_time = total_time / repeats

            print(f"Среднее время выполнения для {repeats} вызовов: {average_time:.2f} секунд")
            print(f"Результат: {last_result}")

            return last_result

        return wrapper

    return decorator


@measure_time(10)
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

compute()

# Среднее время выполнения для 10 вызовов: 0.49 секунд
# 49999995000000

############# 2

# import time
#
#
# def measure_time(repeats=5):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             count = sum_time = 0
#
#             start_time = time.time()
#
#             for _ in range(repeats):
#                 result = func(*args, **kwargs)
#                 count += 1
#
#             sum_time += time.time() - start_time
#
#             print(f"Среднее время выполнения для {count} вызовов: {(sum_time / count):.2f} секунд.")
#
#             print(f"Результат: {result}")
#
#         return wrapper
#
#     return decorator
#
# @measure_time(10)
# def compute():
#     total = 0
#     for i in range(10_000_000):
#         total += i
#     return total
#
# compute()