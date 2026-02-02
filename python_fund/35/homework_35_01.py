""" 01 Счётчик экземпляров

Создайте класс User, представляющий пользователя.
При создании должны указываться
- логин (username)
- и пароль (password).

У класса должно быть поле
- total_users, хранящее общее количество созданных пользователей.

При каждом создании нового объекта User, счётчик должен увеличиваться.

Добавьте метод
- get_total(), возвращающий количество пользователей.
Проверьте, что счётчик работает.

Пример вывода:
Total users: 2
"""

class User:
    total_users = 0

    def __init__(self, username, password):
        self.username = username
        self.password = password
        User.total_users += 1

    @staticmethod
    def get_total():
        return User.total_users



user1 = User("alice", "pass123")
user2 = User("bob", "secure456")

print(f"Total users: {User.get_total()}")

# Total users: 2


