def AssessedValue(county,mktvalue):
    if county == 'cook':
        percent = 0.90
    elif county == 'dupage':
        percent = 0.80
    elif county == 'mchenry':
        percent = 0.75
    elif county == 'kane':
        percent = 0.60
    else:
        percent = 0.70

    assessedvalue = mktvalue * percent
    
    return assessedvalue

totalmktvalue = 0
totalassessedvalue = 0

prompt = input('Do you want to run this program? (Yes/No): ').lower()

if prompt == 'no':
  print('Thank you, have a good day!')

else:
  while prompt == 'yes':
      county = input('Please enter county: ').lower()
      mktvalue = float(input('Please enter market value $'))

      assessedvalue = AssessedValue(county,mktvalue)

      totalmktvalue = totalmktvalue + mktvalue
      totalassessedvalue = totalassessedvalue + assessedvalue

      print('Assessed value for a home in {} county is ${:.2f}'.format(county,assessedvalue))
      print('Total market value is ${:.2f} and total assessed value is ${:.2f}'.format(totalmktvalue,totalassessedvalue))
      prompt = input('Do you want to run this program again? (Yes/No): ').lower()
