# MIS 207 PE27
#
# Create an test a function called input_float

def input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except:
            print('ERROR: Please enter a valid float number.')

number = input_float('Please enter a floating point value: ')
print(number)