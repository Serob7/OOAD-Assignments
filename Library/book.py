from abc import ABC, abstractmethod
from validators import not_empty_string

class Book(ABC):
    @abstractmethod
    def __init__(self, title, author, publication_date):
        ...

class Fiction(Book):
    @not_empty_string('Title', 1)
    @not_empty_string('Author', 2)
    @not_empty_string('Publication date', 3)
    def __init__(self, title, author, publication_date):
        self.title = title
        self.author = author
        self.publication_date = publication_date


class Non_Fiction(Book):
    @not_empty_string('Title', 1)
    @not_empty_string('Author', 2)
    @not_empty_string('Publication date', 3)
    def __init__(self, title, author, publication_date):
        self.title = title
        self.author = author
        self.publication_date = publication_date


