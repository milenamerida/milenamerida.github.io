cd = float(input('Enter the amount of CD: '))
year = int(input('Enter the year to maturity of CD: '))
if cd > 100000 and year == 5:
  interest = 0.06
elif cd >= 50000 and year == 10:
  interest = 0.05
elif cd >= 50000 and year == 5:
  interest = 0.04
else:
  interest = 0.02
total = cd*interest
percent = interest*100
print('CD: ${:.2f}, interest rate {:.0f}% and interest amount for first year ${:.2f}'.format(cd, percent, total))
  
