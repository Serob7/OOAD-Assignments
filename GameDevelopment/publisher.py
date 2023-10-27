from validators import not_empty_string

class Publisher:
    @not_empty_string('Name', 1)
    @not_empty_string('Contact Information', 2)
    def __init__(self, name, contact_information):
        self.name = name
        self.contact_information = contact_information
        self.created_games = []
        self.released_games = []
        self.sales = 0


    def release_game(self, game):
        if game in self.created_games:
            print(f"{game.genre} {game.title} has been realised at {game.release_date}")
            self.released_games.append(game)
        else:
            print('This name is not created by our developers')

    def sell_game(self, game):
        if game in self.released_games:
            print(f"{game.genre} {game.title} released at {game.release_date} has been sold!")
            self.sales += 1
        else:
            print('Not released game cannot be sold!')
