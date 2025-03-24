def OutDoorPrice(msrp,model,ev):
    if model == "accord":
        percentoff = 0.1
    elif model == "rav4":
        percentoff = 0.15
    elif ev == "y":
        percentoff = 0.30
    else:
        percentoff = 0.05

    discount = msrp * percentoff
    outdoorprice = msrp - discount

    return outdoorprice

totalmsrp = 0
totalsales = 0

prompt = input('Do you want to run this program? (Yes/No): ').lower()

if prompt == 'no':
  print('Thank you, have a good day!')

else:
  while prompt == 'yes':
      make = input("Enter the make of the car: ")
      model = input("Enter the model of the car: ").lower()
      ev = input("Is it an electric vehicle? (Y/N) ").lower()
      msrp = float(input("Enter MSRP $"))
      
      outdoorprice = OutDoorPrice(msrp,model,ev)

      tax = outdoorprice * 0.07
      total = outdoorprice + tax

      totalmsrp = totalmsrp + msrp
      totalsales = totalsales + total

      print("Final price for this vehicle is ${:.2f}".format(total))
      print("Total MSRP is ${:.2f} and total sales is ${:.2f}".format(totalmsrp,totalsales))
      prompt = input('Do you want to run this program again? (Yes/No): ').lower()
