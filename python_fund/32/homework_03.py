""" 03. Рамка вокруг вывода

Создайте декоратор frame, который
- оборачивает результат функции рамкой из 50 символов -,
     выводя по строке до и после вызова функции.

Пример декорируемой функции:
def say_hello():
    print("Привет, игрок!")
Пример вывода:
--------------------------------------------------
Привет, игрок!
--------------------------------------------------
"""

def decorator(func):
    def wrapper():
        print(50 * '-')
        func()
        print(50 * '-')
    return wrapper


@decorator
def say_hello():
    print("Привет, игрок!")


say_hello()


############# Вариант 2: С поддержкой аргументов (более гибкий)

# def frame(func):
#     def wrapper(*args, **kwargs):
#         print(50 * '-')
#         result = func(*args, **kwargs)
#         print(50 * '-')
#         return result
#     return wrapper
#
# @frame
# def say_hello(name="игрок"):
#     print(f"Привет, {name}!")
#
# say_hello()
# say_hello("Маша")

########## Вариант 3: С type hints (питонично + читаемо)

# from typing import Callable, Any
#
# def frame(func: Callable) -> Callable:
#     def wrapper(*args: Any, **kwargs: Any) -> Any:
#         print(50 * '-')
#         result = func(*args, **kwargs)
#         print(50 * '-')
#         return result
#     return wrapper
#
# @frame
# def say_hello(name="игрок"):
#     print(f"Привет, {name}!")
#
# say_hello()
# say_hello("Маша")