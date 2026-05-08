import pytest
import allure
import requests

from data import UrlApi


class TestOrdersList:

    @allure.title('В тело ответа возвращается список заказов')
    @allure.description('Отправляем запрос на получение списка заказов, ожидаем' \
    'возвращения списка заказов в теле ответа')
    def test_orders_list_contains_orders(self):
        response = requests.get(UrlApi.orders_api)

        assert response.status_code == 200
        assert 'orders' in response.json()
        assert isinstance(response.json()['orders'], list)

