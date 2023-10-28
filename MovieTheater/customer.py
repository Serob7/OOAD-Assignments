from abc import ABC, abstractmethod
from validators import positive_integer_checker

class MovieOperations(ABC):
    @abstractmethod
    def reserve_seats(self, showtime, amount):
        ...
    @abstractmethod
    def purchase_tickets(self, showtime, amount):
        ...


class Customer(MovieOperations):
    @positive_integer_checker('Amount', 2)
    def reserve_seats(self, showtime, amount):
        showtime.theater.seating_capacity -= amount
        print(f'{amount} tickets have been reserved for {showtime.movie.title}')
    @positive_integer_checker('Amount', 2)

    def purchase_tickets(self, showtime, amount):
        print(f'{amount} tickets have bee purchased for {showtime.movie.title}')


