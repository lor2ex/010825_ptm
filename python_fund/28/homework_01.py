""" 01 Фильтрация по ключевому слову

Напишите программу, которая помогает планировать дела.
Программа должна
- бесконечно выводить план на следующий день недели,
- пока пользователь нажимает 'Enter'.

Данные:
# Расписание дел на неделю
weekly_schedule = {
    "Monday": ["Gym", "Work", "Read book"],
    "Tuesday": ["Meeting", "Work", "Study Python"],
    "Wednesday": ["Shopping", "Work", "Watch movie"],
    "Thursday": ["Work", "Call parents", "Play guitar"],
    "Friday": ["Work", "Dinner with friends"],
    "Saturday": ["Hiking", "Rest"],
    "Sunday": ["Family time", "Rest"]
}

Пример ввода:
Нажмите 'Enter' для получения плана:
Monday: Gym, Work, Read book
Нажмите 'Enter' для получения плана:
Tuesday: Meeting, Work, Study Python
...
Нажмите 'Enter' для получения плана:
Sunday: Family time, Rest
Нажмите 'Enter' для получения плана:
Monday: Gym, Work, Read book
Нажмите 'Enter' для получения плана: q
"""
from itertools import cycle

weekly_schedule = {
    "Monday": ["Gym", "Work", "Read book"],
    "Tuesday": ["Meeting", "Work", "Study Python"],
    "Wednesday": ["Shopping", "Work", "Watch movie"],
    "Thursday": ["Work", "Call parents", "Play guitar"],
    "Friday": ["Work", "Dinner with friends"],
    "Saturday": ["Hiking", "Rest"],
    "Sunday": ["Family time", "Rest"]
}


def weekly_planner(schedule):
    days_cycle = cycle(schedule.keys())

    while True:
        user_input = input("Нажмите 'Enter' для получения плана: ")

        if user_input == 'q':
            print("До свидания!")
            break

        else:
            day = next(days_cycle)
            tasks = schedule[day]
            tasks_str = ", ".join(tasks)
            print(f'{day}: {tasks_str}')

weekly_planner(weekly_schedule)



 #################### Аналог cycle
# days = list(schedule.keys())
# i = 0
#
# while True:
#     day = days[i]
#     i = (i + 1) % len(days)  # возвращаемся к 0 после последнего
