from conftest import *
from data import DataUser

class TestUserUpdate:
    payload = {
        'email': DataUser.random_email,
        'name': DataUser.random_name,
        'password': DataUser.random_password
    }

    @allure.title('Проверка изменения данных авторизованного пользователя')
    def test_update_user_auth_success(self, create_new_user):
        response = requests.patch(Url.url_user_update, headers={
            'Authorization': create_new_user[1]['accessToken']}, data=TestUserUpdate.payload)
        assert response.status_code == 200
        assert response.json()['success'] is True
        assert response.json()['user']['email'] == TestUserUpdate.payload['email']
        assert response.json()['user']['name'] == TestUserUpdate.payload['name']

    @allure.title('Проверка изменения данных не авторизованного пользователя')
    def test_update_user_not_auth_error(self):
        response = requests.patch(Url.url_user_update, headers={}, data=TestUserUpdate.payload)
        assert response.status_code == 401
        assert response.json() == {'success': False, 'message': 'You should be authorised'}