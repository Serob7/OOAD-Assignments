from validators import not_empty_string
from abc import ABC, abstractmethod
from playlist import Playlist

class MusicOperations(ABC):

    @abstractmethod
    def listen(self, song):
        pass
    @abstractmethod
    def create_playlist(self, name):
        pass

class User(MusicOperations):
    @not_empty_string('Name', 1)
    def __init__(self, name):
        self.name = name
        self.playlists = {}
        self.listening_history = []

    def listen(self, song):
        print(f"{self.name} is listening to {song.title}")
        self.listening_history.append(song)

    def create_playlist(self, name):
        if name not in self.playlists:
            playlist = Playlist(name)
            self.playlists[name] = playlist.songs
            return playlist

        else:
            print(f"{name} already exists")

    def view_listening_history(self):
        for song in self.listening_history:
            print (f"{song.title} by {song.artist}, lasting {song.length} minutes")



