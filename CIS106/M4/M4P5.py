fixedcost = float(input('Enter fixed cost $'))
unitprice = float(input('Enter price per unit $'))
unitcost = float(input('Enter cost per unit $'))
breakeven = fixedcost / (unitprice - unitcost)
print('The break-even point of your business is ${:,.2f}'.format(breakeven))
