""" 01 Электронное письмо

Реализуйте класс Email, который представляет электронное письмо.
Каждое письмо должно содержать:
- sender — адрес отправителя
- recipient — адрес получателя
- subject — тема письма
- body — текст письма
- date — дата отправки

Класс должен поддерживать:
- Сравнение писем по дате
- Преобразование письма в строку
- Получение длины текста письма
- Проверку на наличие текста в письме или не состоит ли текст только из пробелов

Пример использования:
e1 = Email("alice@example.com", "bob@example.com", "Meeting", "Let's meet at 10am", datetime(2024, 6, 10))
e2 = Email("bob@example.com", "alice@example.com", "Report", "", datetime(2024, 6, 11))

print(e1)
print(e2)
print("Length:", len(e1))
print("Has text:", bool(e1))
print("Is newer:", e2 > e1)

Пример вывода:
From: alice@example.com
To: bob@example.com
Subject: Meeting
- Let's meet at 10am -

From: bob@example.com
To: alice@example.com
Subject: Report
-  -

Length: 18
Has text: True
Is newer: True
"""

from datetime import datetime

class Email:
    def __init__(self, sender, recipient, subject, body, date):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.date = date

    def __str__(self):
        return f"From: {self.sender}\nTo: {self.recipient}\nSubject: {self.subject}\n- {self.body} -" # {self.body[:100]}

    def __len__(self):
        return len(self.body)

    def __bool__(self):
        return bool(self.body.strip())

    def __gt__(self, other):
        return self.date > other.date



# Пример использования
e1 = Email("alice@example.com", "bob@example.com", "Meeting", "Let's meet at 10am", datetime(2024, 6, 10))
e2 = Email("bob@example.com", "alice@example.com", "Report", "", datetime(2024, 6, 11))

print(e1)
print(e2)
print("Length:", len(e1))
print("Has text:", bool(e1))
print("Is newer:", e2 > e1)

# From: alice@example.com
# To: bob@example.com
# Subject: Meeting
# - Let's meet at 10am -
# From: bob@example.com
# To: alice@example.com
# Subject: Report
# -   -
# Length: 18
# Has text: True
# Is newer: True
