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
        '''bonusrate = float(input("Enter bonus rate: "))'''
        bonusrate = 0.10
        bonus = bonusrate * self.pay
        return bonus

class Manager(Employee):
    def longbonus(self):
        bonusrate = 0.4
        bonus = self.pay + bonusrate
        return bonus


emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('John', 'Smith', 60000)
emp3 = Manager('Monica', 'Geller', 100000)
emp4 = Manager('Rachel', 'Green', 90000)


print(emp1.fullname())
print(emp1.bonus())
print(emp2.fullname())
print(emp2.bonus())
print(emp3.fullname())
print(emp3.bonus())
print(emp4.fullname())
print(emp4.bonus())


