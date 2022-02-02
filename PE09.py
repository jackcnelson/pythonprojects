
#MIS 207 PE09

#This program computes the state of water given the temperature

#User prompt
print('\nThis program determines the state of H2O given its temperature. \n')

#Input statement
water_temperature = float(input('What is the H2O\'s temperature? \n'))

#If/elif/else statements to determine water state
if water_temperature > 212:
    print('The H2O is in a gaseous state (steam) at this temperature.')
elif water_temperature >= 32:
    print('The H2O is in a liquid state (water) at this temperature.')
else:
    print('The H2O is in a solid state (ice) at this temperature.')


