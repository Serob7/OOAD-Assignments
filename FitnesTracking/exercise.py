from abc import ABC, abstractmethod
from validators import not_empty_string

class Exercise(ABC):
    @abstractmethod
    def __init__(self, name, muscle_group_targeted):
        ...

class Cardio(Exercise):
    @not_empty_string('Name', 1)
    @not_empty_string('Muscle group targeted', 2)
    def __init__(self, name, muscle_group_targeted):
        self.name = name
        self.muscle_group_targeted = muscle_group_targeted

class Strength(Exercise):
    @not_empty_string('Name', 1)
    @not_empty_string('Muscle group targeted', 2)
    def __init__(self, name, muscle_group_targeted):
        self.name = name
        self.muscle_group_targeted = muscle_group_targeted
