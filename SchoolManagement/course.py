from abc import ABC, abstractmethod
from validators import not_empty_string

class Course(ABC):
    @abstractmethod
    def __init__(self, name, teacher):
        ...
    @abstractmethod
    def enroll(self, student):
        ...


class Math(Course):
    @not_empty_string('Name', 1)
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.enrolled_students = []

    def enroll(self, student):
        print(f'{student.name} enrolled to {self.name} Math course')
        self.enrolled_students.append(student)

class English(Course):
    @not_empty_string('Name', 1)
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.enrolled_students = []

    def enroll(self, student):
        self.enrolled_students.append(student)
        print (f'{student.name} enrolled to {self.name} English course')

