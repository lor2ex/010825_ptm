""" 03 Класс Teacher и список людей

На основе класса Person создайте класс Teacher.
- У преподавателя есть имя и предмет.
- Метод introduce() должен выводить имя и предмет.

Метод introduce() должен выводить строку:
    Hello, I am professor <имя>. My subject is <предмет>.

Создайте список, в котором будут Student и Teacher,
и вызовите у всех метод introduce().

Пример вывода:
Hello, my name is Alice.
I'm on course 2.
Hello, I am professor Bob.
My subject is Mathematics
"""

class Person:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def introduce(self):
        print(f'Hello, my name is {self.name}.')
        print(f"I'm on course {self.number}")


class Student(Person):
    def __init__(self, name, number):
        super().__init__(name, number)


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name, subject)
        self.subject = subject

    def introduce(self):
        print(f"Hello, I am professor {self.name}")
        print(f"My subject is {self.subject}")


student1 = Student("Alice", 2)
teacher1 = Teacher("Bob", "Mathematics")

people = [student1, teacher1]

for person in people:
    person.introduce()

# Hello, my name is Alice.
# I'm on course 2.
# Hello, I am professor Bob.
# My subject is Mathematics


########## 2

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def introduce(self):
#         print(f"Hello, my name is {self.name}.")
#
# class Student(Person):
#     def __init__(self, name, course):
#         super().__init__(name)
#         self.course = course
#
#     def introduce(self):
#         super().introduce()
#         print(f"I'm on course {self.course}")
#
# class Teacher(Person):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject
#
#     def introduce(self):
#         print(f"Hello, I am professor {self.name}.\nMy subject is {self.subject}")