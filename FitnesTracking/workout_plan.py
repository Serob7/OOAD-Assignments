from validators import positive_number_checker

class WorkoutPlan:
    def __init__(self, user, exercises, duration):
        self.user = user
        self.exercises = exercises
        self.duration = duration

