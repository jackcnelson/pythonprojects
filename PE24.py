# MIS 207 PE24
#
# Create a program that asks for student name, and input filename. The
# input file contains a list of grades (one per line).


name = input('Enter student name: ')
infile = open(input('Enter input filename: '), 'r')

total = 0
count = 0

print(name)

line = infile.readline()
while line != '':
    grade = float(line)
    total += grade
    count += 1
    print(str(grade))
    line = infile.readline()

average = total / count
print(f'Average: {average: .2f}')

infile.close()
