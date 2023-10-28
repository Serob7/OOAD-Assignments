from exercise import Cardio, Strength
from user import User
from workout_plan import WorkoutPlan

def main():
    #create User and Exercise instances
    user = User('Serob', 'serob@gmail.com')
    user2 = User('Tom', 'tom@gmail.com')
    exercise = Cardio('Running', 'Legs')
    exercise2 = Strength('Push ups', 'Chest and sholders')


    #create and follow workout plans, view progress
    plan = user.create_workout_plans([exercise, exercise2], 55)
    user.follow_plan(plan)
    user.view_progress()


    #connect with other fitness enthusiasts
    user.connect_with_others(user2)
if __name__ == '__main__':
    main()