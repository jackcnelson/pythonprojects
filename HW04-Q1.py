# MIS 207 HW04 Q1

# Write a program that asks the user for a number of rows and a number of columns. The program should then use a nested for loop structure to print to the screen a rectangle with an alternating pattern of X's and O's.

rows = input('Please enter the number of rows you want: ')
columns = input('Please enter the number of columns you want: ')


for row in range(int(rows)):
    if row % 2:
        for column in range(int(columns)):
            if column % 2:
                print('X', end='')
            else:
                print('O', end='')
        print()
    else:
        for column in range(int(columns)):
            if column % 2:
                print('O', end='')
            else:
                print('X', end='')
        print()
