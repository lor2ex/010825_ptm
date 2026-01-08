""" 02 Добавление заметок

Продолжите предыдущую программу:
- создайте таблицу notes с полями: id, title, content
- вставьте одну заметку в таблицу
- выполните commit() после вставки
- выведите все заметки используя в формате dict (а не tuple!)

Пример вывода:

All notes:
{'id': 1, 'title': 'First Note', 'content': 'This is the content of my first note.'}

"""

import mysql.connector
from local_settings import dbconfig_write

db_name = "010825_al_notes_app"

q1_create = """
            CREATE TABLE IF NOT EXISTS notes \
            ( \
                id \
                INT \
                AUTO_INCREMENT \
                PRIMARY \
                KEY, \
                title \
                VARCHAR \
            ( \
                100 \
            ),
                content VARCHAR \
            ( \
                100 \
            )
                ) \
            """

q2_insert = """
            INSERT INTO notes (title, content) \
            VALUES (%s, %s) \
            """

with mysql.connector.connect(**dbconfig_write) as conn:
    with conn.cursor(dictionary=True) as cursor:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        cursor.execute(f"USE {db_name}")
        print(f"Database '{db_name}' created or already exists.")

        cursor.execute(q1_create)
        cursor.execute(q2_insert, ('First Note', 'This is the content of my first note.'))

        conn.commit()

        cursor.execute("SELECT * FROM notes")
        print("\nAll notes:")
        for row in cursor.fetchall():
            print(row)

# Database 'notes_app_112226_abcdefg' created or already exists.
#
# All notes:
# {'id': 1, 'title': 'First Note', 'content': 'This is the content of my first note.'}
#
# Process finished with exit code 0
