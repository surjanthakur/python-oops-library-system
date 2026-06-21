# Python OOP Library System

A small object-oriented library management example in Python demonstrating
basic classes and interactions for books, users, borrowing, and transactions.

This repository is intended as a learning project to showcase OOP design in
Python and a simple interactive CLI for registering, borrowing and returning
books.

**Quick Start**

- Requirements: Python 3.8+
- From the repository root run:

```bash
python3 app/main.py
```

The program is interactive and will prompt for a user name and a book to
create; then you can register it into the library, borrow, list available
books, or return borrowed books.

**Commands (interactive menu)**

- `2` — Register a book to the library (donate/register)
- `3` — Show all available library books
- `4` — Borrow a book from the library
- `5` — Return a borrowed book
- `108` — Exit the program

Usage is via the simple menu shown when running `app/main.py`.

**Project Structure**

- `app/book.py` — `Book` class: represents a single book, contains title,
  author, category, unique id and availability state.
- `app/user.py` — `User` and `Student` classes: track user name,
  registered books and borrowed books; provides methods for managing
  borrowed/registered lists.
- `app/library.py` — `Library` class: central logic for registering
  books, borrowing, returning, searching and listing available books. It
  interacts with `User` and `Transaction` objects.
- `app/transaction.py` — `Transaction` class: simple receipt generator used
  when a borrowed book is returned; computes days and fine (if overdue).
- `app/main.py` — Interactive CLI: creates a `Library` and a `Student` user
  and drives the menu loop.

**Examples**

1. Register a book: run the script, provide name and a book; press `2` to
   register the book into the library.

2. Show available books: press `3` to print all books currently in the
   library shelves.

3. Borrow a book: press `4` and type the book title to borrow (max 4
   borrowed books per user). Borrowed books are removed from the available
   shelf and added to the user's borrowed list.

4. Return a book: press `5`, type the title — if matched, the program
   prints a receipt with issued/return dates and any fine.

**Notes & Known Limitations**

- The project is an educational example and not production-ready.
- Some search/loop logic in `app/library.py` uses early `return` inside loops
  which may prevent searching beyond the first element. Consider reviewing
  `borrow_new_book` and `search_for_book` for improved search behavior.
- `app/main.py` calls `main()` at import time; if you wish to import these
  modules elsewhere, run `app/main.py` directly rather than importing it.

**Development**

- Style: keep simple, readable OOP code.
- Tests: none included. Add unit tests under a `tests/` folder to verify
  library and transaction logic.

If you'd like, I can:

- Convert this CLI into a proper command-line tool (Argparse/Click).
- Fix the search/loop logic and add unit tests and example data.

---

If you want any changes to this README (more examples, API reference,
or a usage screencast), tell me which parts to expand and I'll update it.
