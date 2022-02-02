
#MIS 207 PE07
################

#Introduction to program
print('This program calculates the discounted price of computer accessories during the Kilobyte Day sale!')

#User accessory price prompt
accessory_price = float(input("What is the list price of the computer accessory you are interested in?"))

#Calculating the discounted price
if accessory_price >= 128:
    accessory_price *= .92
else:
    accessory_price *= .84

#Discounted price printed
print(f'The discounted price of this accessory is {accessory_price:.2f}')