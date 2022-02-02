# MIS 207 PE17

# This program uses a function to compute the area of a circle given the radius

import math

# Defining user input
radius = float(input('Please enter the radius: '))

# Defining function that calculates circle area
def circle_area(radius):
    area = math.pi * radius ** 2
    return area

# Printing the calculated area by running the function
print(f'The area of this circle is: {circle_area(radius): .2f}.')