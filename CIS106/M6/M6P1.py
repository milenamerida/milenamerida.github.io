widget = int(input('Enter the quantity of widgets: '))
if widget > 10000:
  price = 10.00
elif widget >= 5000:
  price = 20.00
else:
  price = 30.00
extprice = widget*price
tax = extprice*0.07
total = tax+extprice
print('Extended price ${:.2f}, tax amount ${:.2f} and total ${:.2f}'.format(extprice, tax, total))
