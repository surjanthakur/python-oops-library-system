import uuid
from datetime import datetime


class Book:
    """
    this class let's you create the Book object with some fields:
    title:str , author:str , category:str
    """

    def __init__(self, title: str, author: str, category: str):
        self.__book_id = str(uuid.uuid4())
        self.title: str = title
        self.author: str = author
        self.category: str = category
        self.__is_available: bool = True

    def change_available(self):
        if self.__is_available == True:
            self.__is_available = False
        else:
            self.__is_available = True

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

    def update_registered_book(self, book: Book):
        self.__registered_books.append(book)

    def update_borrowed_book(self, book: Book):
        self.__borrowed_books.append(book)

    def borrowed_books_count(self):
        return len(self.__borrowed_books)


class Student(User):
    def __init__(self, name: str):
        super().__init__(name)


class Teacher(User):
    def __init__(self, name: str):
        super().__init__(name)


class Transaction:
    def __init__(self):
        pass


class Library:
    def __init__(self):
        self.__library_books: list[object] = []
        self.__borrowed_book_users: list[object] = []
        self.__registered_book_users: list[object] = []
        self.__all_transactions: list[object] = []

    def register_new_book(self, new_book: Book, person: User):
        self.__library_books.append(new_book)
        person.update_registered_book(new_book)
        self.__registered_book_users.append(person)
        return f"thanks {person.name} to charity {new_book.title} book 📚"

    def borrow_new_book(self, book_title: str, person: User):
        if person.borrowed_books_count() >= 4:
            print("maximum borrow capacity reached return some books first!")
            return
        else:
            for book in self.__library_books:
                if book.title.strip().lower() == book_title.strip().lower():
                    borrowed_book = Book(book.title, book.author, book.category)
                    borrowed_book.issue_date = datetime.now().strftime("%d")
                    borrowed_book.change_available()
                    person.update_borrowed_book(borrowed_book)
                    self.__borrowed_book_users.append(person)
                    self.__library_books.remove(book)
                    return f"hy {person.name} you borrowed {borrowed_book.title} book on {borrowed_book.issue_date} you have 7 days to return otherwise there will be extra charges😎"

                else:
                    return "oops! can't find the matching book"

    def return_book(self, book: Book, person: User):
        pass

    def show_available_books(self):
        """this method gives you the list of Book object's"""
        if self.__library_books:
            return self.__library_books
        else:
            return "the library books shelf is empty"

    def search_for_book(self, book_title: str):
        "this methods let's you search the book by their title."
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

print(obj.search_for_book("atomic habits"))
print(obj.borrow_new_book("atomic habits", std1))
