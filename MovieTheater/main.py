from movie import Movie
from customer import  Customer
from theater import IMAX, Standard
from showtime import Showtime

def main():
    #create Customer, Movie, Theater, Showtime  instances
    customer = Customer()
    movie = Movie('Openheimer','Historical', 3 )
    theater = IMAX('Yerevan', 40)
    showtime = Showtime(movie, theater, '4:45')



    #reserve tickets
    customer.reserve_seats(showtime, 2)
    customer.purchase_tickets(showtime, 2)



if __name__ == '__main__':
    main()