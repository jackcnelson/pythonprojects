# MIS 207 PE 31
#
#

import random

class SKU:

    count = 0

    def __init__(self, description='', cost=0, price=0):
        self._description = str(description)
        self._cost = float(cost)
        self._price = float(price)
        self._sku_number = SKU.count
        SKU.count += 1

    def __str__(self):
        return f'SKU Number: {self._sku_number}\nDescription: {self._description}\nCost: ${self._cost:.2f}\nPrice: ${self._price:.2f} '

    def enter_description(self, desc):
        self._description = str(desc)

    def get_description(self):
        return self._description

    def enter_cost(self, cost):
        self._cost = float(cost)

    def get_cost(self):
        return f'${self._cost:.2f}'

    def enter_price(self, price):
        self._price = float(price)

    def get_price(self):
        return f'${self._price:.2f}'