from abc import ABC, abstractmethod
from validators import not_empty_string, email_checker
from game import Strategy, Action

class GameOperations(ABC):
    @not_empty_string('Name', 1)
    @email_checker('Contact Information', 2)
    def __init__(self, name, contact_information):
        self.name = name
        self.contact_information = contact_information

    @abstractmethod
    def create_strategy_game(self, title, genre, release_date, publisher):
        ...

    @abstractmethod
    def create_action_game(self, title, genre, release_date, publisher):
        ...
class Developer(GameOperations):
    def create_strategy_game(self, title, genre, release_date, publisher):
        game = Strategy(title, genre, release_date)
        print(f"{self.name} created {game.title} strategy game")
        publisher.created_games.append(game)
        return game

    def create_action_game(self, title, genre, release_date, publisher):
        game = Action(title, genre, release_date)
        print(f"{self.name} created {game.title} action game")
        publisher.created_games.append(game)
        return game
