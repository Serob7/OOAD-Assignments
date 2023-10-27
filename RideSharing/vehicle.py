from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        ...

class Car(Vehicle):
    def start(self):
        print('Car started')

class Motorcycle(Vehicle):
    def start(self):
        print('Motorcycle started')