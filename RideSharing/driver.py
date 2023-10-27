from validators import not_empty_string, email_checker
from ride import Ride
class Driver:
    @not_empty_string('Name', 1)
    @email_checker('Contact information', 2)
    def __init__(self, name, contact_information, vehicle):
        self.name = name
        self.contact_information = contact_information
        self.vehicle = vehicle
        self.requested_rides = []
        self.available = True
        self.reviews = []

    def write_review(self, passenger, text):
        passenger.reviews.append(text)

    def accept_ride(self, passenger, name, contact_information, destination, rate):
        ride = Ride(name, contact_information, destination, rate)
        ride.request_ride(passenger, self)
