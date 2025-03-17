import random
import string


def generate_random_data_user():
    letters = string.ascii_lowercase
    random_data = ''.join(random.choice(letters) for i in range(15))
    return random_data

class DataUser:
    email = 'gzvoznikova@ya.ru'
    name = 'gzvoznikova'
    password = 'qwerty123'

    random_name = generate_random_data_user()
    random_email = f'{random_name}@test.test'
    random_password = generate_random_data_user()

class DataIngredient:
    burger1 = ['61c0c5a71d1f82001bdaaa73', '61c0c5a71d1f82001bdaaa79']
    burger2 = ['61c0c5a71d1f82001bdaaa79', '61c0c5a71d1f82001bdaaa7a']

    invalid_hash_ing = "611111b41abdacab0026a733c6"

class Errors:
    create_order_400_message = 'Ingredient ids must be provided'
    create_users_403_message = 'User already exists'
    login_users_401_message = "email or password are incorrect"
    order_users_401_message = 'You should be authorised'
