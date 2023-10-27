from abc import ABC, abstractmethod
from validators import not_empty_string, positive_number_checker

class JobPosting(ABC):
    @abstractmethod
    def __init__(self, title, description, salary):
        ...

class FullTime(JobPosting):
    @not_empty_string('Title', 1)
    @not_empty_string('Description', 2)
    @positive_number_checker('Salary', 3)
    def __init__(self, title, description, salary):
        self.title = title
        self.description = description
        self.salary = salary


class PartTime(JobPosting):
    @not_empty_string('Title', 1)
    @not_empty_string('Description', 2)
    @positive_number_checker('Salary', 3)
    def __init__(self, title, description, salary):
        self.title = title
        self.description = description
        self.salary = salary