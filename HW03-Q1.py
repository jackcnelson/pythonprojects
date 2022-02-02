# MIS 207

# This is a horoscope program

# User birthday input

bday_month = int(input('Enter your birthday month in integer form: '))
bday_day = int(input('\nEnter your birthday day in integer form: '))

# Variable used to detect error

error = 0

# Checks to make sure the birthday date is valid
if not 1 <= bday_month <= 12:
    print('You entered an invalid birthday.')
    error = 1
elif bday_month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
    if bday_day > 31:
        print('You entered an invalid birthday.')
        error = 1
elif bday_month == 4 or 6 or 9 or 11:
    if bday_day > 30:
        print('You entered an invalid birthday.')
        error = 1
elif bday_month == 2:
    if bday_day > 28:
        print('You entered an invalid birthday.')
        error = 1
else:
    error = 0

# If the birthday is valid, the program proceeds

if error == 0:

    # Putting birthday into a simple float in order to make if statements easier

    bday_day = bday_day / 100
    bday_float = bday_month + bday_day

    # If statements to identify horoscope sign based on birthday float

    if 1.20 <= bday_float <= 2.18:
        print('You are an aquarius. \nYou will have good luck on future MIS 207 tests.')
    elif 2.18 < bday_float <= 3.2:
        print('You are a pisces. \nYou will find the love of your life in your next programming class.')
    elif 3.2 < bday_float <= 4.19:
        print('You are an Aries. \nYou will likely do poorly in MIS 207 if you do not study vigorously.')
    elif 4.19 < bday_float <= 5.2:
        print('You are a Taurus. \nYou will find a successful career in programming.')
    elif 5.2 < bday_float <= 6.2:
        print('You are a Gemini. \nYou will like your next programming professor.')
    elif 6.2 < bday_float <= 7.22:
        print('You are a Cancer. \nYou will become a coding prodigy in the next two years.')
    elif 7.22 < bday_float <= 8.22:
        print('You are a Leo. \nYou will work closely with developers in your career but not program yourself.')
    elif 8.22 < bday_float <= 9.22:
        print('You are a Virgo. \nYou will get the developing job of your dreams.')
    elif 9.22 < bday_float <= 10.22:
        print('You are a Libra. \nYou will never program again after this class.')
    elif 10.22 < bday_float <= 11.21:
        print('You are a Scorpio. \nYou will fall in love with a fellow programmer who will friend-zone you.')
    elif 11.21 < bday_float <= 12.21:
        print('You are a Sagittarius. \nYou will build a billion dollar software company.')
    elif (12.21 < bday_float <= 12.31) or (1 <= bday_float <= 1.19):
        print('You are a Capricorn. \nYou will use programming to solve climate change.')
    else:
        print('You entered an invalid birthday date.')
