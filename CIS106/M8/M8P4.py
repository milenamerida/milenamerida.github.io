f = open("M8P4.txt","r")

sumextprice = 0.0
count = 0
average = 0
noitem = 0

item = f.readline()

while item != "":
    qty = float(f.readline())
    price = float(f.readline())

    extprice = qty * price

    print("Item: {} Quantity ordered {:.0f} and extended price ${:.2f}".format(item, qty, extprice))

    noitem = noitem + 1
    count = count + qty
    average = count / noitem

    sumextprice = sumextprice + extprice

    item = f.readline()

print("Total extended price ${:.2f}, total number of orders {:.0f} and average order {:.0f}".format(sumextprice, count, average))
