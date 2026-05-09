import random
import string


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