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

lastname, batave = load()
for i in range(0,10,1):
    print("{:<13} {:<10}".format(lastname[i], batave[i]))
