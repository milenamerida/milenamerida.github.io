from tkinter import *

root = Tk()
root.title("Grade Average Calculator")
root.geometry('350x200')

def GradeData():
    
    def grade_average():
        average = (float(grade1.get()) + float(grade2.get()))/2
        ave.set(average)

    grade1 = StringVar()
    grade2 = StringVar()
    ave = StringVar()

    Label(root, text="Enter first grade:").grid(column=1, row=0)
    Label(root, text="Enter second grade:").grid(column=1, row=1)
    Label(root, text="Average Score:").grid(column=1, row=3)

    Entry(root, textvariable=grade1).grid(column=2, row=0)
    Entry(root, textvariable=grade2).grid(column=2, row=1)
    Entry(root, textvariable=ave).grid(column=2, row=3)

    button = Button(root, text="Calculate", fg="blue", command=grade_average)
    button.grid(column=2, row=2)

    root.mainloop()
    return grade1.get(), grade2.get(), ave.get()

grade1, grade2, ave = GradeData()
print("First Grade: {}, Second Grade: {} and Average: {}.".format(grade1, grade2, ave))

f = open("myfile.txt", "x")
