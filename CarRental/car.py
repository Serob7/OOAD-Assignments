from abc import ABC, abstractmethod
from validators import not_empty_string, positive_number_checker

class Car(ABC):
    @abstractmethod
    def __init__(self, make, model, rental_price):
        ...


class Economy(Car):
    @not_empty_string('Make', 1)
    @not_empty_string('Model', 2)
    @positive_number_checker('Rental price', 3)

    def __init__(self, make, model, rental_price):
        self.make = make
        self.model = model
        self.price = rental_price

class Luxury(Car):
    @not_empty_string('Make', 1)
    @not_empty_string('Model', 2)
    @positive_number_checker('Rental Price', 3)

    def __init__(self, make, model, rental_price):
        self.make = make
        self.model = model
        self.price = rental_price





