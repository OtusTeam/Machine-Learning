from unittest import TestCase

from _pytest.fixtures import fixture
from _pytest.python_api import raises

from users import User, UserNotFoundException, UnauthorizedException


class UserTestCase(TestCase):

    def setUp(self) -> None:
        regular_user = User("regular_user", "1234")
        invalid_username_user = User("invalid_user", "1234")
        invalid_password_user = User("regular_user", "1235")
        self.regular_user = regular_user
        self.invalid_user_user = invalid_username_user
        self.invalid_password_user = invalid_password_user

    # def tearDown(self) -> None:

    def test_login_success(self):
        self.regular_user.login()
        self.assertEqual(self.regular_user.logged_in, True)

    def test_login_access(self):
        self.assertEqual(self.regular_user.logged_in, False)


@fixture
def regular_user():
    user = User("regular_user", "1234")
    # print("user is created")
    return user


class TestUser:

    def test_login_success(self, regular_user):
        regular_user.login()
        assert regular_user.logged_in == True

    def test_login_access(self, regular_user):
        assert regular_user.logged_in == False

    def test_login_error(self, regular_user):
        regular_user.password = "4567"
        # assert regular_user.logged_in == True
        with raises(UserNotFoundException) as ex:
            regular_user.login()
        assert str(ex.value) == "Username or password is not correct"

    # def logout(self):
    #     if self.logged_in:
    #         self.logged_in = False
    #         print(f"Bye, {self.username}! You are logged out.")
    #     else:
    #         print("You are not logged in.")

    def test_logout_invalid(self, regular_user):
        with raises(UnauthorizedException) as ex:
            regular_user.logout()
        assert str(ex.value) == "You are not logged in."

    def test_logout_success(self, regular_user):
        regular_user.login()
        regular_user.logout()
        assert regular_user.logged_in is False


def get_users_list():
    regular_user = User("regular_user", "1234")
    test_user = User("test_user", "5678")
    return [regular_user, test_user]


def test_get_users_list():
    assert len(get_users_list()) == 2


def test_get_usernames():
    assert User.get_usernames() == ["regular_user", "test_user"]
