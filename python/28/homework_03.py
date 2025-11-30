""" 03 Комбинации одежды

Напишите функцию, которая
- принимает списки
    - типов одежды,
    - цветов
    - и размеров,
- а затем генерирует все возможные комбинации в формате "Clothe - Color - Size".

Данные:
clothes = ["T-shirt", "Jeans", "Jacket"]
colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]

Пример вывода:
T-shirt - Red - S
T-shirt - Red - M
T-shirt - Red - L
T-shirt - Blue - S
...
Jacket - Black - L

"""

from itertools import product

clothes = ["T-shirt", "Jeans", "Jacket"]
colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]

def get_product(*args):
    for combo in product(*args):
        print(' - '.join(combo))

get_product(clothes, colors, sizes)


######## 2

# from itertools import product
#
# clothes = ["T-shirt", "Jeans", "Jacket"]
# colors = ["Red", "Blue", "Black"]
# sizes = ["S", "M", "L"]
#
# def get_product(clothes, colors, sizes):
#     for clothe, color, size in product(clothes, colors, sizes):
#         print(f'{clothe} - {color} - {size}')
#
# get_product(clothes, colors, sizes)

# T-shirt - Red - S
# T-shirt - Red - M
# T-shirt - Red - L
# T-shirt - Blue - S
# T-shirt - Blue - M
# T-shirt - Blue - L
# T-shirt - Black - S
# T-shirt - Black - M
# T-shirt - Black - L
# Jeans - Red - S
# Jeans - Red - M
# Jeans - Red - L
# Jeans - Blue - S
# Jeans - Blue - M
# Jeans - Blue - L
# Jeans - Black - S
# Jeans - Black - M
# Jeans - Black - L
# Jacket - Red - S
# Jacket - Red - M
# Jacket - Red - L
# Jacket - Blue - S
# Jacket - Blue - M
# Jacket - Blue - L
# Jacket - Black - S
# Jacket - Black - M
# Jacket - Black - L