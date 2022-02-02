# MIS 207 Practice Exercise 1
#
#
import random

print('Welcome to the number guessing game, you get 7 guesses to guess the correct number between 1 & 100.')

try_number = 1
correct_guess = random.randint(1, 100)

while try_number <= 8:
    if try_number == 8:
        print('You ran out of guesses, better luck next time!')
        break
    guess = input(f'Guess #{try_number}. Enter a number: ')
    try:
        guess = int(guess)
    except ValueError:
        print('Error. Please enter a valid integer.')
        continue

    if 1 <= guess <= 100:
        if guess > correct_guess:
            print(f'The correct number is less than {guess}.')
            try_number += 1
            continue
        elif guess < correct_guess:
            print(f'The correct number is greater than {guess}.')
            try_number += 1
            continue
        else:
            print(f'{correct_guess} is the right number! Congrats and goodbye.')
            break
    else:
        print("Sorry to see that you've quit, better luck next time.")
        break