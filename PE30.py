# MIS 207 PE30
#
#

class Cup:

    def __init__(self, size = 16):
        self._size = size
        self._amount = 0

    def fill(self):
        self._amount = self._size

    def drink(self, amount):
        ret_amount = 0
        if self._amount >= amount:
            self._amount -= amount
            ret_amount = amount
        else:
            ret_amount = self._amount
            self._amount = 0
        return ret_amount

    def empty(self):
        self._amount = 0

    def get_amount(self):
        return self._amount

    def sip(self):
        ret_amount = 0
        if .5 >= self._amount:
            self._amount -= .5
        else:
            ret_amount = self._amount
            self._amount = 0
        return ret_amount

    def sip(self):
        ret_amount = 0
        if .5 <= self._amount:
            self._amount -= .5
        else:
            ret_amount = self._amount
            self._amount = 0
        return ret_amount

    def gulp(self):
        ret_amount = 0
        if 2 <= self._amount:
            self._amount -= 2
        else:
            ret_amount = self._amount
            self._amount = 0
        return ret_amount