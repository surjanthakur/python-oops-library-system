from uuid import uuid4


class Book:
    def __init__(self):
        self.__book_id = str(uuid4())
        self.__title: str
        self.__author: str
        self.__category: str
        self.__is_available: bool


class Library:
    def __init__(self):
        self.library_books: list[object] = []
        self.borrowed_book_users: list[object] = []

    def add_book():
        pass

    def register_book():
        pass

    def issue_book():
        pass

    def accept_return():
        pass

    def show_available_books():
        pass


class User:
    def __init__(self, name: str):
        self.__user_id = str(uuid4())
        self.__name = name
        self.__borrowed_books = []

    def borrow_book():
        pass

    def return_book():
        pass

    def show_my_books(self):
        if self.__borrowed_books:
            return self.__borrowed_books
        else:
            return "oops! you shelf is empty📚"


class Student(User):
    def __init__(self, name: str):
        super().__init__(name)


class Teacher(User):
    def __init__(self, name: str):
        super().__init__(name)
