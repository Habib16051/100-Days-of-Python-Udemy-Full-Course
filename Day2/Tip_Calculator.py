print('Welcome to the tip calculator!\n')
bill = float(input('What was the total bill? $\n'))
tip = int(input('How much tip would you like to give? 10, 12, or 15?\n'))

people = int(input('How many people to split the bill?\n'))

tip_wit_bill = tip / 100 * bill + bill

print('Each person should pay: $', round((tip_wit_bill/people), 2))
