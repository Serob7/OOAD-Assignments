from abc import ABC, abstractmethod
from validators import not_empty_string, email_checker
from rating import Rating

class Operations(ABC):
    @abstractmethod
    def search_recipe(self, recipe):
        ...
    @abstractmethod
    def search_recipe(self, recipe):
        ...

    @abstractmethod
    def save_recipe(self, recipe):
        ...

    @abstractmethod
    def share_fav_recipes(self):
        ...

    @abstractmethod
    def comment(self, recipe, text):
        ...

    @abstractmethod
    def rate(self, score, recipe):
        ...



class User(Operations):
    @not_empty_string('Name', 1)
    @email_checker('Contact Information', 2)
    def __init__(self, name, contact_information):
        self.name = name
        self.contact_information = contact_information
        self.fav_recipes = []

    def search_recipe(self, recipe):
        print(f'Checking now {recipe.title}')


    def save_recipe(self, recipe):
        print('I am saving this recipe')
        self.fav_recipes.append(recipe)

    def share_fav_recipes(self):
        for recipe in self.fav_recipes:
            print(f'{recipe.title}: \nIngredients: {recipe.ingredients}\n Instructions: {recipe.instructions}')

    def comment(self, recipe, text):
        recipe.comments.append(text)

    def rate(self, score, recipe):
        rate = Rating(recipe, self, score)
        recipe.ratings.append(rate)
        ratings_total = 0
        for i in range(len(recipe.ratings)):
            ratings_total += recipe.ratings[i].score
            recipe.rating = ratings_total / (i + 1)




