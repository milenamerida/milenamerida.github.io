prompt = input('Do you want to run this program? (Yes/No) ')
sum = 0
while prompt == 'Yes':
  qty = int(input('Enter the quantity of the item: '))
  price = float(input('Enter the price of the item: '))
  extprice = qty * price
  if extprice > 10000.00:
    discount = 0.25
  else:
    discount = 0.10
  disamount = extprice * discount
  sum = sum + disamount
  total = extprice - disamount
  print('Extended price ${:.2f}, discount amount ${:.2f} and total ${:.2f}'.format(extprice, disamount, total))
  prompt = input('Do you want to run this program again? (Yes/No) ')
print('Total discount amount ${:.2f}'.format(sum))
