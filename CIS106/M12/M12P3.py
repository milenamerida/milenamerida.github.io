def load(lastname, score):
    f = open("M12P3.txt", "r")
    for i in range (0,10,1):
        ln = f.readline()
        ln = ln.rstrip("\n")
        lastname.append(ln)
        s = f.readline()
        s.rstrip("\n")
        score.append(s)
    f.close()
    
def display(lastname, score):
    for i in range(0, 10, 1):
        print(lastname[i], 'has a score of ', score[i])

def hilow(lastname, score):
    high_var = 0
    high = 0
    low_var = 999
    low = 0
    
    for i in range(0, 10, 1):
        if score[i] > high_var:
            high_var = score
            high = i
        elif score[i] < low_var:
            low_var = score
            low = i    
        print(lastname[high], 'has highest score of ', score[high])
        print(lastname[low], 'has highest score of ', score[low])
    return lastname, score

lastname = []
score = []

load(lastname, score)
display(lastname, score)
hilow(lastname, score)
