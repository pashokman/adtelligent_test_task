import random
import string


def generate_password(password_length: int):
    password = "".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=password_length))
    return password
