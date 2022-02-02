#MIS 207 PE12
#
#This program uses a while loop to check a user's input

#User input
answer = int(input('Enter a number between 1 and 10: '))

#While loop checking user input
while not 1 <= answer <= 10:
    print('Invalid Input. Please try again.')
    answer = int(input('Enter a number between 1 and 10: '))

#Exit statement
print('Goodbye!')
