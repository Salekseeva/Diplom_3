# utils/api_client.py
import requests
from test_data import AUTH_URL, HEADERS


class APIClient:
    @staticmethod
    def create_user(email: str, password: str, name: str) -> dict:
        """
        Создание пользователя через API.
        Возвращает результат запроса (JSON).
        """
        url = f"{AUTH_URL}/register"
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        response = requests.post(url, json=payload, headers=HEADERS)
        return response.json()

    @staticmethod
    def delete_user(token: str) -> dict:
        """
        Удаление пользователя через API.
        Необходимо передавать токен авторизации.
        """
        url = f"{AUTH_URL}/user"
        headers = {
            **HEADERS,
            "Authorization": f"Bearer {token}"
        }
        response = requests.delete(url, headers=headers)
        return response.json()

    @staticmethod
    def login_user(email: str, password: str) -> dict:
        """
        Логин пользователя для получения токенов.
        """
        url = f"{AUTH_URL}/login"
        payload = {
            "email": email,
            "password": password
        }
        response = requests.post(url, json=payload, headers=HEADERS)
        return response.json()
