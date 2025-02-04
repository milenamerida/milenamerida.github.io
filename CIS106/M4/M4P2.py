# If statements used from https://www.w3schools.com/python/python_conditions.asp + help from Professor Hull

purchasep = float(input('Enter purchase price per share $'))
stockp = float(input('Enter the current price per share $'))
qtystock = int(input('Enter quantity of shares purchased: '))
value = (stockp - purchasep) * qtystock
if value < 0:
  print('You are losing money! You lost ${:,.2f}'.format(value))
else: 
  print('Congratulations! You are making money off of your stocks! You earned ${:,.2f}'.format(value))
