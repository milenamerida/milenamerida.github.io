def CompTuition(credit,code):
    if code == 'I':
        charge = 250.00
    elif code == 'O':
        charge = 500.00

    tuition = credit * charge

    return tuition

totaltuition = 0

prompt = input('Do you want to compute tuition owed? (Yes/No) ').lower()

while prompt == 'yes':
    lastname = input('Enter last name: ')
    credit = int(input('Enter total credit hours: '))
    code = input('Enter district code: (I or O) ')

    tuition = CompTuition(credit,code)

    totaltuition = totaltuition + tuition

    print('Tuition owed for {} is ${:.2f}'.format(lastname,tuition))
    prompt = input('Do you want to compute tuition owed? (Yes/No) ').lower()

print('Total tuition owed is ${:.2f}'.format(totaltuition))
