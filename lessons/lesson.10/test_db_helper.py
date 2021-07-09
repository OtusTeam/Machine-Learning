import random
from unittest import mock

from pytest import fixture

from db_helper import (
    User,
    Engine,
    Connection,
    get_engine,
    get_connection,
    get_user,
)


@fixture
def user():
    user = User(str(random.randbytes(10)))
    print("created user", user)
    # return user
    yield user
    print("deleting user..", user)
    user.delete()


@fixture(scope="module")
def engine_default():
    return get_engine()


@fixture(scope="module")
def conn_default(engine_default):
    return get_connection(engine_default)


class TestUser:

    def test_init(self):
        username = str(random.randbytes(10))
        u = User(username)
        print("created user", u)
        assert u.username == username

    def test_delete(self, user):
        assert user.delete() is True

    def test_update_username(self, user):
        old_username = user.username
        user.username += "qwe"
        assert user.username != old_username


def test_connection(conn_default):
    assert isinstance(conn_default, Connection)
    assert isinstance(conn_default.engine, Engine)


def test_demo_multiple_fixtures(conn_default, engine_default):
    assert conn_default.engine is engine_default


@mock.patch("db_helper.get_connection", autospec=True)
def test_get_user(mocked_get_connection, user):
    username = user.username
    mocker_conn = mocked_get_connection.return_value
    mocked_conn_get_user = mocker_conn.get_user
    mocked_conn_get_user.return_value = user

    res = get_user(username)
    assert res is user

    # mocked_conn_get_user.assert_called()
    # mocked_conn_get_user.assert_called_once()
    mocked_get_connection.assert_called_once_with()
    mocked_conn_get_user.assert_called_once_with(username)
