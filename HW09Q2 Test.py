# MIS 207 HW09 Q2 Test
#
#

from HW09Q2 import BankAccount

account_1 = BankAccount()
account_2 = BankAccount()

account_1.deposit(1000)
account_2.deposit(500)

print(account_1.get_balance())
print(account_2.get_balance())

account_2.withdraw(600)

account_2.withdraw(400)

print(account_2.get_balance())
