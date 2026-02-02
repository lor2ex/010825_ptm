""" 01 Создание базы

Напишите программу, которая:
- создаёт базу данных notes_app_<your_group>_<your_full_name>
- выбирает эту базу через USE notes_app
- выводит сообщение о результате

Пример вывода:
Database 'notes_app' created or already exists.
"""

import mysql.connector
from local_settings import dbconfig_write

db_name = "010825_al_notes_app"

with mysql.connector.connect(**dbconfig_write) as conn:
    with conn.cursor() as cursor:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        cursor.execute(f"USE {db_name}")

        print(f"Database '{db_name}' created or already exists.")

# Database 'notes_app_112226_abcdefg' created or already exists.
