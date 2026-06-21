from datetime import datetime

from book import Book
from user import User


class Transaction:
    def __init__(self, book: Book, person: User, issued_date: int):
        self.book = book
        self.person = person
        self.issued_date = int(issued_date)
        self.return_date = int(datetime.now().strftime("%d"))

    def print_my_receipt(self):
        extra_days = (self.return_date - self.issued_date) + 1
        total_fine = 0
        if extra_days >= 6:
            total_fine += extra_days * 10

        return f"""
        book name : {self.book.title}
        person who borrowed : {self.person.name}
        book issued date: {self.issued_date}
        book return date: {self.return_date}
        total days : {extra_days}
        total fine : {total_fine}rs
        """
