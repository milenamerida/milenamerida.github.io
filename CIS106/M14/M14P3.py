class Student:
    def __init__(self, first, last, dcode, credit):
        self.first = first
        self.last = last
        self.dcode = dcode
        self.credit = credit

    def tuitionowed(self):
        if self.dcode == 'I':
            tuition = self.credit * 250
        elif self.dcode == 'X':
            tuition = self.credit * 800
        elif self.dcode == 'G':
            tuition = self.credit * 250
        else:
            tuition = self.credit * 500
        return tuition

stu1 = Student('Milena', 'Merida', 'I', 12)
stu2 = Student('John', 'Adams', 'O', 10)
stu3 = Student('Jessica', 'Brown', 'X', 14)
stu4 = Student('Lisa', 'Smith', 'G', 7)

print(stu1.last)
print(stu1.tuitionowed())
print(stu2.last)
print(stu2.tuitionowed())
print(stu3.last)
print(stu3.tuitionowed())
print(stu4.last)
print(stu4.tuitionowed())
