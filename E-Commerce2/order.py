from validators import positive_number_checker
from abc import ABC, abstractmethod

class OrderOperation(ABC):
    @abstractmethod
    def __init__(self, customer, products, total_price):
        ...
class Order(OrderOperation):
    @positive_number_checker('Total price', 3)
    def __init__(self, customer, products, total_price):
        self.customer = customer
        self.products = products
        self.total_price = total_price



