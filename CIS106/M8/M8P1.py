prompt = input("Do you want to calculate interest? (Yes/No)")

if prompt == "No":
    print("Thank you. Have a good day!")
while prompt == "Yes":
    startamount = float(input('Enter the principle amount: '))
    rate = float(input('Enter the interest rate: '))
    totalinterest = 0

    print("Year", "     Beginning Balance     ", "End Balance")
    for count in range(1,6,1):
        interest = startamount * rate
        endbalance = startamount + interest
        print(" {}           {:.2f}             {:.2f}".format(count, startamount, endbalance))
        startamount = endbalance
        totalinterest = totalinterest+interest
    print("Total interest earned: ${:.2f}".format(totalinterest))
    prompt = input("Do you want to calculate interest again? (Yes/No)")
