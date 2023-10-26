from abc import ABC, abstractmethod
from validators import not_empty_string, email_checker

class RealEstateOperations(ABC):
    @not_empty_string('Name', 1)
    @email_checker('Contact Information', 2)
    def __init__(self, name, contact_information):
        self.name = name
        self.contact_information = contact_information

    @abstractmethod
    def manage_listing(self):
        ...
    @abstractmethod
    def client_info(self, client):
        ...

class Agent(RealEstateOperations):
    def manage_listing(self, client):
        print('\tProperty listing')
        for property in client.properties:
            print(f"Property at {property.address}, for {property.price}")

    def client_info(self, client):
        print(f" Name: {client.name}, \nEmail: {client.contact_information}")