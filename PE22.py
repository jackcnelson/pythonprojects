# MIS 207 PE22
#
# Write and test a function called list_filter that accepts a list of numbers,
# and a minimum value and returns a new list with all elements of the
# original list that are larger than the given minimum value.

# Defining list_filter function
def list_filter(lst, minimum):
    new_lst = []
    for num in lst:
        if num > minimum:
            new_lst.append(num)
    return new_lst

# Testing the function

print(list_filter([1, 2, 3, 4, 5, 6], 2))
print(list_filter([51, 32, 13, 24, 15, 6], 22))
