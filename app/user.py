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
        normelized_title = title.strip().lower()
        for book in self.borrowed_books:
            if book.title.strip().lower() == normelized_title:
                return book
        return None


class Student(User):
    def __init__(self, name: str):
        super().__init__(name)
