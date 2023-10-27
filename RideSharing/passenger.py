from validators import not_empty_string, email_checker
from ride import Ride
class Passenger:
    @not_empty_string('Name', 1)
    @email_checker('Contact information', 2)
    def __init__(self, name, contact_information):
        self.name = name
        self.contact_information = contact_information
        self.reviews = []


    def write_review(self, driver, text):
        driver.reviews.append(text)

    def request_ride(self, driver,name, contact, destination, rate ):
        ride = Ride(name, contact, destination, rate)
        ride.request_ride(self, driver)