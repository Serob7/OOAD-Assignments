from recipe import Vegetarian, Dessert
from user import User
from rating import Rating


def main():
    #create Recipe, User instances
    user = User('Serob', 'serob@fjanv.ews')
    recipe = Vegetarian('Salad', 'tomato, potato', 'cut, mix and add olive oil')

    #search for recipe
    user.search_recipe(recipe)

    #save and share favorite recipes
    user.save_recipe(recipe)
    user.share_fav_recipes()

    #rate and comment
    user.comment(recipe, 'Love it!')
    user.rate(8.5, recipe)


if __name__ == '__main__':
    main()