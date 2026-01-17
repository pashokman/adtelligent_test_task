import pytest

from classes.user import User


@pytest.fixture(scope="function")
def user():
    user = User()
    yield user
