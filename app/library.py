from datetime import datetime

from book import Book
from transaction import Transaction
from user import User


class Library:
    def __init__(self):
        self.__library_books: list[object] = []
        self.__borrowed_book_users: list[object] = []
        self.__registered_book_users: list[object] = []

    # add new book in library method
    def register_new_book(self, new_book: Book, person: User):
        "this method let's you register new book in library."
        self.__library_books.append(new_book)
        person.update_registered_book(new_book)
        self.__registered_book_users.append(person)
        return f"thanks {person.name} to charity {new_book.title} book 📚"

    # borrow new book from library method
    def borrow_new_book(self, book_title: str, person: User):
        """this method let's you borrow a book from library and return a msg."""

        if person.borrowed_books_count() >= 4:
            return "maximum borrow capacity reached return some books first!"
        else:
            for book in self.__library_books:
                if book.title.strip().lower() == book_title.strip().lower():
                    borrowed_book = Book(book.title, book.author, book.category)
                    borrowed_book.issue_date = datetime.now().strftime("%d")
                    borrowed_book.change_available()
                    person.add_borrowed_book(borrowed_book)
                    self.__borrowed_book_users.append(person)
                    self.__library_books.remove(book)
                    return f"hy {person.name} you borrowed {borrowed_book.title} book on {borrowed_book.issue_date} you have 7 days to return otherwise there will be extra charges😎"

                else:
                    return "oops! can't find the matching book"

    # return borrowed book method
    def return_book(self, book: Book, person: User):
        if book.check_book_status() == True:
            return "wrong book to_return😡"
        else:
            for user in self.__borrowed_book_users:
                if user.name.strip().lower() == person.name.strip().lower():
                    book.change_available()
                    self.__library_books.append(book)
                    person.remove_borrowed_book(book)
                    get_receipt = Transaction(
                        book=book,
                        person=person,
                        issued_date=book.issue_date,
                    )
                    print(get_receipt.print_my_receipt())
                else:
                    return "wrong owner req to return_book 📕"

    # show all available books method
    def show_available_books(self):
        """this method gives you the list of Book object's"""
        if self.__library_books:
            return self.__library_books
        else:
            return "the library books shelf is empty"

    # search book by its title method
    def search_for_book(self, book_title: str):
        "this methods let's you search the book by their title."
        for book in self.__library_books:
            if book.title.strip().lower() == book_title.strip().lower():
                return Book(book.title, book.author, book.category)
            else:
                return "oops! can't find the matching book"
