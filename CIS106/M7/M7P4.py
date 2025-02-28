prompt = input('Do you want to run this program? (Yes/No) ')
sum = 0
employees = 0
while prompt == 'Yes':
  lastname = input('Enter last name: ')
  hours = float(input('Enter hours worked: '))
  rate = float(input('Enter rate of pay: '))
  if hours > 40:
    rate = rate * 1.5
  pay = hours * rate
  print('Gross pay for {} is ${:.2f}'.format(lastname, pay))
  sum = sum + pay
  employees = employees + 1
  prompt = input('Do you want to run this program again? (Yes/No) ')
average = sum / employees
print('Sum of all gross pay is ${:.2f}, number of employees is {:.0f} and average gross pay is ${:.2f}'.format(sum, employees, average))
