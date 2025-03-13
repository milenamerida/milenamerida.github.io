def CompTotal(qty,price):
    total = qty*price

    if total > 10000.00:
        discount = total * 0.1
    else:
        discount = 0.0

    total = total - discount
    
    return total

totalextprice = 0

prompt = input('Do you want to compute the total price? (Yes/No) ').lower()

while prompt == 'yes':
    qty = int(input('Enter the quantity of items: '))
    price = float(input('Enter the unit price $'))

    total = CompTotal(qty,price)

    totalextprice = totalextprice + total
    
    print('Total is ${:.2f}'.format(total))
    prompt = input('Do you want to compute the total price? (Yes/No) ').lower()

print('Total extended price is ${:.2f}'.format(totalextprice))
