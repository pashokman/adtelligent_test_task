import os
from utils.generators.login_generator import login_generator


def test_create_user(user):
    response = user.create_user()

    assert response.status_code == 200
    response_json = response.json()

    assert "login" in response_json
    assert "User-Token" in response_json
    assert os.getenv("FAVQS_TOKEN"), "Token is not set"


def test_get_user(user):
    user.create_user()
    response = user.get_user()
    response_json = response.json()

    assert response_json["login"] == user.login
    assert response_json["account_details"]["email"] == user.user_obj["user"]["email"]


def test_update_user(user):
    user.create_user()

    new_login = login_generator()
    new_email = f"{new_login}@example.com"
    user.update_user(login=new_login, email=new_email)

    get_response = user.get_user()
    get_response_json = get_response.json()

    assert get_response_json["login"] == new_login
    assert get_response_json["account_details"]["email"] == new_email
