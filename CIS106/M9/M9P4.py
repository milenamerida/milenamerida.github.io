def CompPayRate(code,hours):
    if code == 'L':
        rate = 25
        overtime = 25 * 1.5
    elif code == 'A':
        rate = 30
        overtime = 30 * 1.5
    elif code == 'J':
        rate = 50
        overtime = 50 * 1.5

    if hours > 40:
        grosspay = overtime * hours
    else:
        grosspay = rate * hours

    return grosspay


totalgrosspay = 0

prompt = input('Do you want to compute gross pay? (Yes/No) ').lower()

while prompt == 'yes':
    lastname = input('Enter last name: ')
    code = input('Enter job code (L, A or J): ')
    hours = float(input('Enter total hours worked: '))

    grosspay = CompPayRate(code,hours)

    totalgrosspay = totalgrosspay + grosspay

    print('Total gross pay for {} is ${:.2f}'.format(lastname,grosspay))
    prompt = input('Do you want to compute gross pay? (Yes/No) ').lower()

print('Total gross pay computed: ${:.2f}'.format(totalgrosspay))
