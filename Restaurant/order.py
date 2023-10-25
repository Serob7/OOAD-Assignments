from validators import positive_number_checker
class Order:
    @positive_number_checker('Total price', 3)
    def __init__(self, customer, dishes, total_price):
        self.customer = customer
        self.dishes = dishes
        self.total_price = total_price





