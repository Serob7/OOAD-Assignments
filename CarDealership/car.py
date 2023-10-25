from abc import ABC, abstractmethod
from validators import not_empty_string, positive_number_checker

class Car(ABC):
    @abstractmethod
    def __init__(self, make, model, price):
        ...


class ElectricCar(Car):
    @not_empty_string('Make', 1)
    @not_empty_string('Model', 2)
    @positive_number_checker('Price', 3)

    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price

class HybridCar(Car):
    @not_empty_string('Make', 1)
    @not_empty_string('Model', 2)
    @positive_number_checker('Price', 3)

    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price





