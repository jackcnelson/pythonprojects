
#MIS 207 PE10

#This program uses boolean expressions to make determinations on two user number inputs

#Intro to program and defining variables
print('Please enter two numbers.')
number_one = float(input('First Number: '))
number_two = float(input('Second Number: '))

#If/Elif/Else to determine if numbers are both odd, even, or both
if (number_one % 2 == 0) and (number_two % 2 == 0):
    print('Both numbers are even.')
elif (number_one % 2 != 0) and (number_two % 2 != 0):
    print('Both numbers are odd.')
else:
    print('One number is odd and the other is even.')

#If/Elif/Else to determine
if number_one + number_two > 20:
    print('These numbers added together equal more than my age.')
elif number_one + number_two < 20:
    print('These numbers added together equal less than my age.')
else:
    print('These numbers added together equal my age.')