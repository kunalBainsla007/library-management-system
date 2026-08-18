from models import Book, User, Admin


def save_books(books):
    with open("book.txt", "w") as file:
        for book in books:
            file.write(
                f"{book.book_id},{book.title},{book.author},"
                f"{book.category},{book.year},{book.available}\n"
            )


def load_books():
    books = []

    try:
        with open("book.txt", "r") as file:
            for line in file:
                part = line.strip().split(",")

                if len(part) < 6:
                    continue

                book = Book(
                    int(part[0]),
                    part[1],
                    part[2],
                    part[3],
                    int(part[4])
                )

                book.available = part[5] == "True"
                books.append(book)

    except FileNotFoundError:
        pass

    return books


def save_users(users):
    with open("user.txt", "w") as file:
        for user in users:
            file.write(f"{user.username},{user.get_password()}\n")


def load_users():
    users = []

    try:
        with open("user.txt", "r") as file:
            for line in file:
                part = line.strip().split(",")

                if len(part) >= 2:
                    username = part[0]
                    password = part[1]

                    if username == "admin":
                        users.append(Admin(username, password))
                    else:
                        users.append(User(username, password))

    except FileNotFoundError:
        pass

    return users