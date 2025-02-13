itemqty = int(input('Enter the quantity: '))
if itemqty > 1000:
  unitprice = 3.00
  price = itemqty * unitprice
else:
  unitprice = 5.00
  price = itemqty * unitprice
tax = 0.07 * price
total = price + tax
print('Quantity {}, unit price ${:.2f}, extended price ${:.2f}, tax ${:.2f} and total ${:.2f}'.format(itemqty,unitprice,price,tax,total))
