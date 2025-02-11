numbooks = int(input('Enter the number of books ordered: '))
cost = float(input('Enter the cost per book $'))
total = numbooks * cost
if total > 50.00:
  shipping = 0
else:
  shipping = 25
print('The order total is ${:.2f} and the shipping is ${:.2f}'.format(total,shipping))
