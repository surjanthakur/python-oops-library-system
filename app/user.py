from book import Book
import uuid


class User:
    def __init__(self, name: str):
        self.user_id = str(uuid.uuid4())
        self.name = name
        self.__borrowed_books: list[Book] = []
        self.__registered_books: list[Book] = []

    def show_my_books(self):
        if self.__borrowed_books:
            return self.__borrowed_books
        else:
            return f"oops! {self.name} you shelf is empty📚"

    def update_registered_book(self, book: Book):
        self.__registered_books.append(book)

    def add_borrowed_book(self, book: Book):
        self.__borrowed_books.append(book)

    def remove_borrowed_book(self, book: Book):
        self.__borrowed_books.remove(book)

    def borrowed_books_count(self):
        return len(self.__borrowed_books)

    def give_borrowed_book(self, title: str):
        for book in self.__borrowed_books:
            if book.title.strip().lower() == title.strip().lower():
                return book


class Student(User):
    def __init__(self, name: str):
        super().__init__(name)
