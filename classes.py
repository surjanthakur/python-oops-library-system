class Library:
    def __init__(self):
        self.library_books: list = []
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


class Book:
    def __init__(self):
        self.__book_id: str
        self.title: str
        self.author: str
        self.category: str
        self.__is_available: bool

    def borrow():
        pass

    def return_book():
        pass

    def get_status():
        pass


class User:
    def __init__(self):
        self.user_id: str
        self.name: str
        self.borrowed_books = []

    def borrow_book():
        pass

    def return_book():
        pass


class Transaction:
    def __init__(self):
        self.book: str
        self.user: str
        self.issue_date: str
        self.return_date: str
        self.fine_calculate: str

    def print_receipt():
        pass
