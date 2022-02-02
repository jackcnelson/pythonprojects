# MIS 207 PE15

# This program determines if a user input is an Iowan phone number

# Defining user input
user_input = input('Please enter a phone number formatted (###)###-####: ')

# Defining empty string variable
phone = ''

for i in user_input:
    if i.isdigit():
        phone += i

if phone[0:3] in '319 515 563 641 712':
    print('This phone number is from Iowa.')
else:
    print('This phone number is not from Iowa.')
