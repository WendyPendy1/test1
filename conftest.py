import pytest
from base.model import ModelCard
from base.base_page import User, Automat
from page.page import Proverka
from faker import Faker


@pytest.fixture(scope="function")
def initialize():
    fake=Faker()
    client_card = ModelCard(number=fake.credit_card_number(), balance=fake.random_number())
    client = User(name=fake.name(), dataCard=client_card)
    obj_auth = Automat(name=client.name, dataCard=client.card)
    prov=Proverka(client_card, client, obj_auth)
    yield prov
    client_card = None
    client = None
    obj_auth = None
    print('data clean')

