name = input('Enter your last name: ')
salary = float(input('Enter your salary $'))
level = int(input('Enter your job level: '))
if level >= 10:
  rate = 0.25
elif level >= 5:
  rate = 0.20
else:
  rate = 0.10
bonus = salary*rate
print('{} has a bonus of ${:.2f}'.format(name, bonus))
