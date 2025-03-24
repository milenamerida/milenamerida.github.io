import math

def SqrFoot(length, width, height):
  wallsqrft = 2 * (length * height) + 2 * (width * height)
  
  return wallsqrft

def Gallons(wallsqrft):
  gallons = wallsqrft / 50
  
  return gallons

def AreaCeilFloor(length,width):
  areaceilfloor = length * width

  return areaceilfloor

prompt = input('Do you want to run this program? (Yes/No): ').lower()

if prompt == 'no':
  print('Thank you, have a good day!')

else:
  while prompt == 'yes':
    length = float(input('Enter the length of the room: '))
    width = float(input('Enter the width of the room: '))
    height = float(input('Enter the height of the room: '))

    wallsqrft = SqrFoot(length, width, height)
    gallons = Gallons(wallsqrft)

    print('The number of gallons of paint needed is: ', math.ceil(gallons))

    bonus = input('Are you painting your ceiling or varnishing your floor? (Yes/No): ').lower()
    if bonus == 'yes':
      areaceilfloor = AreaCeilFloor(length,width)
      bonusgallon = areaceilfloor / 50
      print('You will need ', math.ceil(bonusgallon), 'gallons for paint/varnish')
      prompt = input('Do you want to run this program again? (Yes/No): ').lower()
    else:
      prompt = input('Do you want to run this program again? (Yes/No): ').lower()
