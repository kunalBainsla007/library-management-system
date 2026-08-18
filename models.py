class Person:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def check_password(self, password):
        return self.__password == password

    def get_password(self):
        return self.__password


class User(Person):
    def __init__(self, username, password):
        super().__init__(username, password)

    def show_menu(self):
        print("\n===== User Menu =====")
        print("1. Display Books")
        print("2. Search Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Logout")


class Admin(Person):
    def __init__(self, username, password):
        super().__init__(username, password)

    def show_menu(self):
        print("\n===== Admin Menu =====")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Display Books")
        print("4. Search Book")
        print("5. Logout")


class Book:
    def __init__(self, book_id, title, author, category, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.year = year
        self.available = True