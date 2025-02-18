ticket = int(input('Enter the number of tickets: '))
if ticket >= 25:
  price = 50.00
elif ticket >= 10:
  price = 60.00
elif ticket >= 5:
  price = 70.00
else:
  price = 75.00
total = ticket*price
print('Number of tickets {}, price per ticket ${:.2f} and total cost ${:.2f}'.format(ticket, price, total))
