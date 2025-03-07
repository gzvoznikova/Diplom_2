class Url:
    base_url = 'https://stellarburgers.nomoreparties.site'
    url_user_create = f'{base_url}/api/auth/register'
    url_user_login = f'{base_url}/api/auth/login'
    url_user_update = f'{base_url}/api/auth/user'
    url_user_delete = f'{base_url}/api/auth/user'
    url_order_create = f'{base_url}/api/orders'
    url_user_orders = f'{base_url}/api/orders'

    headers = {'Content-Type': 'application/json'}