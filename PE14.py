# MIS 207 PE14

# This program asks a user how many rows and columns of '#' they would like printed

# User welcome
print('This program will print #\'s in the format of rows and columns you want.\n')

# Defining user input
rows = input('Enter the amount of rows you want: ')
columns = input('Enter the amount of columns you want: ')

# Nested for loops to print the #'s in the correct format
for row in range(int(rows)):
    for column in range(int(columns)):
        print('#', end='')
    print()