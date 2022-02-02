# MIS 207 HW09 Q2
#
#

class BankAccount:

    account = 0

    def __init__(self):
        self._balance = 0
        self._account_num = BankAccount.account
        BankAccount.account += 1

    def deposit(self, amount):
        self._balance += float(amount)

    def withdraw(self, amount):
        if float(amount) <= self._balance:
            self._balance -= float(amount)
        else:
            print(f'This withdraw amount exceeds the current account balance of {self._balance:.2f}.')

    def get_balance(self):
        return f'Account Number: {self._account_num}\nAccount Balance: {self._balance:.2f}'