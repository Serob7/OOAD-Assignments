from driver import Driver
from passenger import Passenger
from ride import Ride
from vehicle import Car, Motorcycle

def main():
    #create Ride, Passenger, Driver instances
    ride = Ride('Yandex', 'yandex@gmail.com', 'Abovyan', 2000)
    passenger = Passenger('Serob', 'serob@gmial.cpm')
    vehicle = Car()
    driver = Driver('Gegham', 'gegham@gjns.evs', vehicle)


    #request, accept and complete rides
    passenger.request_ride(driver, 'yandex', 'yandex@enk.ce', 'Abovyan', 2000)
    driver.accept_ride(passenger, 'yandex', 'yandex@enk.ce', 'Abovyan', 2000 )


    # review each other
    driver.write_review(passenger, 'Nice passenger')
    passenger.write_review(driver, 'Nice driver')

if __name__ == '__main__':
    main()