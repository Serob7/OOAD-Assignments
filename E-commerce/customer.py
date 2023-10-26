from validators import not_empty_string, email_checker
from order import Order

class Customer:
    @not_empty_string('Name', 1)
    @email_checker('Contact information', 2)
    def __init__(self, name, contact_information):
        self.name = name
        self.contact_information = contact_information
        self.purchase_history = []

    def purchase_product(self, products):
        total_price = 0
        for product in products:
            total_price += product.price
        order = Order(self, products, total_price)
        print(f'{self.name} purchased goods for total price ${total_price}')
        self.purchase_history.append(order)
        return order

    def view_history(self):
        print(f"\t{self.name}'s purchase history")
        for purchase in self.purchase_history:
            for product in purchase.products:
                print(f"{product.name} for ${product.price}: {product.description}")

    @not_empty_string('Text', 2)
    def leave_review(self, product, text):
        if product in self.purchase_history:
            product.reviews[self.name] = text



