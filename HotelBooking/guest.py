from validators import not_empty_string, email_checker
from reservation import Reservation

class Guest:
    @not_empty_string('Name', 1)
    @email_checker('Contact information', 2)
    def __init__(self, name, contact_information):
        self.name = name
        self.contact_information = contact_information
        self.reservation_history = []


    def book_avail_room(self, room, date):
        booked = Reservation(self, room, date)
        booked.book_room()

    def leave_feedback(self,room, text):
        room.feedback.append(text)
    def view_reservation_history(self):
        print('\tReservation history')
        for history in self.reservation_history:
            print(history)
