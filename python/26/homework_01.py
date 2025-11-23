"""01 Список файлов и папок

Напишите программу, которая
- принимает путь к директории через аргумент командной строки
- и выводит:
    - Отдельно список папок
    - Отдельно список файлов

Пример запуска:
python script.py /home/user/documents

Пример вывода:
Содержимое директории '/home/user/documents':
Папки:
- folder1
- folder2
Файлы:
- file1.txt
- file2.txt
- notes.docx
"""

import os, sys



def files_and_folders(path):
    if os.path.exists(path) and os.path.isdir(path):
        files = []
        folders = []

        items = os.listdir(path)
        for item in items:
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                folders.append(item)
            elif os.path.isfile(full_path):
                files.append(item)

        print(f"Содержимое директории '{path}':")
        print("Папки:")
        for folder in folders:
            print(f"- {folder}")
        print("Файлы:")
        print("\n".join(f"- {file}" for file in files))

if len(sys.argv) != 2:
    print("Использование: python homework_01.py <директория>")
    sys.exit(1)

files_and_folders(sys.argv[1])



######### 2

# import os
# import sys
#
# usrargs = sys.argv
#
# if len(usrargs) != 2:
#     print("Usage: python HW26.py <dir>")
#     sys.exit(1)
#
# path = usrargs[1]
#
# if not os.path.isdir(path):
#     print(f"Error: {path} is not a directory")
#     sys.exit(1)
#
# print(f"Elements of directory: {path}")
# print("---")
#
# print("List of files:")
# for el in os.listdir(path):
#     if os.path.isfile(os.path.join(path, el)):
#         print(f"file - {el}")
#
# print("---")
#
# print("List of directories:")
# for d in os.listdir(path):
#     if os.path.isdir(os.path.join(path, d)):
#         print(f"dir - {d}")
















########## 2

import os
import sys
# usrargs = sys.argv
#
# if len(usrargs) != 2:
#     print("Usage: python HW26.py <dir>")
#     sys.exit(1)
#
# path = usrargs[1]
# if not os.path.isdir(path):
#     print(f"Error: {path} is not a directory")
#     sys.exit(1)
#
# print(f"Elements of directory: {path}")
#
# print("List of files:")
# for el in os.listdir(path):
#     if os.path.isfile(os.path.join(path, el)):
#         print(f"file - {el}")
#
# print("List of directories:")
# for d in os.listdir(path):
#     if os.path.isdir(os.path.join(path,d)):
#         print(f"dir - {d}")