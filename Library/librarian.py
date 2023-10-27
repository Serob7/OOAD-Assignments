from abc import ABC, abstractmethod
from validators import not_empty_string, email_checker

class LibraryOperations(ABC):
    @not_empty_string('Name', 1)
    @email_checker('Contact information', 2)
    def __init__(self, name, contact_information):
        self.name = name
        self.contact_information = contact_information
        self.borrowed = []

    @abstractmethod
    def borrow_book(self, borrower, book):
        ...

    @abstractmethod
    def return_book(self, borrower, book):
        ...




class Librarian(LibraryOperations):
    def borrow_book(self, borrower, book):
        print(f"{borrower.name} borrowed {book.title} by {book.author}")
        self.borrowed.append(book)
        return f"Borrowed {book.title} by {book.author}"
    def return_book(self, borrower, book):
        if book in self.borrowed:
            print(f"{borrower.name} returned {book.title} by {book.author}")
            self.borrowed.remove(book)
            return f"Returned {book.title} by {book.author}"
        else:
            print('You have never borrowed that book')
