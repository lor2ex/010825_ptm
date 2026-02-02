""" 02 Поиск и удаление файлов с указанным расширением

Напишите программу, которая
- Принимает путь к директории и расширение файлов через аргумент командной строки.
- Рекурсивно ищет файлы с этим расширением во всех вложенных папках.
- Спрашивает у пользователя, хочет ли он удалить найденные файлы.
- Если пользователь подтверждает, удаляет их.

Пример запуска
python_fund script.py /home/user/PycharmProjects/project1 .log

Пример вывода:
Найдены файлы с расширением '.log':
- logs/error.log
- logs/system.log
- logs/backup/old.log
- logs/backup/debug.log

Вы хотите удалить эти файлы? (y/n): y
Удаление завершено.
"""

import os
import sys


def find_files_with_extension(directory, extension):
    found_files = []

    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(extension):
                full_path = os.path.join(root, filename)
                found_files.append(full_path)

    return found_files


# Предварительно создаём ненужные файлы для удаления
files_log = [
    'error.log',
    'system.log',
    'old.log',
    'debug.log',
]

for file in files_log:
    with open(file, 'w') as f:
        f.write("")

if len(sys.argv) != 3:
    print("Использование: python_fund script.py <директория> <расширение>")
    sys.exit(1)

directory = sys.argv[1]
extension = sys.argv[2]

found_files = find_files_with_extension(directory, extension)

if found_files:
    print(f"Найдены файлы с расширением '{extension}':")
    for file in found_files:
        print(f"- {file}")

    answer = input("\nВы хотите удалить эти файлы? (y/n): ")

    if answer.lower() == 'y':
        for file in found_files:
            os.remove(file)
        print("Удаление завершено.")
    else:
        print("Удаление отменено.")
else:
    print(f"Файлы с расширением '{extension}' не найдены.")












############# 2

# newargs = sys.argv
# usr_path = newargs[1]
# ext = newargs[2]
# list_of_files = []
#
# if len(newargs) < 2:
#     print("Usage: python_fund HW26.py <dir> <extension>")
#     sys.exit(1)
#
# if not os.path.isdir(usr_path):
#     print(f"Error: {usr_path} is not a directory")
#     sys.exit(1)
#
# print("List of found files:")
# for root,_, files in os.walk(usr_path):
#     for file in files:
#         if file.endswith(ext):
#             list_of_files.append(os.path.join(root, file))
#             print("-",os.path.join(root, file))
#
#
# verdict = input("Victims found. Awaiting for execution... (y/n): ")
#
# while True:
#     if verdict == "y":
#         print(f"Chainsaw turned on...")
#         for v in list_of_files:
#             os.remove(v)
#         print("Successfully removed all files")
#         break
#     if verdict == "n":
#         print("Well...okay")
#         break
#     else:
#         verdict = input("Incorrect answer (y/n): ")