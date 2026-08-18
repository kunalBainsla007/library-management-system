from models import User, Admin


def register_user(users, username, password):
    if username == "":
        print("Invalid username")
        return False

    if len(password) < 6:
        print("Password must be at least 6 characters")
        return False

    for user in users:
        if user.username == username:
            print("User already registered")
            return False

    users.append(User(username, password))
    print("You registered successfully")
    return True


def login_user(users, username, password):
    for user in users:
        if user.username == username:
            if user.check_password(password):
                print("Login successful")
                return user
            else:
                print("Wrong password")
                return None

    print("User does not exist")
    return None


def create_admin(users):
    for user in users:
        if user.username == "admin":
            return

    users.append(Admin("admin", "admin123"))