from library import Library
from book import Book
from user import User


def message_display():
    return int(input("""
                      👉🏻enter 2 to register book
                     👉🏻enter 3 to show all library books
                     👉🏻enter 4 to borrow a book from libarary:  
                     👉🏻enter 5 to return a book.
                     👉🏻enter 108 to exit ❌
                     """))


def main():
    main_library = Library()

    # creating user
    name = input("👉🏻Enter Your Name: ")
    new_user = User(name)

    print("now we are creating book")
    # creating book
    title = input("enter book title: ")
    author = input("enter book author: ")
    category = input("enter book category: ")
    new_book = Book(title, author, category)

    while True:
        user_choice = message_display()

        if user_choice == 108:
            print("thanks for using our services.")
            break

        if user_choice == 2:
            msg = main_library.register_new_book(new_book, new_user)
            print(msg)
            user_choice = message_display()

        if user_choice == 3:
            [print(book) for book in main_library.show_available_books()]

        if user_choice == 4:
            title = input("enter book title: ")
            msg = main_library.borrow_new_book(title, new_user)
            print(msg)

        if user_choice == 5:
            title = input("enter book title: ")
            borrowed_book = new_user.give_borrowed_book(title)
            if borrowed_book:
                msg = main_library.return_new_book(borrowed_book, new_user)
                print(msg)
            else:
                print("can't find the matching book.")


main()
