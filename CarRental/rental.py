from validators import positive_number_checker
from abc import ABC, abstractmethod

class RentalOperations(ABC):
    @positive_number_checker('Duration', 3)
    def __init__(self, customer, car, duration):
        self.customer = customer
        self.car = car
        self.duration = duration

    def rent_car(self):
        ...
class Rental(RentalOperations):
    def rent(self):
        print(f"{self.customer.name} rented {self.car.make} {self.car.model} for {self.duration} ")
        self.customer.rented_cars.append(self.car)
        return f'Rented {self.car.make} {self.car.model}'


    def return_car(self):
        if self.car in self.customer.rented_cars:
            print(f"{self.customer.name} returned {self.car.make} {self.car.model}")
            self.customer.rented_cars.remove(self.car)
            return f'Returned {self.car.make} {self.car.model}'

        else:
            print('That car was never rented')
