infile = open("input.txt", "r")
for word in infile :
   word = word.lstrip(".!")
   print(word)