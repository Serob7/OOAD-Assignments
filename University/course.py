from abc import ABC, abstractmethod
from validators import not_empty_string

class Course(ABC):
    @abstractmethod
    def __init__(self, name, instructor, content):
        ...
    @abstractmethod
    def enroll(self, student):
        ...


class UndergraduateCourse(Course):
    @not_empty_string('Name', 1)
    @not_empty_string('Content', 3)
    def __init__(self, name, instructor, content):
        self.name = name
        self.instructor = instructor
        self.content = content
        self.students = []

    def enroll(self, student):
        print(f'{student.name} enrolled to {self.name} Undergraduate course')
        self.students.append(student)

class GraduateCourse(Course):
    @not_empty_string('Name', 1)
    @not_empty_string('Content', 3)
    def __init__(self, name, instructor, content):
        self.name = name
        self.instructor = instructor
        self.content = content
        self.students = []

    def enroll(self, student):
        self.students.append(student)
        student.courses.append(self)
        print (f'{student.name} enrolled to {self.name} Graduate course')

