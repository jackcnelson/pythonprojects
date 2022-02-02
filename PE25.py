# MIS 207 PE25
#
# Count the number of times "Waldo" appears in the txt file

in_file = open('waldo.txt', 'r', encoding="utf-8")

waldo_count = 0
for line in in_file:
    words = line.split()
    if len(line) > 0:
        if 'waldo' or 'Waldo' in words:
            waldo_count += 1
#for line in in_file:
#    words = line.split()
#    for word in words:
#        if 'waldo' in word.lower():
#            waldo_count += 1

print(f'The word \"Waldo\" appears {waldo_count} times in this text.')

in_file.close()