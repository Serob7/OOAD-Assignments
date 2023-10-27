from validators import not_empty_string, email_checker
from rental import Rental

class Customer:
    @not_empty_string('Name', 1)
    @not_empty_string('Contact information', 2)
    @email_checker('Contact information', 2)

    def __init__(self, name, contact_information):
        self.name = name
        self.contact_information = contact_information
        self.rented_cars = []
        self.rental_history = []


    def rent_car(self, car, duration):
        rental = Rental(self, car, duration)
        rent = rental.rent()
        self.rental_history.append(rent)

    def return_car(self, rental):
        returned = rental.return_car()
        self.rental_history.append(returned)


    def view_rental_history(self):
        for rental in self.rental_history:
            print(rental)