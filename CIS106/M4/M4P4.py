name = input('Enter your name: ')
steps = int(input('Enter the total steps walked today: '))
calburned = steps * 0.25
print('The amount of calories {} burned today was {:,.0f}'.format(name,calburned))
