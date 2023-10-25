from validators import not_empty_string, email_checker, is_class_instance
from car import Car
from salesman import CarInventory, Salesman

class Customer:
    @not_empty_string('Name', 1)
    @not_empty_string('Contact information', 2)
    @email_checker('Contact information', 2)

    def __init__(self, name, contact_information):
        self.name = name
        self.contact_information = contact_information

    @is_class_instance(CarInventory, 1)
    @is_class_instance(Car, 2)
    @is_class_instance(Salesman, 3)
    def purchase_car(self, inventory, car, salesman):
        if car in inventory.car_inventory:
            print(f"{self.name} purchased {car.make} {car.model} for {car.price} from {salesman.name}")
            inventory.car_inventory.remove(car)
            salesman.sale_history.append(car)
        else:
            print(f"There are no {car.make} {car.model}s in {inventory.name}")
