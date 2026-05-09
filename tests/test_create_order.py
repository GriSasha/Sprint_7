import allure
import pytest
import requests

from data import UrlApi
from helpers import get_order_payload


class TestCreateOrder:

    @allure.title('Создание заказа с разными вариантами цвета')
    @allure.description('Заполняем цвет самоката, отправляем запрос на создание заказа,'
    'ожидаем ответ 201 и что в ответе есть номер заказа')
    @pytest.mark.parametrize(
        'color',
        [
            ['BLACK'],
            ['GREY'],
            ['BLACK', 'GREY'],
            []
        ]
    )
    def test_create_order_with_different_colors_returns_track(self, color):
        payload = get_order_payload()

        if color:
            payload['color'] = color

        response = requests.post(UrlApi.orders_api, json=payload)

        assert response.status_code == 201
        assert 'track' in response.json()