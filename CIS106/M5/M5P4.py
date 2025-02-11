name = input('Enter the name of the appliance: ')
cost = float(input('Enter the cost of the appliance $'))
if cost > 1000:
  warranty = cost*0.1
else:
  warranty = cost*0.05
total = cost+warranty
print('The cost for {} is ${:.2f}. The warranty is ${:.2f} and the total is ${:.2f}'.format(name,cost,warranty,total))
