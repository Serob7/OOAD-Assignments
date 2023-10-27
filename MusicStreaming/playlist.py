from validators import not_empty_string

class Playlist:
    @not_empty_string('Name', 1)
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def view_playlist(self):
        print(f"Playlist {self.name}:")
        for song in self.songs:
            print(f"\t {song.title} by {song.artist}")
        print('\n')
