#This program calculates the area of a circle when a user inputs the radius
print('This program calculates the area of a circle given a radius.')
circle_radius = float(input('What is your circle\'s radius?'))
circle_area = circle_radius ** 2 * 3.14
print('The area of a circle with radius = ' + str(circle_radius) + ' is ' + str(circle_area))
