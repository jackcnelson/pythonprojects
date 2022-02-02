# MIS 207 PE13

# This program is a 1-10 number guessing game using a while loop to check user input

# User welcome and input

print('See if you can guess what number the computer is thinking!\n')
guess = input('Please enter a number between 1 and 10: ')

while int(guess) != 5:
    if 0 < int(guess) <= 10:
        print('Wrong guess, try again!')
        guess = input('Please enter a number between 1 and 10: ')
    else:
        print('Invalid input.')
        guess = input('Please enter a number between 1 and 10: ')
print('You guessed correctly, goodbye!')