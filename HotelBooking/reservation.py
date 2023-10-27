from abc import ABC, abstractmethod
from validators import not_empty_string

class ReservastionOperation(ABC):
    @not_empty_string('Date', 3)
    def __init__(self, guest, room, date):
        self.guest = guest
        self.room = room
        self.date = date

    @abstractmethod
    def book_room(self):
        ...

class Reservation(ReservastionOperation):
    def __init__(self, guest, room, date):
        super().__init__(guest, room, date)
    def book_room(self):
        if self.room.available:
            print(f'{self.guest.name} booked room numebr {self.room.room_no} for ${self.room.price}')
            self.room.available = not self.room.available
            self.guest.reservation_history.append(f'Booked room number {self.room.room_no} for ${self.room.price}')
        else:
            print('This room is not available at the time')


