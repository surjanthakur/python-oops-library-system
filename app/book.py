import uuid


class Book:

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

    def check_book_status(self):
        return self.__is_available

    def __str__(self):
        return f"{self.title} by {self.author}, category={self.category}, book_id={self.__book_id}"
