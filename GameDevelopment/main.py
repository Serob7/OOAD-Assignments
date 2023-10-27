from game import Strategy, Action
from developer import Developer
from publisher import Publisher

def main():
    #create Developer and Publisher instance
    developer = Developer('Serob', 'serob@gmail.com')
    publisher = Publisher('Tom', 'tom@gmail.com')
    print('\n')

    #create games
    action_game = developer.create_action_game('NFS', 'Action', '14.10.2004', publisher)
    strategy_game = developer.create_strategy_game('Strangold', 'Strategy', '28.11.2000', publisher)
    print('\n')


    #release and sell games
    publisher.release_game(action_game)
    publisher.release_game(strategy_game)
    print('\n')

    publisher.sell_game(action_game)
    publisher.sell_game(strategy_game)

if __name__ == '__main__':
    main()