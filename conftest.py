import pytest

from base_methods import (
    register_new_courier_and_return_login_password,
    delete_courier_by_login_and_password,
    generate_courier_payload
)


@pytest.fixture
def courier_payload():
    return generate_courier_payload()


@pytest.fixture
def registered_courier():
    courier_data = register_new_courier_and_return_login_password()

    login = courier_data[0]
    password = courier_data[1]
    firstName = courier_data[2]

    yield {
        'login': login,
        'password': password,
        'firstName': firstName
    }

    delete_courier_by_login_and_password(login, password)