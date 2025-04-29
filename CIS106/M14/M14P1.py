class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
        '''print(emp1.fullname()) print with () because it's a method'''

    def bonus(self):
        bonusrate = float(input("Enter bonus rate: "))
        bonus = bonusrate * self.pay
        return bonus

emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Test', 'User', 60000)


print(emp1.fullname())
print(emp1.bonus())
print(emp2.fullname())
print(emp2.bonus())

