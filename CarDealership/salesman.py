from validators import not_empty_string, positive_number_checker, is_class_instance
from car import Car
class CarInventory:
    @not_empty_string('Inventory', 1)

    def __init__(self, name):
        self.name = name
        self.car_inventory = []

class Salesman:
    @not_empty_string('Name', 1)
    @positive_number_checker('Commission rate', 2)
    def __init__(self, name, commission_rate):
        self.name = name
        self.commission_rate = commission_rate
        self.sale_history = []
        self.salary = 0

    def view_sale_history(self):
        for sale in self.sale_history:
            print(sale.make, sale.model, sale.price)

    @is_class_instance(Car, 1)
    @is_class_instance(CarInventory, 2)
    def add_car(self, car, inventory):
        inventory.car_inventory.append(car)

    @is_class_instance(CarInventory, 1)
    def view_car_inventory(self, inventory):
        for item in inventory.car_inventory:
            print(item.make, item.model, item.price)





