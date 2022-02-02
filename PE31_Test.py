# PE31 Test
#
#

from PE31 import SKU

item_1 = SKU('iPhone Model 13 Max',770.80,1399.99)
item_2 = SKU()


item_2.enter_description('iPhone Model 12')

print(item_1.get_description())

item_2.enter_cost(650.75)

print(item_2.get_cost())

item_2.enter_price(1099.99)

print(item_2.get_price())

print(item_1.__str__())
print(item_2.__str__())