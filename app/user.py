from book import Book
from uuid import uuid4


class User:
    def __init__(self, name: str):
        self.user_id = str(uuid4())
        self.name = name
        self.borrowed_books: list[Book] = []
        self.registered_books: list[Book] = []

    def show_my_books(self):
        return self.borrowed_books

    def give_borrowed_book(self, title: str):
        normalized_title = title.strip().lower()
        for book in self.borrowed_books:
            if book.title.strip().lower() == normalized_title:
                return book
        return None
