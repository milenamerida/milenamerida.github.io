itemqty = int(input('Enter the quantity: '))
if itemqty > 1000:
  price = itemqty * 3
else:
  price = itemqty * 5
tax = 0.07 * price
total = price + tax
print('Quantity {}, extended price ${:.2f}, tax ${:.2f} and total ${:.2f}'.format(itemqty,price,tax,total))
