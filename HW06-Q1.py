# MIS 207 HW06 Q1
#
# Create and test a function that accepts a list of digits and returns a new list containing the word for each of the digits found.

def word_form(lst):
    word_lst = []
    for item in lst:
        if item == 1:
            word_lst.append('one')
        elif item == 2:
            word_lst.append('two')
        elif item == 3:
            word_lst.append('three')
        elif item == 4:
            word_lst.append('four')
        elif item == 5:
            word_lst.append('five')
        elif item == 6:
            word_lst.append('six')
        elif item == 7:
            word_lst.append('seven')
        elif item == 8:
            word_lst.append('eight')
        else:
            word_lst.append('nine')
    return word_lst

print(word_form([2, 2, 3, 1, 8, 9]))
print(word_form([3, 2, 4, 5, 6]))
