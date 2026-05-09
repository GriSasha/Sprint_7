import requests
import allure

from data import UrlApi



# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
@allure.step('Отправляем post-запрос на регистрацию курьера со случайными логином, паролем и firstName ' \
'и сохраняем ответ в переменную response')
def register_new_courier_and_return_login_password(courier_payload):

    response = create_courier(courier_payload)

    if response.status_code == 201:
        return courier_payload

    return None


@allure.step('Отправляем post-запрос на создание курьера')
def create_courier(payload):
    return requests.post(UrlApi.create_courier_api, json=payload)

@allure.step('Отправляем post-запрос на вход в учетную запись курьера')
def login_courier(payload):
    return requests.post(UrlApi.login_courier_api, json=payload)

@allure.step('Отправляем delete-запрос, чтобы удалить курьера из базы данных')
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
