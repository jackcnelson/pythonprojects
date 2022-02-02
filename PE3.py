# MIS 207 Practice Exercise 3
#
#
class dictionary(dict):

    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value


new_dict = dictionary()

infile = open('input-1.txt', 'r', encoding="utf-8")

line = infile.readline()

for line in infile:
    words = line.split()
    for word in words:
        word_count = 0
        for instance in word.lower():
            word_count += 1
        new_dict.add(word, word_count)

for word in new_dict:
    print(f'{word.lower()}: ' + '*' * new_dict[word])


infile.close()