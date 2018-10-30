class Vehicle(object):
    def __init__(self, number='', year=0):
        self.license = number
        self.year = year
        self.weight = 0.00
        self.fee = 0.00
        self.cc = 0
        self.weight = 0.00

    def set_CC(self, pw):
        self.cc = pw
        if self.cc < 50:
            self.fee = 10
        elif 50 <= self.cc < 200:
            self.fee = 0

    def set_weight(self, num):
        self.weight = num
        if self.weight < 3000:
            self.fee = 30
        elif 3000 <= self.weight < 5000:
            self.fee = 40
        else:
            self.fee = 50

    def __str__(self):
        return "Vehicle: {} {} Weight={} Fee=${}".format(self.license, self.year, ("%.2f" % self.weight),
                                                         ("%.2f" % self.fee))


class Car(Vehicle):
    def __str__(self):
        return "Car: {} {} {} Weight={} Fee=${}".format(self.license, self.year, self.style, ("%.2f" % self.weight),
                                                        ("%.2f" % self.fee))


class Truck(Vehicle):
    def __str__(self):
        return "Truck: {} {} {} wheels Weight={} Fee=${}".format(self.license, self.year, self.wheels,
                                                                 ("%.2f" % self.weight), ("%.2f" % self.fee))


class Motorbike(Vehicle):

    def __str__(self):
        return "Motorbike: {} {} {} cc Fee=${}".format(self.license, self.year, self.cc, ("%.2f" % self.fee))


v1 = Vehicle("AB 123", 2010)
# c1 = Car("SF 735", 2007, "Station")
# t1 = Truck("TU 765", 1994, 6)
b1 = Motorbike("XY 666", 2005)

# Car: SF 735 2007 Station Weight=3500.00 Fee=$40.00
# Truck: TU 765 1994 6 wheels Weight=9000.00 Fee=$60.00
# Motorbike: XY 666 2005 250 cc Fee=$35.00
v1.set_weight(3500)
# t1.set_weight(9000)
b1.set_CC(250)
print(v1)
print(b1)
# print(t1)
# print(c1)
# print(c1)
