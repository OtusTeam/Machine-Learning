from users import User


def get_user_menu():
    choice = input("If you want to logout, enter 1: ")
    if choice == "1":
        user.logout()

    else:
        get_user_menu()


username = input("Enter your username:")
password = input("Enter your password:")

user = User(username, password)
user.login()
get_user_menu()
