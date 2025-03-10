f = open("M8P5.txt","r")

c = 0
totaltuition = 0.0

lastname = f.readline()

while lastname != "":
        dcode = f.readline()
        credits = float(f.readline())

        if dcode.rstrip("\n") == 'I':
                costpercredit = 250.00
        else:
                costpercredit = 500.00


        tuition = costpercredit * credits
        c = c + 1
        totaltuition = totaltuition + tuition

        print("Student {} is taking {:.0f} credits and owes ${:.2f} in tuition".format(lastname, credits, tuition))

        lastname = f.readline()

print("Total number of students: {} and total tuition owed ${:.2f}".format(c, totaltuition))

	
