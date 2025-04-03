def CompTotal(qty,price):
    global total
    total = qty * price
    global tax
    tax = 0.07 * total

    return


qty = int(input('Enter quantity of items: '))
price = float(input('Enter price per unit: $'))

CompTotal(qty,price)

print('Total is ${:.2f} and tax cost is ${:.2f}'.format(total,tax))
