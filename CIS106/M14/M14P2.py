class Student:
    def __init__(self, first, last, dcode, credit):
        self.first = first
        self.last = last
        self.dcode = dcode
        self.credit = credit

    def tuitionowed(self):
        if self.dcode == 'I':
            tuition = self.credit * 250
        else:
            tuition = self.credit * 500
        return tuition

stu1 = Student('Milena', 'Merida', 'I', 12)

print(stu1.last)
print(stu1.tuitionowed())
