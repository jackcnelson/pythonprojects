####################
#MIS 207

#This program takes a user's string input and prints attributes of the string

#User text prompt
user_text = input('Please enter text. ')

#Making user text all lowercase in order to make easier determinations about the string
user_text_lower = user_text.lower()

#Determining how many times the word "the" appears in the string
print('The word \"the\" appears in this text ' + str(user_text_lower.count('the')) + ' times.')

#Determining if the word "apple" appears in the string
if "apple" in user_text_lower:
    print('The word \"apple\" is in this text.')
else:
    print('The word \"apple\" is not in this text.')

#Printing user text in uppercase and lowercase

print(user_text.upper())

print(user_text.lower())
