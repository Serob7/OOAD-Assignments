from song import Rock, Pop
from user import User

def main():
    #creating Song instances
    rock = Rock('IEAIAIO', 'SOAD', 4.23)
    pop = Pop('Be alright', 'Lewis Dean', 3.55)

    #creating User instance
    user = User("Serob")

    #listening songs and view listening history
    user.listen(rock)
    user.listen(pop)
    user.listen(rock)
    print(f"{user.name}'s listening history")
    user.view_listening_history()
    print('\n')

    #create and manage playlists
    playlist = user.create_playlist('Some songs')
    playlist.add_song(rock)
    playlist.add_song(pop)
    print(f"{user.name}'s playlists")
    playlist.view_playlist()

if __name__ == '__main__':
    main()