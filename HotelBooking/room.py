from abc import ABC, abstractmethod
from validators import not_empty_string, positive_number_checker, positive_integer_checker

class Room(ABC):
    @abstractmethod
    def __init__(self, room_no, price, amenities):
        ...

class StandardRoom(Room):
    @positive_integer_checker('Room number', 1)
    @positive_number_checker('Price', 2)
    @not_empty_string('Amenities', 3)
    def __init__(self, room_no, price, amenities):
        self.room_no = room_no
        self.price = price
        self.amenities = amenities
        self.available = True
        self.feedback = []


class DeluxeRoom(Room):
    @positive_integer_checker('Room number', 1)
    @positive_number_checker('Price', 2)
    @not_empty_string('Amenities', 3)
    def __init__(self, room_no, price, amenities):
        self.room_no = room_no
        self.price = price
        self.amenities = amenities
        self.available = True

