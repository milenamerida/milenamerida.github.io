name = input('Enter your last name: ')
dependents = int(input('Enter the number of dependents: '))
gross = float(input('Enter gross income $'))
adjgross = gross-dependents*12000
if gross > 50000:
  tax = 0.2
else:
  tax = 0.1
incometax = adjgross*tax
if incometax < 0:
  tax = 100
else:
  incometax = adjgross*tax
print('User {}, gross income ${:.2f}, number of dependents: {}.'.format(name,gross,dependents))
print('Adjusted gross income ${:.2f} and income tax ${:.2f}'.format(adjgross,incometax))
