from movie import DramaMovie, ComedyMovie
from customer import Customer, RentalOperations
from rentals import Rental

def main():
    #creating customer, movie, rental instances
    customer = Customer('Serob', 'serob@gmai.com')
    movie = DramaMovie('Life is wonderful', 10)
    movie2 = ComedyMovie('We are Millers', 8.5)
    rental = Rental(customer, 3.5)
    rental.movies[movie.title] = movie
    rental.movies[movie2.title] = movie2



    #rent, return movies, view history
    customer.rent_movie(rental, 'Life is wonderful')
    customer.return_movie(rental, 'Life is wonderful')

    customer.view_rental_history()

if __name__ == '__main__':
    main()

