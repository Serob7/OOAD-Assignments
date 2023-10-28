from validators import not_empty_string

class Showtime:
    @not_empty_string('Time', 3)
    def __init__(self, movie, theater, time):
        self.movie = movie
        self.theater = theater
        self.time = time


