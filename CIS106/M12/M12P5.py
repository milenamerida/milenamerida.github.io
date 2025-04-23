def load():
    f = open("M12P4.txt", "r")
    lastname = []
    batave = []
    for i in range (0,10,1):
        ln = f.readline()
        ln = ln.rstrip("\n")
        lastname.append(ln)
        b = f.readline()
        b.rstrip("\n")
        batave.append(b)
    f.close()
    return lastname, batave

def searchname(slname):
    found = -1
    lastname, batave = load()
    for i in range(0, 10, 1):
        if lastname[i] == slname:
            found = i
    if found == -1:
        print(slname, ' not in the list')
    else:
        print(lastname[found], ' has average of ', batave[found])

prompt = input('Do you want to search for a last name? (Yes/No) ').lower()

while prompt == 'yes':
    slname = input('Enter the name to search for: ')
    searchname(slname)
    prompt = input('Do you want to search for a last name? (Yes/No) ').lower()
