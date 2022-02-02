# MIS 207 PE16

# This program simulates the outcome of a user who begins with $10,000 in the pot, and bets $1 on 10,000 plays of Sort-of-Crap.

#
#
import random

# Starting pot size
pot = 10000
plays = 10000

while plays > 0:
    bet = 1
    plays -= 1
    # Roll dice
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    dice = die1 + die2

    # Either gain or lose money based on dice roll
    if dice == 2 or dice == 3 or dice == 11 or dice == 12:
        pot += bet
    else:
        pot -= bet

print(f"\n\nAfter 10,000 bets, the pot is ${pot:,.2f}.")

# I am not surprised to see that we lose roughly $6,700.00 each time the program is run
# Our odds in this game are not good and the result is a win percentage of roughly 33% of the time