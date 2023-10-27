from room import DeluxeRoom, StandardRoom
from guest import Guest
from reservation import Reservation

def main():
    #creating Guest and Rooom instances
    guest = Guest('Serob', 'serob@gmail.com')
    guest2 = Guest('Tom','tom@gmail.com')
    room1 = StandardRoom(1123, 150, 'cool TV')
    room2 = DeluxeRoom(1222, 300, 'cool everything')


    #book room, try to rebook, view history, leave feedback
    guest.book_avail_room(room1, '24.10.2023')
    guest2.book_avail_room(room1, '24.10.2023')
    guest.view_reservation_history()
    guest.leave_feedback(room1, 'yes, the tv is cool')

if __name__ == '__main__':
    main()