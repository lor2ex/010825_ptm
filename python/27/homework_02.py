""" 02 Поиск и удаление дубликатов

Напишите программу, которая
- удаляет дублирующиеся строки из файла
- и сохраняет результат в новый файл.

Имя нового файла формируется как unique_<original_filename>.

Если файл не существует, программа должна вывести ошибку.

Исходный порядок строк должен сохраниться.
Если в файле нет дубликатов, создаётся точная копия файла.

Используйте файл movies_to_watch.txt.

Пример ввода:
Введите имя файла: movies_to_watch.txt

Пример вывода:
Дубликаты удалены. Уникальные строки сохранены в unique_movies_to_watch.txt.

"""

def remove_duplicates(filename: str) -> None:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()

        unique_lines = list(dict.fromkeys(lines))

        new_name = f'unique_{filename}'
        with open(new_name, "w", encoding="utf-8") as f_out:
            f_out.writelines(unique_lines)
        print(f'Дубликаты удалены. Уникальные строки сохранены в {new_name}')

    except FileNotFoundError as e:
        print(f'file not found: {e}')



remove_duplicates("movies_to_watch.txt")
# Дубликаты удалены. Уникальные строки сохранены в unique_movies_to_watch.txt.

remove_duplicates("M")
# File not found: [Errno 2] No such file or directory: 'M'



############### 2

# def remove_duplicates(filename: str) -> None:
#     try:
#         with open(filename, "r", encoding="utf-8") as f:
#             lines = f.readlines()
#             seen = set()
#             unique_lines = []
#             for line in lines:
#                 if line not in seen:
#                     unique_lines.append(line)
#                     seen.add(line)
#
#         new_name = f'unique_{filename}'
#         with open(new_name, "w", encoding="utf-8") as f_out:
#             f_out.writelines(unique_lines)
#         print(f'Дубликаты удалены. Уникальные строки сохранены в {new_name}')
#
#     except FileNotFoundError as e:
#         print(f'file not found: {e}')

############ 3

# from collections import Counter
#
#
# def remove_duplicates(filename: str) -> None:  # 2 usages
#
#
# try:
#     with open(filename, 'r', encoding='utf-8') as f:
#         lines = tuple(l.strip() for l in f.readlines())
#         uniq_lines = []
#         for line in lines:
#             if line not in uniq_lines:
#                 uniq_lines.append(line)
#
#         with open('unique_' + filename, 'a', encoding='utf-8') as f_unique:
#             for line in uniq_lines:
#                 f_unique.write(line + '\n')
#
#     # если надо было сохранять только те строки, которые встречаются один раз:
#     # count_lines = dict(Counter(lines))
#     # uniq_lines = tuple(l for l, c in count_lines.items() if c == 1)
#     # print(uniq_lines)
#
# except FileNotFoundError as e:
#     print(f'File {filename} not found: {e}')
#
# remove_duplicates("movies_to_watch.txt")
# # Дубликаты удалены. Уникальные строки сохранены в unique_movies_to_watch.txt.
#
# remove_duplicates("M")
# File not found: [Errno 2] No such file or directory: 'M'