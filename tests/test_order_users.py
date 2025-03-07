from conftest import *
import requests
import allure

class TestOrdersUsers:
    @allure.title('Проверка успешного получения списка заказов для авторизованного пользователя')
    def test_orders_auth_user_success(self, create_user_and_order):
        headers = {'Authorization': create_user_and_order[0]}
        response = requests.get(Url.url_user_orders, headers=headers)
        assert response.status_code == 200
        assert response.json()['success'] is True
        assert 'orders' in response.json().keys()
        assert 'total' in response.json().keys()

    @allure.title('Проверка получения списка заказов для неавторизованного пользователя')
    def test_orders_not_auth_user_success(self):
        response = requests.get(Url.url_user_orders, headers=Url.headers)
        assert response.status_code == 401
        assert response.json() == {'success': False, 'message': 'You should be authorised'}