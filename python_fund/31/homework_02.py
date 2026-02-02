"""2. Разделение списка тегов
Реализуйте программу, которая должна:
Прочитать строку с тегами, введёнными пользователем.
Разделить её на отдельные теги, независимо от того,
чем они были разделены (запятые, точки с запятой, слэши или пробелы).
Удалить лишние пробелы и пустые значения.

Данные:
tag_input = "python_fund, data-science / machine-learning; AI  neural-networks"

Пример вывода:
['python_fund', 'data-science', 'machine-learning', 'AI', 'neural-networks']
"""
tag_input = "python_fund, data-science / machine-learning; AI  neural-networks"

import re

tags_raw = re.split(r'[,\s;/]+', tag_input)

tags = [tag for tag in tags_raw if tag]
print(tags)

# ['python_fund', 'data-science', 'machine-learning', 'AI', 'neural-networks']