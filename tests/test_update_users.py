from conftest import *
import requests
import allure

class TestUserUpdate:

    @allure.title('Проверка изменения данных авторизованного пользователя')
    def test_update_user_auth_success(self, create_new_user, payload_data_user):
        response = requests.patch(Url.URL_USER_UPDATE, headers={
            'Authorization': create_new_user[1]['accessToken']}, data=payload_data_user)
        assert response.status_code == 200
        assert response.json()['success'] is True
        assert response.json()['user']['email'] == payload_data_user['email']
        assert response.json()['user']['name'] == payload_data_user['name']

    @allure.title('Проверка изменения данных не авторизованного пользователя')
    def test_update_user_not_auth_error(self, payload_data_user):
        response = requests.patch(Url.URL_USER_UPDATE, headers={}, data=payload_data_user)
        assert response.status_code == 401
        assert response.json() == {'success': False, 'message': 'You should be authorised'}