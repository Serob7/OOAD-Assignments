from abc import ABC, abstractmethod
from validators import not_empty_string

class Recipe(ABC):
    @abstractmethod
    def __init__(self,title, ingredients, instructions):
        ...

class Vegetarian(Recipe):
    @not_empty_string('Title', 1)
    @not_empty_string('Ingredients', 2)
    @not_empty_string('Instructions', 3)
    def __init__(self,title, ingredients, instructions):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        self.comments = []
        self.ratings = []
        self.rating = 0




class Dessert(Recipe):
    @not_empty_string('Title', 1)
    @not_empty_string('Ingredients', 2)
    @not_empty_string('Instructions', 3)
    def __init__(self, title, ingredients, instructions):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        self.comments = []
        self.ratings = []
        self.rating = 0
