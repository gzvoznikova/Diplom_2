import pytest
import allure
import requests
from urls import *
from data import *


@pytest.fixture
@allure.title('Фикстура создает пользователя с рандомными данными')
def create_new_user():
    payload = {
        'email': DataUser.random_email,
        'password': DataUser.random_password,
        'name': DataUser.random_name
    }
    response = requests.post(Url.URL_ORDER_CREATE, data=payload)
    response_body = response.json()

    yield payload, response_body

    access_token = response_body['accessToken']
    requests.delete(Url.URL_USER_DELETE, headers={'Authorization': access_token})

@pytest.fixture
@allure.title('Фикстура создает пользователя и заказ')
def create_user_and_order(create_new_user):
    access_token = create_new_user[1]['accessToken']
    headers = {'Authorization': access_token}
    payload = {'ingredients': [DataIngredient.burger2]}
    response_body = requests.post(Url.URL_ORDER_CREATE, data=payload, headers=headers)

    yield access_token, response_body

    requests.delete(Url.URL_USER_DELETE, headers={'Authorization': access_token})

@pytest.fixture
def payload_data_user():
    payload = {
        'email': DataUser.random_email,
        'name': DataUser.random_name,
        'password': DataUser.random_password
    }
    return payload