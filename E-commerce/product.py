from abc import ABC, abstractmethod
from validators import not_empty_string, positive_number_checker

class Product(ABC):
    @abstractmethod
    def __init__(self, name, price, description):
        ...

class Electronics(Product):
    @not_empty_string('Name', 1)
    @positive_number_checker('Price', 2)
    @not_empty_string('Description', 3)

    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description
        self.reviews = {}


class Clothing(Product):
    @not_empty_string('Name', 1)
    @positive_number_checker('Price', 2)
    @not_empty_string('Description', 3)

    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description
        self.reviews = {}


