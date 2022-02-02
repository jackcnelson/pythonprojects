# MIS 207 PE21
##
#  This program reads a sequence of values and prints them, marking the
#  largest value.
#

# Create an empty list.
values = []

# Read the input values.
user_input = input("Please enter values, Q to quit: ")
while user_input.upper() != "Q" :
   values.append(float(user_input))
   user_input = input("Please enter values, Q to quit: ")

# Finding the largest and smallest values in the list
largest = max(values)
smallest = min(values)

# Print all values, marking the largest and smallest.
for element in values:
   print(element, end="")
   if element == largest :
      print(" <== largest value", end="")
   if element == smallest :
      print(" <== smallest value", end="")
   print()

