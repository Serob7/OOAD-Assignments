from validators import  positive_number_checker, not_empty_string
from abc import ABC, abstractmethod
from order import Order


class Dish(ABC):
    @abstractmethod
    def display(self):
        pass


class Apetizer(Dish):

    @not_empty_string('Name', 1)
    @positive_number_checker('Price', 2)
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        return (f"Apetizer: {self.name} - ${self.price}")


class Entree(Dish):

    @not_empty_string('Name', 1)
    @positive_number_checker('Price', 2)
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        return (f"Entree: {self.name} - ${self.price}")

class MenuOperations(ABC):
    @abstractmethod
    def add_dish(self, dish):
        pass
    @abstractmethod
    def display_menu(self):
        pass

    def place_order(self, customer, dishes):
        total_price = 0
        for dish in dishes:
            total_price += dish.price
        order = Order(customer, dishes, total_price)
        print(f"{customer.name} placed order for  ${total_price}")
        customer.order_history.append(order)
        return order



class Menu(MenuOperations):
    def __init__(self):
        self.dishes = []


    def add_dish(self, dish):
        self.dishes.append(dish)


    def display_menu(self):
        for dish in self.dishes:
            print(dish.display())



