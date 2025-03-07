from conftest import *
from data import DataUser
import allure
import requests

class TestLoginUsers:
    @allure.title('Проверка успешной авторизации существующего пользователя')
    def test_auth_existing_user_success(self):
        payload = {
            'email': DataUser.email,
            'password': DataUser.password
        }
        response = requests.post(Url.url_user_login, data=payload)
        assert response.status_code == 200
        assert response.json()['success'] is True
        assert 'accessToken' in response.json().keys()
        assert response.json()['user']['email'] == payload['email']

    @allure.title('Проверка авторизации с неверным логином')
    def test_auth_invalid_user_success(self):
        payload = {
            'email': DataUser.random_email,
            'password': DataUser.password
        }
        response = requests.post(Url.url_user_login, data=payload)
        assert response.status_code == 401
        assert response.json() == {"success": False, "message": "email or password are incorrect"}

    @allure.title('Проверка авторизации с неверным паролем')
    def test_auth_invalid_user_success(self):
        payload = {
            'email': DataUser.email,
            'password': DataUser.random_password
        }
        response = requests.post(Url.url_user_login, data=payload)
        assert response.status_code == 401
        assert response.json() == {"success": False, "message": "email or password are incorrect"}

