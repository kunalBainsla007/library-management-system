def show_book(book):
    print(
        book.book_id,
        book.title,
        book.author,
        book.category,
        book.year,
        book.available
    )
    print("-" * 40)


def search_by_id(books, book_id):
    for book in books:
        if book.book_id == book_id:
            show_book(book)
            return

    print("Book not found")


def search_by_category(books, category):
    found = False

    for book in books:
        if book.category.lower() == category.lower():
            show_book(book)
            found = True

    if not found:
        print("Book not found")


def search_by_author(books, author):
    found = False

    for book in books:
        if book.author.lower() == author.lower():
            show_book(book)
            found = True

    if not found:
        print("Book not found")


def search_by_year(books, year):
    found = False

    for book in books:
        if book.year == year:
            show_book(book)
            found = True

    if not found:
        print("Book not found")


def search_book(books):
    print("\n1. Search by ID")
    print("2. Search by Category")
    print("3. Search by Author")
    print("4. Search by Year")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            book_id = int(input("Enter Book ID: "))
            search_by_id(books, book_id)

        elif choice == 2:
            category = input("Enter Category: ")
            search_by_category(books, category)

        elif choice == 3:
            author = input("Enter Author: ")
            search_by_author(books, author)

        elif choice == 4:
            year = int(input("Enter Year: "))
            search_by_year(books, year)

        else:
            print("Invalid choice")

    except ValueError:
        print("Please enter valid input")