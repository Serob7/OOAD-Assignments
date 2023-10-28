from validators import  positive_integer_checker

class Rating:
    @positive_integer_checker('Score', 3)
    def __init__(self, recipe, user, score):
        self.recipe = recipe
        self.user = user
        self.score = score

