""" 01 Фильтрация по ключевому слову

Напишите программу, которая
- ищет в файле все строки, содержащие указанное пользователем слово,
- и сохраняет их в новый файл.

Имя нового файла формируется как <keyword>_<original_filename>.
Если файл не существует, программа должна вывести ошибку.
Если совпадения не найдены, новый файл не создаётся.

Используйте файл system_log.txt.

Пример ввода:
Введите имя файла для поиска: system_log.txt
Введите ключевое слово: error

Пример вывода:
Строки, содержащие 'error', сохранены в <keyword>_<original_filename>.

"""

def find_keyword(filename: str, keyword: str) -> None:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
            error_lines = [line for line in lines if keyword in line]

        if error_lines:
            new_name = keyword + "_" + filename
            with open(new_name, "w", encoding="utf-8") as f_out:
                f_out.writelines(error_lines)
            print(f'Строки, содержащие {keyword}, сохранены в {new_name}')
        else:
            print(f'Строки, содержащие {keyword}, не найдены')

    except FileNotFoundError as e:
        print(f'file not found: {e}')



find_keyword('s', 'error')
# File not found: [Errno 2] No such file or directory: 's'

find_keyword('system_log.txt', 'error')
# Строки, содержащие 'error', сохранены в error_system_log.txt.











###### 2

# from collections import Counter

# def find_keyword(filename: str, keyword: str) -> None: # 2 usages
#
# try:
#     with open(filename, 'r', encoding='utf-8') as f:
#         lines = f.readlines()
#         lines_k = list(s for s in lines if keyword in s)
#         if lines_k:
#             fn2 = keyword + '_' + filename
#             with open(fn2, "w", encoding="utf-8") as f2:
#                 f2.writelines(lines_k)
#                 print(f"Строки, содержащие '{keyword}', сохранены в {fn2}")
#
# except FileNotFoundError as e:
#     print(f'File {filename} not found. {e}')