from abc import ABC, abstractmethod
from validators import not_empty_string, email_checker
from workout_plan import WorkoutPlan

class FitnessTrackingOperation(ABC):
    @not_empty_string('Name', 1)
    @email_checker('Contact information', 2)
    def __init__(self, name, contact_information):
        self.name = name
        self.contact_information = contact_information
        self.favorite_exercises = []
        self.progress = 0

    @abstractmethod
    def view_progress(self):
        pass

    @abstractmethod
    def create_workout_plans(self, exercises, duration):
        ...

    @abstractmethod
    def follow_plan(self, plan):
        ...

    @abstractmethod
    def connect_with_others(self, other):
        ...

class User(FitnessTrackingOperation):
    def create_workout_plans(self, exercises, duration):
        plan = WorkoutPlan(self, exercises, duration)
        print(f'Workout plan has been created by {self.name} with {[exercise.name for exercise in exercises]} for {duration} minutes.')
        return plan

    def follow_plan(self, plan):
        for exercise in plan.exercises:
            print(f'Doing {exercise.name} exercise for {exercise.muscle_group_targeted} muscles.')
            self.progress += 10

    def view_progress(self):
        print(f"\t{self.name}'s progress")
        print(self.progress)

    def connect_with_others(self, other):
        if isinstance(other, User):
            print(f'{self.name} is sending regards to {other.name}')

