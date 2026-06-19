import secrets
import string

RANDOM_ID = " ".join(
    secrets.choice(string.ascii_uppercase + string.digits) for _ in range(4)
)


class Book:
    def __init__(self):
        self.__book_id = RANDOM_ID
        self.__title: str
        self.__author: str
        self.__category: str
        self.__is_available: bool


class Library:
    def __init__(self):
        self.__library_books: list[object] = []
        self.__borrowed_book_users: list[object] = []
        self.__all_transactions: list[object] = []

    def register_new_book(self, new_book: Book, person: User):
        pass

    def rent_new_book(self, book_id: str, book_title: str, person: User):
        pass

    def return_book(self, book: Book, person: User):
        pass

    def show_available_books(self):
        pass

    def search_for_book(self, book_title: str):
        pass


class User:
    def __init__(self, name: str):
        self.__name = name
        self.__borrowed_books = []

    def show_my_books(self):
        if self.__borrowed_books:
            return self.__borrowed_books
        else:
            return f"oops! {self.__name} you shelf is empty📚"


class Student(User):
    def __init__(self, name: str):
        super().__init__(name)


class Teacher(User):
    def __init__(self, name: str):
        super().__init__(name)
