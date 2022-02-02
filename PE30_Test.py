# MIS 207 PE30 Test

from PE30 import Cup


my_cup = Cup()
your_cup = Cup()

print(f"My cup amount: {my_cup.get_amount()}")
print(f"Your cup amount: {your_cup.get_amount()}")

my_cup.fill()
your_cup.fill()

print(f"My cup amount: {my_cup.get_amount()}")
print(f"Your cup amount: {your_cup.get_amount()}")

print(my_cup.sip())

print(f"My cup amount: {my_cup.get_amount()}")

print(my_cup.gulp())

print(f"My cup amount: {my_cup.get_amount()}")