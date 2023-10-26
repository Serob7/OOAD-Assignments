from validators import positive_number_checker

class Rental:
    @positive_number_checker('Duration', 2)
    def __init__(self, customer, duration):
        self.customer = customer
        self. duration = duration
        self.movies = {}
        self.rented_movies = []



