LIBRARY MANAGEMENT SYSTEM


A simple Python based Library Management System.

FEATURES

- User registration and login
- Admin login
- Add and remove books
- Display books
- Search books by:
  - Book ID
  - Category
  - Author
  - Year
- Borrow books
- Return books
- Fine calculation
- Save and load books and users using text files


PROJECT FILES

main.py
    Main program and menu handling.

models.py
    Contains Book, Person, User and Admin classes.

auth.py
    Handles user registration and login.

book_operations.py
    Handles adding, removing and displaying books.

search.py
    Handles book searching.

borrow_return.py
    Handles borrowing, returning and fine calculation.

storage.py
    Handles saving and loading data from text files.


OOP CONCEPTS USED

- Classes and Objects
- Inheritance
- Polymorphism
- Method Overriding
- Encapsulation
- Constructor (__init__)
- super()
- Private attribute (__password)


DEFAULT ADMIN

Username: admin
Password: admin123


HOW TO RUN

Run the following command:

python main.py