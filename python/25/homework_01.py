""" 01 Деление без ошибок

Напишите функцию, которая
- выполняет деление двух чисел, введенных пользователем,
- и обрабатывает возможные ошибки.

ВАЖНО: Используйте несколько обработок различных ошибок

Пример вывода:
Введите делимое: 345
Введите делитель: 5a
Ошибка: Введено некорректное число.

"""


def safe_division(a, b):
    try:
        a = float(a)
        b = float(b)
        result = a / b
        return result
    except ValueError:
        return "Ошибка: Введено некорректное число."
    except ZeroDivisionError:
        return "Ошибка: Деление на ноль!"
    except Exception as e:
        return f"Неожиданная ошибка: {e}"


# Примеры вызова
print(safe_division(345, 5))        # 69.0
print(safe_division(345, "5a"))     # Ошибка: Введено некорректное число.
print(safe_division(345, 0))        # Ошибка: Деление на ноль!
print(safe_division(345, []))       # Неожиданная ошибка: float() argument must be a string or a real number, not 'list'

