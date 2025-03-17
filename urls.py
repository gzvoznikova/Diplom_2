class Url:
    BASE_URL = 'https://stellarburgers.nomoreparties.site'
    URL_USER_CREATE = f'{BASE_URL}/api/auth/register'
    URL_USER_LOGIN = f'{BASE_URL}/api/auth/login'
    URL_USER_UPDATE = f'{BASE_URL}/api/auth/user'
    URL_USER_DELETE = f'{BASE_URL}/api/auth/user'
    URL_ORDER_CREATE = f'{BASE_URL}/api/orders'
    URL_USER_ORDERS = f'{BASE_URL}/api/orders'

    headers = {'Content-Type': 'application/json'}