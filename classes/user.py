from classes.base_api import BaseAPI
from utils.generators.user_generator import generate_user


class User(BaseAPI):

    def __init__(self, headers=None):
        super().__init__(headers=headers)
        self.user_obj = None
        self.user_token = None
        self.login = None
        self.email = None

    def create_user(self):
        if self.user_obj is None:
            self.user_obj = generate_user(password_length=8)
        response = self.post(endpoint="users", json=self.user_obj)
        if response.status_code == 200:
            data = response.json()
            self.login = data["login"]
            self.user_token = data["User-Token"]
        return response

    def get_user(self):
        headers = {"User-Token": self.user_token}
        response = self.get(endpoint=f"users/{self.login}", headers=headers)
        return response

    def update_user(self, login=None, email=None):
        headers = {"User-Token": self.user_token}

        body = {"user": {}}
        if login:
            body["user"]["login"] = login
        if email:
            body["user"]["email"] = email

        response = self.put(endpoint=f"users/{self.login}", headers=headers, json=body)
        if response.status_code == 200 and login:
            self.login = login
        if response.status_code == 200 and email:
            self.email = email
        return response
