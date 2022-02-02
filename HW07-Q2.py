# MIS 207 HW07 Q2
#
#

infile_name = input("Please enter a file name: ")

while True:
   try:
      infile = open(infile_name, 'r', encoding="utf-8")
      break
   except:
      infile_name = input("File not found, please enter a valid file name: ")
infile = open(infile_name, 'r', encoding="utf-8")


infile_read = infile.readlines()

count = 0
for line in infile_read:
   if not line.isspace():
      count += 1

print(f"The number of non-blank lines in this file is: {count}.")

infile.close()