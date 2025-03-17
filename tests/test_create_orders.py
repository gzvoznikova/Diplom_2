from conftest import *
from data import Errors
import allure
import pytest

class TestCreateOrders:
    @allure.title('Проверка создание заказа с указанными ингредиентами и авторизованным пользователем')
    @pytest.mark.parametrize('burger_ing', [DataIngredient.burger1, DataIngredient.burger2])
    def test_create_order_auth_user_success(self, create_new_user, burger_ing):
        headers = {'Authorization': create_new_user[1]['accessToken']}
        payload = {'ingredients': [burger_ing]}
        response = requests.post(Url.URL_ORDER_CREATE, data=payload, headers=headers)
        assert response.status_code == 200
        assert response.json()['success'] is True
        assert 'name' in response.json().keys()
        assert 'number' in response.json()['order'].keys()

    @allure.title('Проверка создание заказа с указанными ингредиентами без авторизованного пользователя')
    @pytest.mark.parametrize('burger_ing', [DataIngredient.burger1, DataIngredient.burger2])
    def test_create_order_not_auth_user_success(self, burger_ing):
        payload = {'ingredients': [burger_ing]}
        response = requests.post(Url.URL_ORDER_CREATE, data=payload, headers={})
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title('Проверка cоздания заказа без указания ингредиентов для авторизованного пользователя')
    def test_create_order_not_ing_auth_user_error(self, create_new_user):
        headers = {'Authorization': create_new_user[1]['accessToken']}
        payload = {'ingredients': []}
        response = requests.post(Url.URL_ORDER_CREATE, data=payload, headers=headers)
        assert response.status_code == 400
        assert response.json().get("message") == Errors.create_order_400_message

    @allure.title('Проверка создания заказа без указания ингредиентов для не авторизованного пользователя')
    def test_create_order_not_ing_not_auth_error(self):
        payload = {'ingredients': []}
        response = requests.post(Url.URL_ORDER_CREATE, data=payload, headers=Url.headers)
        assert response.status_code == 400
        assert response.json().get("message") == Errors.create_order_400_message

    @allure.title('Проверка создания заказа с невалидным хэшем ингредиента для авторизованного пользователя')
    def test_create_order_invalid_hash_ingedient_error(self, create_new_user):
        headers = {'Authorization': create_new_user[1]['accessToken']}
        payload = {'ingredients': [DataIngredient.invalid_hash_ing]}
        response = requests.post(Url.URL_ORDER_CREATE, data=payload, headers=headers)
        assert response.status_code == 500
