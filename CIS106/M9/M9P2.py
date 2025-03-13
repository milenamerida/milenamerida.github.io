def CompBatAve(hits,bats):
    average = hits / bats

    return average

numplayers = 0

prompt = input("Do you want to compute player's average? (Yes/No) ").lower()

while prompt == 'yes':
    lastname = input("Enter player's last name: ")
    hits = int(input('Enter number of hits: '))
    bats = int(input('Enter number of at bats: '))

    average = CompBatAve(hits,bats)

    numplayers = numplayers + 1

    print('Player {} has a batting average of {:.0f}'.format(lastname,average))
    prompt = input("Do you want to compute next player's average? (Yes/No) ").lower()

print('Total number of players entered is: {}'.format(numplayers))
    
