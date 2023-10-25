from abc import ABC, abstractmethod
from validators import positive_integer_checker, is_class_instance
from customer import Customer
from salesman import Salesman, CarInventory
from car import Car
class SaleOperation(ABC):
    @positive_integer_checker('Operation ID', 1)
    def __init__(self, operation_id):
        self.operation_id = operation_id

    @abstractmethod
    @is_class_instance(Customer, 1)
    @is_class_instance(Salesman, 2)
    @is_class_instance(Car, 3)
    @is_class_instance(CarInventory, 4)
    def sell_car(self, customer, salesman, car, inventory):
        ...

class SellCar(SaleOperation):
    def sell_car(self, customer, salesman, car, inventory):
        print(f"{salesman.name} sold {car.make} {car.model} for {car.price} to {customer.name}")
        salesman.sale_history.append(f"{self.operation_id}: {car.make} {car.model} for {car.price} to {customer.name}")
        inventory.remove(car)
