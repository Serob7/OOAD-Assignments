from validators import not_empty_string, email_checker
class Customer:
    @not_empty_string('Name', 1)
    @email_checker('Contact information', 2)
    def __init__(self, name, contact_information):
        self.name = name
        self.contact_information = contact_information
        self.order_history = []

    def view_menu(self, menu):
        menu.display_menu()


    def view_order_history(self):
        for order in self.order_history:
            for dish in order.dishes:
                print(dish.name, end = ', ')
            print(order.total_price)

    def leave_review(self, dish, text):
        dish.reviews.append(text)



