f = open("M8P3.txt","r")
lastname = f.readline()
addbonus = 0
while lastname != "":
        salary = float(f.readline())
        if salary >= 100000:
                rate = 0.2
        elif salary > 50000:
                rate = 0.15
        else:
                rate = 0.10
        bonus = salary*rate
        print('Employee {} Salary ${:.2f} and bonus ${:.2f}'.format(lastname,salary,bonus))
        addbonus = addbonus + bonus
        lastname = f.readline()
print('Total bonuses paid out ${:.2f}'.format(addbonus))
        
