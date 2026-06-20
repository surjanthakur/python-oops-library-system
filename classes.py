import secrets
import string

RANDOM_ID = " ".join(
    secrets.choice(string.ascii_uppercase + string.digits) for _ in range(4)
)


class Book:
    """
    this class let's you create the Book object with some fields:
    title:str , author:str , category:str
    """

    def __init__(self, title: str, author: str, category: str):
        self.__book_id = RANDOM_ID
        self.title: str = title
        self.author: str = author
        self.category: str = category
        self.__is_available: bool = True

    def __str__(self):
        return f"{self.title} by {self.author}, category={self.category}, book_id={self.__book_id}"


class User:
    def __init__(self, name: str):
        self.name = name
        self.__borrowed_books = []
        self.__registered_books = []

    def show_my_books(self):
        if self.__borrowed_books:
            return self.__borrowed_books
        else:
            return f"oops! {self.name} you shelf is empty📚"

    def update_register_book(self, book: Book):
        self.__registered_books.append(book)


class Student(User):
    def __init__(self, name: str):
        super().__init__(name)


class Teacher(User):
    def __init__(self, name: str):
        super().__init__(name)


class Library:
    def __init__(self):
        self.__library_books: list[object] = []
        self.__borrowed_book_users: list[object] = []
        self.__registered_book_users: list[object] = []
        self.__all_transactions: list[object] = []

    def register_new_book(self, new_book: Book, person: User):
        self.__library_books.append(new_book)
        person.update_register_book(new_book)
        self.__registered_book_users.append(person)
        return f"thanks {person.name} to charity {new_book.title} book 📚"

    def borrow_new_book(self, book_id: str, book_title: str, person: User):
        pass

    def return_book(self, book: Book, person: User):
        pass

    def show_available_books(self):
        """gives you the list of Book object's"""
        if self.__library_books:
            return self.__library_books
        else:
            return "the library books shelf is empty"

    def search_for_book(self, book_title: str):
        for book in self.__library_books:
            if book.title.strip().lower() == book_title.strip().lower():
                return Book(book.title, book.author, book.category)
            else:
                return "oops! can't find the matching book"


obj = Library()
std1 = Student("james")
b1 = Book("Atomic Habits", "James Clear", "Self Help")
b2 = Book("The Alchemist", "Paulo Coelho", "Fiction")
b3 = Book("Sapiens", "Yuval Noah Harari", "Non-Fiction")
b4 = Book("The Psychology of Money", "Morgan Housel", "Finance")
b5 = Book("Dune", "Frank Herbert", "Science Fiction")
b6 = Book("Pride and Prejudice", "Jane Austen", "Classic")
b7 = Book("The Hobbit", "J.R.R. Tolkien", "Fantasy")
b8 = Book("Becoming", "Michelle Obama", "Memoir")
b9 = Book("Thinking, Fast and Slow", "Daniel Kahneman", "Psychology")
b10 = Book("The Catcher in the Rye", "J.D. Salinger", "Fiction")

obj.register_new_book(b1, std1)
obj.register_new_book(b2, std1)
obj.register_new_book(b3, std1)
obj.register_new_book(b4, std1)
obj.register_new_book(b5, std1)
obj.register_new_book(b6, std1)
obj.register_new_book(b7, std1)
obj.register_new_book(b8, std1)
obj.register_new_book(b9, std1)
obj.register_new_book(b10, std1)
