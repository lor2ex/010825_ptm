""" 02 Генератор уникальных элементов

Создайте генератор, который
- принимает список элементов и выдаёт только уникальные значения,
сохраняя порядок их появления в исходном списке

Входные данные:
data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]

Пример вывода:
3
1
2
4
5
6
7
8

"""
from typing import Generator, Any


def generator_unique(items: list[Any]) -> Generator[Any, None, None]:
    yield from list(dict.fromkeys(items))

data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]

for x in generator_unique(data):
    print(x)


####### 2

# def generator_unique(items: list[Any]) -> Generator[Any, None, None]:
#     seen = set()
#
#     for item in items:
#         if item not in seen:
#             yield item
#             seen.add(item)
#
# data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]
#
# for x in generator_unique(data):
#     print(x)

# 3
# 1
# 2
# 4
# 5
# 6
# 7
# 8