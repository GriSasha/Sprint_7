import allure
import pytest

from base_methods import create_courier, delete_courier_by_login_and_password
from data import Response


class TestCreateCourier:

    @allure.title('Курьера можно создать')
    @allure.description('Отправляем запрос на создание курьера, ожидаем статус ответа 201' \
    ' и сообщение об успешном создании')
    def test_create_courier_success(self, courier_payload):
        response = create_courier(courier_payload)

        assert response.status_code == 201
        assert response.json() == Response.response_courier_created

        delete_courier_by_login_and_password(
            courier_payload['login'],
            courier_payload['password']
        )

    @allure.title('Нельзя создать двух одинаковых курьеров')
    @allure.description('Создаем курьера, ожидаем статус ответа 201, ' \
    'далее пытаемся создать курьера с теми же данными, ожидаем статус ответа 409')
    def test_create_two_same_couriers_returns_error(self, courier_payload):
        first_response = create_courier(courier_payload)
        second_response = create_courier(courier_payload)

        assert first_response.status_code == 201
        assert second_response.status_code == 409

        delete_courier_by_login_and_password(
            courier_payload['login'],
            courier_payload['password']
        )

    @allure.title('Для создания курьера нужно передать login')
    @allure.description('Не заполняем login при заполнении данных для создания учетной записи курьера, ' \
    'отправляем запрос, ожидаем статус ответа 400 и сообщения об ошибке')
    def test_create_courier_without_login_returns_error(self, courier_payload):
        courier_payload.pop('login')

        response = create_courier(courier_payload)

        assert response.status_code == 400
        assert response.json()['message'] == Response.not_enough_data_for_create_courier

    @allure.title('Для создания курьера нужно передать password')
    @allure.description('Не заполняем password при заполнении данных для создания учетной записи курьера, ' \
    'отправляем запрос, ожидаем статус ответа 400 и сообщения об ошибке')
    def test_create_courier_without_password_returns_error(self, courier_payload):
        courier_payload.pop('password')

        response = create_courier(courier_payload)

        assert response.status_code == 400
        assert response.json()['message'] == Response.not_enough_data_for_create_courier

    @allure.title('Если создать курьера с уже существующим логином, вернётся ошибка')
    @allure.description('Заполняем login уже существующими данными, ' \
    'отправляем запрос, ожидаем статус ответа 409 и сообщения об ошибке')
    def test_create_courier_with_existing_login_returns_error(self, courier_payload):
        create_courier(courier_payload)

        new_courier_with_same_login = {
            'login': courier_payload['login'],
            'password': 'another_password',
            'firstName': 'another_name'
        }

        response = create_courier(new_courier_with_same_login)

        assert response.status_code == 409
        assert response.json()['message'] == Response.login_used

        delete_courier_by_login_and_password(
            courier_payload['login'],
            courier_payload['password']
        )