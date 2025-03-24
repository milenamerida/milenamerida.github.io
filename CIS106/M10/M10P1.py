def ForecastPct(month,sales):
    if month == "jan":
        percent = 0.10
    elif month == "feb":
        percent = 0.10
    elif month == "mar":
        percent = 0.10
    elif month == "apr":
        percent = 0.15
    elif month == "may":
        percent = 0.15
    elif month == "jun":
        percent = 0.15
    elif month == "jul":
        percent = 0.20
    elif month == "aug":
        percent = 0.20
    elif month == "sep":
        percent = 0.20
    else:
        percent = 0.25

    forecastpct = sales*percent
    
    return forecastpct

prompt = input("Do you want to run this program? (Yes/No) ").lower()

if prompt == "no":
    print("Thank you, have a good day!")

else:
    while prompt == "yes":
        lastname = input("Enter last name: ")
        month = input("Enter month: ").lower()
        sales = int(input("Enter number of sales: "))

        forecastpct = ForecastPct(month,sales)
        
        nextmonth = sales * (1+forecastpct)

        print("Forecast for next month's sales is: {:.0f}".format(nextmonth))
        prompt = input("Do you want to run this program again? (Yes/No) ").lower()
