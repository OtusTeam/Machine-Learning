class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.role = "REGULAR_USER"
        self.logged_in = False

    def __repr__(self):
        return f"{self.__class__.__name__}: username = {self.username}"

    def is_logged_in(self):
        return self.logged_in

    def login(self):
        if self.username not in User.get_usernames():
            raise UserNotFoundException(f"Username or password is not correct.")
        for user in User.get_users_list():
            if self.username == user.username and self.password != user.password:
                raise UserNotFoundException("Username or password is not correct")
        self.logged_in = True
        print(f"Hi, {self.username}! You are logged in.")

    def logout(self):
        if self.logged_in:
            self.logged_in = False
            print(f"Bye, {self.username}! You are logged out.")
        else:
            raise UnauthorizedException("You are not logged in.")

    @classmethod
    def get_usernames(cls):
        return ["regular_user", "test_user"]

    @classmethod
    def get_users_list(cls):
        regular_user = User("regular_user", "1234")
        test_user = User("test_user", "5678")
        return [regular_user, test_user]


class UserNotFoundException(BaseException):
    pass


class UnauthorizedException(BaseException):
    pass


if __name__ == "__main__":
    user = User("regular_user", "1234")
    print(user.logged_in is False)
