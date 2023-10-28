from validators import not_empty_string, positive_number_checker


class Movie:
    @not_empty_string('Title', 1)
    @not_empty_string('Genre', 2)
    @positive_number_checker('Length', 3)
    def __init__(self, title, genre, length):
        self.title = title
        self.genre = genre
        self.length = length

