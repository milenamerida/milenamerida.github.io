def CompAverage(s1,s2,s3):
    average = (s1 + s2 + s3) / 3
    handicap = (200 - average) * 0.9

    return average,handicap


print('Base score is set at 200 and handicap at 90%')
lastname = input('Enter last name: ')
s1 = int(input('Enter score for game 1: '))
s2 = int(input('Enter score for game 2: '))
s3 = int(input('Enter score for game 3: '))

average,handicap = CompAverage(s1,s2,s3)


print('Bowler {} has an average of {:.0f} and handicap of {:.0f}'.format(lastname,average,handicap))
