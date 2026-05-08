
class UrlApi:
    url = 'https://qa-scooter.praktikum-services.ru/api/v1'

    create_courier_api = f'{url}/courier'
    login_courier_api = f'{url}/courier/login'
    orders_api = f'{url}/orders'


class Response:
    response_courier_created = {'ok': True}

    not_enough_data_for_create_courier = 'Недостаточно данных для создания учетной записи'
    login_used = 'Этот логин уже используется'
    not_enough_data_for_login = 'Недостаточно данных для входа'
    account_not_found = 'Учетная запись не найдена'