from abc import ABC, abstractmethod
from validators import not_empty_string, positive_integer_checker

class Theater(ABC):
    @not_empty_string('Location', 1)
    @positive_integer_checker('Seating capacity', 2)
    def __init__(self, location, seating_capacity):
        self.location = location
        self.seating_capacity = seating_capacity


class Standard(Theater):
    ...
class IMAX(Theater):
    ...

