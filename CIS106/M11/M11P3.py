def ComputeComm(sales):
    if sales > 100000:
        rate = 0.10
    else:
        rate = 0.05

    commission = sales * rate
    target = 0.05 * sales

    return commission,target

lastname = input('Enter last name: ')
sales = float(input('Enter total sales of last term: $'))

commission,target = ComputeComm(sales)

print("Salesperson: {}, commission for last term ${:.2f} and next year's target ${:.2f}".format(lastname,commission,target))
