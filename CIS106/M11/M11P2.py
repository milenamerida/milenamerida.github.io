def ComputePoints(p1,p2,p3):
    total = p1 + p2 + p3
    average = total / 3

    return total,average

lastname = input("Enter student's last name: ")
p1 = float(input('Enter first grade: '))
p2 = float(input('Enter second grade: '))
p3 = float(input('Enter third grade: '))

total,average = ComputePoints(p1,p2,p3)

print('Student: {}, total points {:.1f} and average score {:.1f}'.format(lastname,total,average))

