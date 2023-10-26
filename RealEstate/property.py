from abc import ABC, abstractmethod
from validators import not_empty_string, positive_number_checker

class Property(ABC):
    @abstractmethod
    def __init__(self, address, price, feature):
        ...

class Residental(Property):
    @not_empty_string('Address', 1)
    @positive_number_checker('Price', 2)
    @not_empty_string('Features', 3)
    def __init__(self, address, price, feature):
        self.address = address
        self.price = price
        self.features = feature
        self.owner = ''


class Commercial(Property):
    @not_empty_string('Address', 1)
    @positive_number_checker('Price', 2)
    @not_empty_string('Features', 3)
    def __init__(self, address, price, feature):
        self.address = address
        self.price = price
        self.features = feature
        self.owner = ''


