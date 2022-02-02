# MIS 207 HW03 Question 2

# This program computes a tax schedule

# Defining variable for marital status and income level

marital_status = input('Enter your marital status. Enter m for married or s for single: ').lower()
income = float(input('Enter your income from the past year: '))

if marital_status == 's':
    if income < 0:
        print('Invalid income entered.')
    elif 0 <= income <= 9000:
        print('You owe ' + str(income * .1) + ' in taxes.')
    elif 9000 < income <= 32000:
        print('You owe ' + str(((income - 9000) * .15) + 900 + (9000 * .1)) + ' in taxes.')
    else:
        print('You owe ' + str(((income - 32000) * .25) + 4350 + (23000 * .15) + 900 + (9000 * .1)) + ' in taxes.')
if marital_status == 'm':
    if income < 0:
        print('Invalid income entered.')
    elif 0 <= income <= 18000:
        print('You owe ' + str(income * .1) + ' in taxes.')
    elif 18000 < income <= 64000:
        print('You owe ' + str(((income - 18000) * .15) + 1800 + (18000 * .1)) + ' in taxes.')
    else:
        print('You owe ' + str(((income - 64000) * .25) + 8700 + (46000 * .15) + 1800 + (18000 * .1)) + ' in taxes.')

