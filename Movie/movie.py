from abc import ABC, abstractmethod
from validators import not_empty_string, positive_number_checker
class Movie(ABC):
    @abstractmethod
    def __init__(self, title, rating, genre):
        ...

class ComedyMovie(Movie):
    @not_empty_string('Title', 1)
    @positive_number_checker('Rating', 2)
    def __init__(self, title, rating, genre = 'Comedy'):
        self.title = title
        self.genre = genre
        self.rating = rating

class DramaMovie(Movie):

    @not_empty_string('Title', 1)
    @positive_number_checker('Rating', 2)
    def __init__(self, title, rating, genre = 'Drama'):
        self.title = title
        self.genre = genre
        self.rating = rating