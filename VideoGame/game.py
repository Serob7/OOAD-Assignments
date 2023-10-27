from abc import ABC, abstractmethod
from validators import not_empty_string

class Game(ABC):
    @abstractmethod
    def __init__(self, title, genre, release_date):
        ...


class Sports(Game):
    @not_empty_string('Title', 1)
    @not_empty_string('Genre', 2)
    @not_empty_string('Release', 3)
    def __init__(self, title, genre,  release_date):
        self.title = title
        self.genre = genre
        self.release_date = release_date


class Adventure(Game):
    @not_empty_string('Title', 1)
    @not_empty_string('Genre', 2)
    @not_empty_string('Release', 3)
    def __init__(self, title, genre,  release_date):
        self.title = title
        self.genre = genre
        self.release_date = release_date
