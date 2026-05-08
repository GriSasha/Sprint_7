import allure
import pytest

from base_methods import login_courier, generate_courier_payload
from data import Response


class TestLoginCourier:

    @allure.title('Курьер может авторизоваться')
    @allure.description('Вводим логин и пароль зарегистрированного курьера, отправляем запрос на авторизацию,' \
    'ожидаем статус ответа - 200, запрос возвращает id курьера')
    def test_courier_can_login(self, registered_courier):
        login_payload = {
            'login': registered_courier['login'],
            'password': registered_courier['password']
        }

        response = login_courier(login_payload)

        assert response.status_code == 200
        assert 'id' in response.json()

    @allure.title('Система вернет ошибку при авторизации, если не заполнить login')
    @allure.description('Не заполняем login, заполняем password существующими данными,' \
    'отправляем запрос на авторизацию, ожидаем появления ошибки 400')
    def test_login_without_login_returns_error(self, registered_courier):

        login_payload = {'password': registered_courier['password']}

        response = login_courier(login_payload)

        assert response.status_code == 400
        assert response.json()['message'] == Response.not_enough_data_for_login

    @allure.title('Система вернет ошибку при авторизации, если не заполнить password')
    @allure.description('Заполняем login существующими данными, не заполняем password,' \
    'отправляем запрос на авторизацию, ожидаем появления ошибки 400')
    def test_login_without_password_returns_error(self, registered_courier):
        
        login_payload = {'login': registered_courier['login']}

        response = login_courier(login_payload)

        assert response.status_code == 400
        assert response.json()['message'] == Response.not_enough_data_for_login

    @allure.title('Система вернёт ошибку, если неправильно указан логин')
    @allure.description('Заполняем login несуществующими данными, заполняем пароль существующими данными,' \
    'отправляем зарос на авторизацию, ожидаем появления ошибки 404')
    def test_login_with_wrong_login_returns_error(self, registered_courier):
        login_payload = {
            'login': 'wrong_login',
            'password': registered_courier['password']
        }

        response = login_courier(login_payload)

        assert response.status_code == 404
        assert response.json()['message'] == Response.account_not_found

    @allure.title('Система вернёт ошибку, если неправильно указан пароль')
    @allure.description('Заполняем login существующими данными, заполняем password несуществующими данными,' \
    'отправляем зарос на авторизацию, ожидаем появления ошибки 404')
    def test_login_with_wrong_password_returns_error(self, registered_courier):
        login_payload = {
            'login': registered_courier['login'],
            'password': 'wrong_password'
        }

        response = login_courier(login_payload)

        assert response.status_code == 404
        assert response.json()['message'] == Response.account_not_found

    @allure.title('Если авторизоваться под несуществующим пользователем, вернётся ошибка')
    @allure.description('Заполняем login и password несуществующими данными, отправляем запрос на авторизацию, ' \
    'ожидаем появления ошибки 404')
    def test_login_nonexistent_courier_returns_error(self):
        nonexistent_courier = generate_courier_payload()

        login_payload = {
            'login': nonexistent_courier['login'],
            'password': nonexistent_courier['password']
        }

        response = login_courier(login_payload)

        assert response.status_code == 404
        assert response.json()['message'] == Response.account_not_found