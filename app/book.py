class Book:

    def __init__(self, title: str, author: str, category: str):
        self.title: str = title
        self.author: str = author
        self.category: str = category
        self.is_available: bool = True

    def __str__(self):
        return f"{self.title} by {self.author}, category={self.category}"
