from menu_item import Menu, Apetizer, Entree
from customer import Customer
def main():
    #creating Menu instance
    menu = Menu()


    #creating dishes and adding them to menu
    salad = Apetizer('Salad', 5.99)
    steak = Entree('Steak', 29.99)
    menu.add_dish(salad)
    menu.add_dish(steak)

    #crating Customer instance
    customer = Customer('Serob', 'serob@gmail.com')

    #view the menu
    customer.view_menu(menu)

    #place orders
    menu.place_order(customer,[salad, steak])

    #view order history
    customer.view_order_history()

    #leave review
    customer.leave_review(salad, 'Very good!')
    print(salad.reviews)

if __name__ == '__main__':
    main()