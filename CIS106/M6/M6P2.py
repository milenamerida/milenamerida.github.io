partnumber = int(input("Enter the part number: "))
qty = int(input("Enter the quantity: "))
if partnumber == 10 or partnumber == 55:
  unitprice = 1.00
  total = qty * unitprice
elif partnumber == 99:
  unitprice = 2.00
  total = qty * unitprice
elif partnumber == 80 or partnumber == 70:
  unitprice = 3.00
  total = qty * unitprice
else:
  unitprice = 5.00
  total = qty * unitprice
print("Part number: {}, unit price ${:.2f} and total ${:.2f}".format(partnumber, unitprice, total))
