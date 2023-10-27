from validators import not_empty_string, email_checker

class Borrower:
    @not_empty_string('Name', 1)
    @email_checker('Contact information', 2)
    def __init__(self, name, contact_information):
        self.name = name
        self.contact_information = contact_information
        self.borrowing_history = []


    def borrow_book(self, book, librarian):
        history = librarian.borrow_book(self, book)
        self.borrowing_history.append(history)
    def return_book(self, book, librarian):
        history = librarian.return_book(self, book)
        self.borrowing_history.append(history)

    def view_borrowing_history(self):
        print('\tBorrowing history')
        for history in self.borrowing_history:
            print(history)




