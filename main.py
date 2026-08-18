from models import Admin
from auth import register_user, login_user, create_admin
from book_operations import add_book, remove_book, display_books
from search import search_book
from borrow_return import borrow_book, return_book
from storage import load_books, save_books, load_users, save_users


def admin_menu(user, books):
    while True:
        user.show_menu()

        try:
            choice = int(input("Enter choice: "))

            if choice == 1:
                book_id = int(input("Enter Book ID: "))
                title = input("Enter Book Title: ")
                author = input("Enter Author Name: ")
                category = input("Enter Category: ")
                year = int(input("Enter Year: "))

                add_book(
                    books,
                    book_id,
                    title,
                    author,
                    category,
                    year
                )

            elif choice == 2:
                book_id = int(input("Enter Book ID to remove: "))
                remove_book(books, book_id)

            elif choice == 3:
                display_books(books)

            elif choice == 4:
                search_book(books)

            elif choice == 5:
                print("Logged out")
                break

            else:
                print("Invalid choice")

        except ValueError:
            print("Please enter valid input")


def user_menu(user, books):
    while True:
        user.show_menu()

        try:
            choice = int(input("Enter choice: "))

            if choice == 1:
                display_books(books)

            elif choice == 2:
                search_book(books)

            elif choice == 3:
                book_id = int(input("Enter Book ID: "))
                borrow_book(books, user.username, book_id)

            elif choice == 4:
                book_id = int(input("Enter Book ID: "))
                return_book(books, user.username, book_id)

            elif choice == 5:
                print("Logged out")
                break

            else:
                print("Invalid choice")

        except ValueError:
            print("Please enter valid input")


def main():
    books = load_books()
    users = load_users()

    
    create_admin(users)

    while True:
        print("\n===== Library Management System =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        try:
            choice = int(input("Enter choice: "))

            if choice == 1:
                username = input("Enter Username: ")
                password = input("Enter Password: ")

                register_user(users, username, password)
                save_users(users)

            elif choice == 2:
                username = input("Enter Username: ")
                password = input("Enter Password: ")

                user = login_user(users, username, password)

                if user is not None:
                    if isinstance(user, Admin):
                        admin_menu(user, books)
                    else:
                        user_menu(user, books)

            elif choice == 3:
                save_books(books)
                save_users(users)
                print("Thank you for using Library Management System.")
                break

            else:
                print("Invalid choice")

        except ValueError:
            print("Please enter a valid choice")


if __name__ == "__main__":
    main()