"""01 Анализ курсов студентов

Реализуйте программу, которая должна:
1. Прочитать файл student_courses.json, содержащий:
    - Имя
    - дату рождения (birth_date) в формате дд.мм.гггг
    - дату поступления (enrollment_date) в том же формате
    - список курсов.

2. Вычислить:
    - общее количество студентов.
    - средний возраст на момент поступления.
    - количество студентов на каждом курсе.

3. Сохранить отчёт в JSON-файл student_courses_report.json.
"""

import json
from collections import Counter
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta as rld


def read_json(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)



def write_json(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def get_info():
    students = read_json("student_courses.json")
    total_students = len(students)

    ages = []
    for student in students:
        birth = dt.strptime(student["birth_date"], "%d.%m.%Y")
        enroll = dt.strptime(student["enrollment_date"], "%d.%m.%Y")
        age = rld(enroll, birth).years
        ages.append(age)  # ← ДОБАВИЛИ

    average_age = sum(ages) / len(ages)

    course_counter = Counter()
    for student in students:
        for course in student["courses"]:
            course_counter[course] += 1

    report = {
        "total_students": total_students,
        "average_enrollment_age": average_age,
        "students_per_course": dict(course_counter),  # ← dict()
    }

    write_json("student_courses_report.json", report)
    print("Отчет успешно сохранен в student_courses_report.json")
    print(json.dumps(report, indent=4, ensure_ascii=False))


get_info()
