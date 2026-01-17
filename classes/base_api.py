import os
import requests

from dotenv import load_dotenv

load_dotenv()


class BaseAPI:
    def __init__(self, headers=None):
        self.base_url = "https://favqs.com/api"
        self.headers = headers or {
            "Authorization": f"Token token={os.getenv('FAVQS_TOKEN')}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def post(self, endpoint: str, json=None, headers=None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = requests.post(url, json=json, headers={**self.headers, **(headers or {})})
        return response

    def get(self, endpoint: str, params=None, headers=None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = requests.get(url, params=params, headers={**self.headers, **(headers or {})})
        return response

    def put(self, endpoint: str, json=None, headers=None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = requests.put(url, json=json, headers={**self.headers, **(headers or {})})
        return response
