def TrainTicket(miles):
    if miles >= 30:
        price = 12
    elif miles >= 20:
        price = 10
    elif miles >= 10:
        price = 8
    else:
        price = 5

    return price

totalprice = 0

prompt = input('Do you want to run this program? (Yes/No): ').lower()

if prompt == 'no':
  print('Thank you, have a good day!')

else:
  while prompt == 'yes':
      lastname = input("Enter last name: ")
      miles = int(input("Enter total miles from Chicago: "))

      price = TrainTicket(miles)

      totalprice = totalprice + price

      print("Your ticket price is ${:.2f}".format(price))
      print("Total tickets ${:.2f}".format(totalprice))
      prompt = input('Do you want to run this program again? (Yes/No): ').lower()
