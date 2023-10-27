from validators import not_empty_string, email_checker, positive_number_checker
from abc import ABC, abstractmethod

class RideOperations(ABC):

    @abstractmethod
    def request_ride(self, passenger, driver):
        ...

    @abstractmethod
    def accept_and_complete_ride(self, passenger, driver):
        ...




class Ride(RideOperations):
    @not_empty_string('Name', 1)
    @email_checker('Contact information', 2)
    @not_empty_string('Destination', 3)
    @positive_number_checker('Rate', 4)
    def __init__(self, name, contact_information, destination, rate):
        self.name = name
        self.contact_information = contact_information
        self.destination =destination
        self.rate = rate

    def request_ride(self, passenger, driver):
        print(f'{passenger.name} requested ride from {driver.name}')
        driver.requested_rides.append(self)

    def accept_and_complete_ride(self, passenger, driver):
        if driver.available:
            driver.available = False
            print(f"{driver.name} accepted ride request from {passenger.name}")
            driver.requested_rides.remove(self)
            print(f"{driver.name} comleted ride request from {passenger.name}, rate is {self.rate}")
            driver.available = True