from base.model import ModelCard


class User:
    def __init__(self, name, dataCard: ModelCard):
        self.name=name
        self.card=dataCard

class Automat(User):

    def __init__(self, name, dataCard):
        super().__init__(name, dataCard)

    def opred_skid(self):
        if self.card.balance > 0 and self.card.balance <= 100:
            skidka = 1
        if self.card.balance >100 and self.card.balance <= 200:
            skidka = 3
        if self.card.balance >200 and self.card.balance <= 500:
            skidka = 5
        if self.card.balance >500:
            skidka = 10
        return skidka

    def pokupka(self, price):
        value = self.opred_skid()
        stoimost = (price*value)/100
        if self.card.balance > stoimost:
            self.card.balance = self.card.balance - stoimost
        else:
            raise Exception("not enought money")
        return self.card.balance


