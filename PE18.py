# MIS 207

# This program translates a telephone number written in letters to an actual phone number

def phone_number(letter_form):
    final_num = ''
    for letter in letter_form:
        if letter in 'ABC':
            final_num += str(2)
        elif letter in 'DEF':
            final_num += str(3)
        elif letter in 'GHI':
            final_num += str(4)
        elif letter in 'JKL':
            final_num += str(5)
        elif letter in 'MNO':
            final_num += str(6)
        elif letter in 'PQRS':
            final_num += str(7)
        elif letter in 'TUV':
            final_num += str(8)
        elif letter in 'WXYZ':
            final_num += str(9)
        else:
            final_num += ''
    return final_num

print(phone_number('JACKNELSON'))
print(phone_number('IOWASTATE'))
print(phone_number('GUITAR'))
