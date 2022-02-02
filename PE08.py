
#MIS 207 PE08

#This program determines whether or not the swams will be mating in March

#User input
march_temperature = float(input('What has been the average march temperature? '))

#If statement to determine temperature and whether or not the cyclones won against Iowa
if march_temperature < 60:
    cyclone_performance = input('Did the Cyclones win against Iowa last season? Enter \'y\' if they won or \'n\' if they lost. ')
    if cyclone_performance == 'y':
        print('The swans will be mating!')
    else:
        print('The swans will not be mating.')
else:
    print('The swans will be mating!')
