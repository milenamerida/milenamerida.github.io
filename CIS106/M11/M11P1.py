def ComputeDiscount(qty,price,rate):
    extprice = qty * price
    discamount = extprice * rate
    discprice = extprice - discamount

    return discamount,discprice



qty = int(input('Enter the quantity: '))
price = float(input('Enter the price $: '))
rate = float(input('Enter the discount rate %" '))

discamount,discprice = ComputeDiscount(qty,price,rate)


print('Quantity of items: {}, price per item ${:.2f}, discount amount ${:.2f} and discounted price ${:.2f}'.format(qty,price,discamount,discprice))
