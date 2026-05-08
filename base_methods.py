import requests
import random
import string

from data import UrlApi

def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

def generate_courier_payload():
    return {
        'login': generate_random_string(10),
        'password': generate_random_string(10),
        'firstName': generate_random_string(10)
    }

# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
def register_new_courier_and_return_login_password():

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    login = generate_random_string(10),
    password = generate_random_string(10),
    firstName = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": firstName
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(UrlApi.create_courier_api, data=payload)

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(firstName)

    # возвращаем список
    return login_pass 

def create_courier(payload):
    return requests.post(UrlApi.create_courier_api, data=payload)


def login_courier(payload):
    return requests.post(UrlApi.login_courier_api, data=payload)


def delete_courier(courier_id):
    return requests.delete(f'{UrlApi.url}/courier/{courier_id}')


def delete_courier_by_login_and_password(login, password):
    payload = {
        'login': login,
        'password': password
    }

    response = login_courier(payload)

    if response.status_code == 200:
        courier_id = response.json()['id']
        delete_courier(courier_id)


def get_order_payload():
    return {
        'firstName': 'Иван',
        'lastName': 'Иванов',
        'address': 'Москва, улица Строителей, дом 12',
        'metroStation': 4,
        'phone': '+7 800 555 35 35',
        'rentTime': 5,
        'deliveryDate': '2026-06-06',
        'comment': 'Тестовый заказ'
    }