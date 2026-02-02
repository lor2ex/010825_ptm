""" 01 Сумма цифр числа

Напишите рекурсивную функцию, которая находит сумму всех цифр числа.

Попробуйте решить в двух вариантах: tail и non-tail.

Данные:
num = 43197
Пример вывода:
24
"""

def sum_digits_tail(n: int) -> int:
    if n == 0:
        return 0
    return n % 10 + sum_digits_tail(n // 10)


def sum_digits_non_tail(n: int, acc: int = 0) -> int:
    if n == 0:
        return acc
    return sum_digits_non_tail(n // 10, acc + n % 10)


# ##### 2
# def sum_digits_non_tail(num, accumulator=0):
#     print(num, accumulator)
#     if len(str(num)) < 2:
#         return accumulator + num
#     else:
#         return sum_digits_non_tail(int(str(num)[1:]), accumulator + int(str(num)[0]))

###### 3
# def sum_digits_iterative(n: int) -> int:
#     total = 0
#     while n > 0:
#         total += n % 10
#         n //= 10
#     return total



print(sum_digits_tail(43197))       # 24
print(sum_digits_non_tail(43197))   # 24
print(sum_digits_iterative(43197))  # 24
