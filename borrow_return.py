def borrow_book(books, username, book_id):
    for book in books:
        if book.book_id == book_id:

            if book.available:
                book.available = False
                print(f"Book borrowed successfully by {username}")
            else:
                print("Book not available")

            return

    print("Book not found")


def calculate_fine(days):
    if days <= 7:
        return 0

    return (days - 7) * 10


def return_book(books, username, book_id):
    for book in books:
        if book.book_id == book_id:

            if not book.available:
                try:
                    days = int(input("Enter number of days: "))
                except ValueError:
                    print("Please enter a valid number")
                    return

                fine = calculate_fine(days)
                print("Fine:", fine)

                book.available = True
                print(f"Book returned successfully by {username}")

            else:
                print("Book is already available")

            return

    print("Book not found")