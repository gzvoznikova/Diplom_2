import allure
import requests
from data import DataUser, Errors
from urls import Url

class TestsCreateUsers:
    @allure.title('Проверка успешной регистрации пользователя')
    def test_create_new_user_success(self):
        payload = {
            'email': DataUser.random_email,
            'name': DataUser.random_name,
            'password': DataUser.random_password
        }
        response = requests.post(Url.URL_USER_CREATE, data=payload)
        assert response.status_code == 200
        assert response.json()['success'] is True
        assert response.json()['user']['email'] == payload['email']
        assert response.json()['user']['name'] == payload['name']

    @allure.title('Проверка ответа регистрации с существующим в базе email')
    def test_create_user_with_existing_email_failed(self):
        payload = {
            'email': DataUser.email,
            'password': DataUser.random_password,
            'name': DataUser.random_name
        }
        response = requests.post(Url.URL_USER_CREATE, data=payload)
        assert response.status_code == 403
        assert response.json().get("message") == Errors.create_users_403_message

    @allure.title('Проверка ответа регистрации с пустым email')
    def test_create_user_with_empty_email_failed(self):
        payload = {
            'email': '',
            'password': DataUser.random_password,
            'name': DataUser.random_name
        }
        response = requests.post(Url.URL_USER_CREATE, data=payload)
        assert (response.status_code == 403 and response.json() ==
                {'success': False, 'message': 'Email, password and name are required fields'})