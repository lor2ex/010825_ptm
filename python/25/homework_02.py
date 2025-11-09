""" 02 Логирование ошибок

Перенаправьте в предыдущей задаче вывод ошибок в файл errors.log
в соответствии с форматом ниже.

ВАЖНО: используйте вывод ошибок и в файл, и на экран.

Пример вывода:
2025-02-23 22:38:53,686 - ERROR - test.py - 16 - Ошибка: Введено некорректное число.

"""

import logging
import sys

# Настройка логирования
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

# Формат сообщений (добавляем - %(message)s в конце)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s')

# Обработчик для вывода в файл
file_handler = logging.FileHandler(filename='errors.log', encoding='utf-8')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

# Обработчик для вывода на экран (stderr)
stream_handler = logging.StreamHandler(sys.stderr)
stream_handler.setLevel(logging.ERROR)
stream_handler.setFormatter(formatter)

# Добавляем обработчики в логгер
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

def safe_division(a, b):
    try:
        a = float(a)
        b = float(b)
        result = a / b
        return result
    except ValueError:
        error_msg = "Ошибка: Введено некорректное число."
        logger.error(error_msg)
        return error_msg
    except ZeroDivisionError:
        error_msg = "Ошибка: Деление на ноль!"
        logger.error(error_msg)
        return error_msg
    except Exception as e:
        error_msg = f"Неожиданная ошибка: {e}"
        logger.error(error_msg)
        return error_msg


# Примеры вызова
print(safe_division(345, 5))        # 69.0
print(safe_division(345, "5a"))     # Ошибка: Введено некорректное число.
print(safe_division(345, 0))        # Ошибка: Деление на ноль!
print(safe_division(345, []))       # Неожиданная ошибка: float() argument must be a string or a real number, not 'list'
