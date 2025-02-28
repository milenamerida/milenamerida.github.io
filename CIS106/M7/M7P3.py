prompt = input('Do you want to run this program? (yes/no) ')
  while prompt == 'yes':
    lastname = input('Enter last name: ')
    score1 = int(input('Enter first score: '))
    score2 = int(input('Enter second score: '))
    average = (score1 + score2) / 2
    print('Average for {} is {:.0f}'.format(lastname, average))
    prompt = input('Do you want to run this program again? (yes/no) ')
