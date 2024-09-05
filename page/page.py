from base.base_page import User, Automat
from base.model import ModelCard

class Proverka:
    def __init__(self, client_card, client, obj_auth):
        self.client_card = client_card
        self.client = client
        self.obj_auth = obj_auth

    def proverka_skidki_1(self):
        if self.client.card.balance > 0 and self.client.card.balance <= 100:
            assert self.obj_auth.opred_skid() == 1

    def proverka_skidki_3(self):
        if self.client.card.balance > 100 and self.client.card.balance <= 200:
            assert self.obj_auth.opred_skid() == 3

    def proverka_skidki_5(self):
        if self.client.card.balance > 200 and self.client.card.balance <= 500:
            assert self.obj_auth.opred_skid() == 5

    def proverka_skidki_10(self):
        if self.client.card.balance > 500:
            assert self.obj_auth.opred_skid() == 10



