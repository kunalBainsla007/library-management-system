from models import Book


def add_book(books, book_id, title, author, category, year):
    for book in books:
        if book.book_id == book_id:
            print("Book ID already exists.")
            return

    books.append(Book(book_id, title, author, category, year))
    print("Book added successfully!")


def remove_book(books, book_id):
    for book in books:
        if book.book_id == book_id:
            books.remove(book)
            print("Book removed successfully")
            return

    print("Book not found")


def display_books(books):
    if not books:
        print("No books in library")
        return

    for book in books:
        print(f"\nBook ID = {book.book_id}")
        print(f"Book Title = {book.title}")
        print(f"Book Author = {book.author}")
        print(f"Book Category = {book.category}")
        print(f"Year = {book.year}")

        if book.available:
            print("Available")
        else:
            print("Not Available")

        print("_" * 45)