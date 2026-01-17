from utils.generators.login_generator import login_generator
from utils.generators.password_generator import generate_password


def generate_user(password_length: int):
    login = login_generator()
    password = generate_password(password_length=password_length)

    result_user = {"user": {"login": login, "email": f"{login}@example.com", "password": password}}

    return result_user
