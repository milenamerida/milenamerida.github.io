def CompMPG(miles,gallon):
    mpg = miles / gallon

    return mpg

numtrips = 0

prompt = input('Do you want to compute miles per gallon? (Yes/No) ').lower()

while prompt == 'yes':
    destiny = input('Enter destination city: ')
    miles = float(input('Enter total miles traveled: '))
    gallon = float(input('Enter total gallons used for the trip: '))

    mpg = CompMPG(miles,gallon)

    numtrips = numtrips + 1

    print('Average miles per gallon on the trip to {} is {:.1f}'.format(destiny,mpg))
    prompt = input('Do you want to compute miles per gallon? (Yes/No) ').lower()

print('Total trips entered: {}'.format(numtrips))    
    
