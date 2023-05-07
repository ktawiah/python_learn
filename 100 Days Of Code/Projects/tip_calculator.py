print('Welcome to the tip calculator')
total_payment = float(input('What was the total bill? $'))
tip = int(input('What percentage of tip would you like to give? 10, 12, or 15? '))
while tip not in [10, 12, 15]:
	tip = int(input('Tip must be either 15, 12 or 15. Enter new tip. '))
people = int(input('How many people are to split the bill? '))
print(f'Each person should pay: {round(total_payment * (1 + tip/100) / people, 2)}')
