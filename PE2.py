# MIS 207
#
#

rows = input('Please enter the amount of rows you\'d like in your rectangle: ')
col = input('Please enter the amount of rows you\'d like in your rectangle: ')

print('*' * int(col))

for column in range(int(rows)):
    print('*' + ' '*(int(col)-2) + '*')



print('*' * int(col) + '\n')