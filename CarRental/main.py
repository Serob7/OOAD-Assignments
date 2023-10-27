from car import Luxury, Economy
from customer import Customer
from rental import Rental

def main():
    #craete Customer, Car instance
    customer = Customer('Serob', 'serob@gmail.com')
    lux_car = Luxury('Range Rover', 'Sport', 24)
    economy_car = Economy('Hyundai', 'Elantra', 48)
    rental = Rental(customer, lux_car, 24)

    #rent, return a car and view history
    customer.rent_car(lux_car, 14)
    customer.return_car(rental)
    print('\tRental history')
    customer.view_rental_history()

if __name__ == '__main__':
    main()