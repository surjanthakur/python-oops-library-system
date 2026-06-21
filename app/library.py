from datetime import datetime

from book import Book
from transaction import Transaction
from user import User


class Library:
    MAX_BORROW_LIMIT = 4

    def __init__(self):
        self.__library_books: list[Book] = []
        self.__borrowed_book_users: set[User] = set()
        self.__registered_book_users: set[User] = set()

    # add new book in library method
    def register_new_book(self, new_book: Book, user: User) -> str:
        self.__library_books.append(new_book)
        user.update_registered_book(new_book)
        self.__registered_book_users.add(user)

        return f"thanks {user.name} to donating {new_book.title}📚"

    # borrow new book from library method
    def borrow_new_book(self, book_title: str, person: User) -> str:

        if person.borrowed_books_count() >= self.MAX_BORROW_LIMIT:
            return "Borrow limit reached."

        normalized_title = book_title.strip().lower()
        for book in self.__library_books:

            if book.title.strip().lower() == normalized_title:
                book.issue_date = datetime.now().strftime("%d")

                book.change_available()

                person.add_borrowed_book(book)

                self.__borrowed_book_users.add(person)

                self.__library_books.remove(book)

                return f"hy {person.name} you borrowed {book.title} book on {book.issue_date} you have 7 days to return otherwise there will be extra charges😎"

        return None

    # return borrowed book method
    def return_new_book(self, book: Book, person: User):
        if book.check_book_status():
            return "wrong book"

        book.change_available()

        self.__library_books.append(book)

        person.remove_borrowed_book(book)

        if person.borrowed_books_count() == 0:
            self.__borrowed_book_users.discard(person)

        get_receipt = Transaction(
            book=book,
            person=person,
            issued_date=book.issue_date,
        )
        return get_receipt.print_my_receipt()

    #  return searched book
    def search_for_book(self, title: str) -> Book:
        normalized_title = title.strip().lower()

        for book in self.__library_books:
            if book.title.strip().lower() == normalized_title:
                return book
        return None

    # return all available books
    def show_available_books(self) -> list[Book]:
        return self.__library_books.copy()
