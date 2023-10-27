from game import Adventure, Sports
from player import Player
from console import Console


def main():
    #crate Player and Game instances
    player1 = Player('Serob', 'serob@gmail.com')
    player2 = Player('Tom', 'tom@gmil.com')
    game = Adventure('HP', 'adventure', '10.10.2023')


    #play game and compete with others
    player1.play()
    player1.play()
    player2.play()
    player1.compete(player2)

if __name__ == '__main__':
    main()