from validators import not_empty_string, email_checker
from abc import ABC, abstractmethod
class RentalOperations(ABC):
    @abstractmethod
    def rent_movie(self, rental, title):
        ...
    @abstractmethod
    def return_movie(self, rental, title):
        ...
    @abstractmethod
    def view_rental_history(self):
        ...

class Customer(RentalOperations):
    @not_empty_string('Name', 1)
    @email_checker('Contact information', 2)
    def __init__(self, name, contact_information):
        self.name = name
        self.contact_information = contact_information
        self.rented_movies = {}
        self.rental_history = []

    def rent_movie(self, rental, title):
        if title in rental.movies:
            movie = rental.movies.pop(title)
            self.rented_movies[title] = movie
            self.rental_history.append(['Rented', movie])

    def return_movie(self, rental, title):
        if title in self.rented_movies:
            movie = self.rented_movies.pop(title)
            rental.movies[title] = movie
            self.rental_history.append(['Returned', movie])

    def view_rental_history(self):
        for history in self.rental_history:
            print(f'{history[0]}: {history[1].title}, {history[1].genre} with {history[1].rating} rating')