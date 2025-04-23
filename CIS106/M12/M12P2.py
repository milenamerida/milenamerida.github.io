def display(lastname, score):
    for i in range(0, 10):
        print(lastname[i], 'has a score of ', score[i])


lastname = ['Smith', 'Brown', 'Green', 'White', 'Jones', 'Davis', 'Grant', 'Baker', 'Allen', 'Clark']
score = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]

display(lastname, score)
