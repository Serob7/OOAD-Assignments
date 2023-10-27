from book import Fiction, Non_Fiction
from borrower import Borrower
from librarian import Librarian

def main():
    #create Book, Borrower and Librarian instances
    fiction_book = Fiction('Sherlock Holmes', 'Arthur Conan Doyle', '10.05.1976')
    non_fiction_book = Non_Fiction('Count Monte Christo', 'Alexander Dyuma', '30.09.1970')
    borrower = Borrower('Serob', 'serob@gmail.com')
    librarian = Librarian('Tom', 'tom@gmail.com')

    #borrow, return and view history
    borrower.borrow_book(fiction_book, librarian)
    borrower.borrow_book(non_fiction_book, librarian)
    print('\n')
    borrower.return_book(fiction_book, librarian)
    borrower.return_book(non_fiction_book, librarian)
    print('\n')
    borrower.view_borrowing_history()


if __name__ == '__main__':
    main()