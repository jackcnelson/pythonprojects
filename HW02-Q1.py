
#MIS 207 HW02 Q1
#This program is a simple interest rate calculator

#Present value prompt
pv = float(input("What is the value of your current investment?"))

#Expected rate of return prompt
err = float(input("What is your expected rate of return per year? Enter this percentage in decimal format."))

#Number of year prompt
years = float(input("How many years will you hold this investment?"))

#Future value calculation
future_value = pv * ((1 + err) ** years)

print(f'The future value of your investment is: {future_value: ,.2f}')
