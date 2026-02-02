""" 02 Сумма вложенных чисел

Напишите рекурсивную функцию, которая суммирует все числа во вложенных списках.

Попробуйте решить в двух вариантах: tail и non-tail.

Данные:
nested_numbers = [1, [2, 3], [4, [5, 6]], 7]
Пример вывода:
28
"""

def sum_digits_non_tail(lst):
    if not lst:
        return 0
    if isinstance(lst[0], list):
        return sum_digits_non_tail(lst[0]) + sum_digits_non_tail(lst[1:])
    return lst[0] + sum_digits_non_tail(lst[1:])


def sum_digits_tail(lst, acc=0):
    if not lst:
        return acc
    if isinstance(lst[0], list):
        return sum_digits_tail(lst[1:] + lst[0], acc)
    return sum_digits_tail(lst[1:], acc + lst[0])
#
#
# ##### 2
# def sum_digits_tail_2(lst):
#     if not lst:
#         return 0
#     # print(lst)
#     head, *tail = lst
#     if isinstance(head, list):
#         return sum_digits_tail_2(head) + sum_digits_tail_2(tail)
#     return head + sum_digits_tail_2(tail)
#
#
# def sum_digits_non_tail_2(lst, acc=0):
#     if not lst:
#         return acc
#     # print(acc, '\t', lst)
#     head, *tail = lst
#     if isinstance(head, list):
#         return sum_digits_non_tail_2(tail, acc + sum_digits_non_tail_2(head, acc=0))
#     else:
#         return sum_digits_non_tail_2(tail, acc + head)

##### 3
# def sum_digits_non_tail(lst) -> int:
#     return sum(element if isinstance(element, int) else sum_digits_non_tail(element)
#         for element in lst)


# def sum_digits_non_tail(lst) -> int:
#     total = 0
#     for element in lst:
#         if isinstance(element, int):  # если число
#             total += element
#         else:  # если список
#             total += sum_digits_non_tail(element)  # рекурсия!
#     return total



nested_numbers = [1, [2, 3], [4, [5, 6]], 7]

#print(sum_digits_tail(nested_numbers))       # 28
print(sum_digits_non_tail(nested_numbers))   # 28