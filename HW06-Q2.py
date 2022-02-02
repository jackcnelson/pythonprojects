# MIS 207 HW06 Q2
#
# Write and test a function that accepts a table (2-dimensional list) and prints the contents of the table in a grid/table-like format.

def grid_form(lst):
    for row in lst:
        for col in row:
            print(f'{col: ^10}', end='')
        print()

grid_form([[1, 2, 3], [4, 5, 6]])
grid_form([['house', 'dog'], ['cottage', 'cat']])