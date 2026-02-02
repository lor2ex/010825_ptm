""" 02 Расширяемый логгер событий

Создайте функцию, которая
- возвращает функцию "вложенный логгер событий".

Каждый вызов логгера должен сохранять событие с текущим временем (если оно передано)
и возвращать весь список событий.

Пример вызова:
log("Загрузка данных")
log("Обработка завершена")
log("Сохранение файла")
for event in log():
    print(event)

Пример вывода:
Загрузка данных: 2025-03-24 14:06:29
Обработка завершена: 2025-03-24 14:06:29
Сохранение файла: 2025-03-24 14:06:29

"""

from datetime import datetime

def make_logger():
    events = []

    def logger(event=None):
        if event is None:
            return events
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        events.append(f"{event}: {now}")

    return logger

log = make_logger()

log("Загрузка данных")
log("Обработка завершена")
log("Сохранение файла")

for event in log():
    print(event)