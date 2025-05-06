class Car:
    def __init__(self, make, model, price, disprice):
        self.make = make
        self.model = model
        self.price = price
        self.disprice = disprice

    def details(self):
        return '{}, {}, ${:.2f}'.format(self.make, self.model, self.price)


class Sportcar(Car):
    def option(self):
        if wheels == 'y':
            price = self.price + 1000
        elif engine == 'y':
            price = self.price + 3000
        elif interior == 'y':
            price = self.price + 2000
        else:
            price = self.price + 0
        return price

    def details(self):
        return '{}, {}, ${:.2f}'.format(self.make, self.model, self.price)

        
car1 = Car('Toyota', 'RAV4', 23000, 20700)
car2 = Car('Honda', 'CRV', 28000, 25200)
car3 = Sportcar('BMW', 'M5', 120000, 108000)
car4 = Sportcar('Mercedes Benz', 'S-Class', 118000, 106200)


wheels = input("Do you want to include sport wheels? (Y/N) ").lower()
engine = input("Do you want to include sport engine? (Y/N) ").lower()
interior = input("Do you want to include sport interior? (Y/N) ").lower()

print(car1.details())
print(car2.details())
print(car3.details())
print(car4.details())
