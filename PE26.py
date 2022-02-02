# MIS 207 PE26
#
# You’re provided a populations.txt file that contains country populations.
# Read this file, and calculate the total population of all the countries list
# in this file.

in_file = open('countries.txt', 'r', encoding='utf-8')

txt = in_file.read()
lines = txt.split('\n')
total_pop = 0
for line in lines:
    if ':' in line:
        description, pop = line.split(':')
        total_pop += int(pop)

print(f'The total population is: {total_pop}.')

in_file.close()