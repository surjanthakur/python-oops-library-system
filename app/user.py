from book import Book


class User:
    def __init__(self, name: str):
        self.name = name
        self.borrowed_books: list[Book] = []
        self.registered_books: list[Book] = []

    def show_my_books(self) -> Book:
        for book in self.borrowed_books:
            return book

    def give_borrowed_book(self, title: str):
        for book in self.borrowed_books:
            if book.title.strip().lower() == title.strip().lower():
                return book


class Student(User):
    def __init__(self, name: str):
        super().__init__(name)
