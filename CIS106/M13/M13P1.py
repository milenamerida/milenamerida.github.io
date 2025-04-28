students = {"Jones":90, "Adams":87, "Johnson":100, "Smith":93, "Brown":98}

names = list(students.keys())
scores = list(students.values())
print("{:<10} {:<10}".format("Name", "Grade"))
for i in range(len(students)):
    print("{:<10} {:<10}".format(names[i], scores[i]))

print()
print("Class average", sum(scores)/len(scores))


'''Format of table found in: https://www.geeksforgeeks.org/python-program-to-print-the-dictionary-in-table-format/'''
