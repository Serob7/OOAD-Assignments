from abc import ABC, abstractmethod
from validators import not_empty_string

class Assignment(ABC):
    @not_empty_string('Name', 1)
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def complete(self, student):
        ...

class TestAssignment(Assignment):
    def complete(self, student):
        print(f'{student.name} completed {self.name} test assignment')
        student.progress += 10

class CodeAssignment(Assignment):
    def complete(self, student):
        print(f'{student.name} completed {self.name} code assignment')
        student.progress += 10


