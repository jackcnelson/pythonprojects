# MIS 207 HW07 Q1
#
#
infile = open('input.txt', 'r', encoding="utf-8")
outfile = open('outfile.txt', 'w')

lines = infile.readlines()

for line in lines:
    num_1, num_2, num_3 = line.split(',')
    line = line.strip('\n')
    outfile.write(f"{line},{str((int(num_1)+int(num_2)+int(num_3)))}")
    outfile.write('\n')

infile.close()
outfile.close()