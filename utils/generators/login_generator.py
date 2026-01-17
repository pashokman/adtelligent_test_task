from faker import Faker

fake = Faker()


def login_generator():
    return f"{fake.user_name()}"
