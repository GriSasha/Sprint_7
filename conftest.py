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
def registered_courier(courier_payload):
    courier_data = register_new_courier_and_return_login_password(courier_payload)

    yield courier_data

    if courier_data is not None:
        delete_courier_by_login_and_password(courier_data['login'], 
                                             courier_data['password'])
        
        