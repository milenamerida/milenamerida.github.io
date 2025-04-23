def display(lastname):
    for i in range(0, 10):
        print(lastname[i])

def reversedisplay(lastname):
    for i in range(9, -1, -1):
        print(lastname[i])

lastname = ['Smith', 'Brown', 'Green', 'White', 'Jones', 'Davis', 'Grant', 'Baker', 'Allen', 'Clark']

display(lastname)
print("\n")
reversedisplay(lastname)
