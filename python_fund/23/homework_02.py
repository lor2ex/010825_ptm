""" 02 Сумма вложенных чисел

Напишите функцию, которая
- принимает список словарей, где каждый словарь содержит
    - имя пользователя
    - и список баллов.
- Функция должна вернуть сумму всех чисел.
- Добавьте документацию и аннотации типов для всех параметров и возвращаемого значения.

Данные:
data = [
    {"name": "Alice", "scores": [10, 20, 30]},
    {"name": "Bob", "scores": [5, 15, 25]},
    {"name": "Charlie", "scores": [7, 17, 27]}
]

Пример вывода:
Итоговый балл: 156
"""
data = [
    {"name": "Alice", "scores": [10, 20, 30]},
    {"name": "Bob", "scores": [5, 15, 25]},
    {"name": "Charlie", "scores": [7, 17, 27]}
]

def sum_nested_scores(data: list[dict[str, list[int]]]) -> int:
    """Функция принимает список словарей с именами пользователей и списками баллов,
    и возвращает сумму всех баллов.

    :param data: список словарей, где каждый словарь содержит имя пользователя и список баллов
    :return: сумма всех баллов из всех пользователей
    """
    return sum(score for user in data for score in user["scores"])

print(f"Итоговый балл: {sum_nested_scores(data)}")


####### 2
# def sum_nested_scores(data: list[dict[str, list[int]]]) -> int:
#     """Функция принимает список словарей с именами пользователей и списками баллов,
#     и возвращает сумму всех баллов.
#
#     :param data: список словарей, где каждый словарь содержит имя пользователя и список баллов
#     :return: сумма всех баллов из всех пользователей
#     """
#     total_score = 0
#     for user in data:
#         total_score += sum(user["scores"])
#     return total_score
#
# print(f"Итоговый балл: {sum_nested_scores(data)}")



##### 3
# def sum_nested_scores(data_scores: list[dict]) -> int:
#     """
#     принимает список словарей, где каждый словарь содержит
#     - имя пользователя
#     - и список баллов.
#     Функция возвращает сумму всех чисел.
#
#     :param data_scores: list(dict(name: str, scores[int]))
#     :return: int
#     """
#
#     sum_all = reduce(lambda acc, x: acc + sum(x.get('scores', [0])), data_scores, 0)
#     return sum_all
#
# print(f"Итоговый балл: {sum_nested_scores(data)}")
