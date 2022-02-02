# MIS 207 PE20
#
# This program stores user input grade data in a list

grades = []
grade = float(input('Please enter grade values (enter a negative number to stop): '))

while grade > 0:
    grades.append(grade)
    grade = float(input('Please enter grade values (enter a negative number to stop): '))

print('These were the grades entered: ' + str(grades))
print('The sum of the grades was: ' + str(sum(grades)))
print('The lowest grade was: ' + str(min(grades)))
print('The highest grade was: ' + str(max(grades)))
print('The average grade was: ' + str(sum(grades) / len(grades)))