from abc import ABC, abstractmethod
from validators import not_empty_string, positive_number_checker

class Song(ABC):
    @abstractmethod
    def __init__(self, title, artist, duration):
        ...

    @abstractmethod
    def play(self):
         ...

class Rock(Song):
    @not_empty_string('Title', 1)
    @not_empty_string('Artist', 2)
    @positive_number_checker('duration', 3)
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def play(self):
        print(f"Rocking {self.title}!!!")

class Pop(Song):
    @not_empty_string('Title', 1)
    @not_empty_string('Artist', 2)
    @positive_number_checker('duration', 3)
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def play(self):
        print(f"Playing {self.title}!!!")

