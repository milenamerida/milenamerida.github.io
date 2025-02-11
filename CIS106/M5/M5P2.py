item = input('Enter the item: ')
qty = int(input('Enter the quantity: '))
if item == "A":
  unitprice = 10.00
else:
  unitprice = 20.00
extprice = qty*unitprice
print('Item {}, unit price ${:.2f} and extended price ${:.2f}'.format(item,unitprice,extprice))
