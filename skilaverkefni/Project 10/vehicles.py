class Vehicle(object):
    def __init__(self, number='', year=0):
        self.license = number
        self.year = year
        self.weight = 0.00
        self.fee = 0.00

    def get

    def __str__(self):
        return "Vehicle: {} {} Weight={} Fee=${}".format(self.license, self.year, ("%.2f" % self.weight), ("%.2f" % self.fee))


class Car(Vehicle):
    def __init__(self, number='', year=0, style=''):
        super().__init__(number, year)
        self.style = style

    def set_weight(self, num):
        self.weight = num
        if self.weight < 3000:
            self.fee = 30
        elif 3000 <= self.weight < 5000:
            self.fee = 40
        else:
            self.fee = 50

    def get_weight(self):
        return self.weight

    def __str__(self):
        return "Car: {} {} {} Weight={} Fee=${}".format(self.license, self.year, self.style, ("%.2f" % self.weight), ("%.2f" % self.fee))


class Truck(Vehicle):
    def __init__(self, number='', year=0, wheels=0):
        super().__init__(number, year)
        self.wheels = wheels

    def set_weight(self, num):
        self.weight = num
        if 3000 <= self.weight < 5000:
            self.fee = 40
        elif 5000 <= self.weight < 10000:
            self.fee = 60
        else:
            self.fee = 70

    def get_fee(self):
        return self.fee

    def __str__(self):
        return "Truck: {} {} {} wheels Weight={} Fee=${}".format(self.license, self.year, self.wheels,
                                                                 ("%.2f" % self.weight), ("%.2f" % self.fee))


class Motorbike(Vehicle):
    def __init__(self, number='', year=0):
        super().__init__(number, year)
        self.cc = 0

    def set_CC(self, pw):
        self.cc = pw
        if self.cc < 50:
            self.fee = 10
        elif 50 <= self.cc < 200:
            self.fee = 20
        else:
            self.fee = 35

    def get_CC(self):
        return self.cc

    def __str__(self):
        return "Motorbike: {} {} {} cc Fee=${}".format(self.license, self.year, self.cc, ("%.2f" % self.fee))


def main():
    # Create some vehicles
    v1 = Vehicle("AB 123", 2010)
    c1 = Car("SF 735", 2007, "Station")
    t1 = Truck("TU 765", 1994, 6)
    b1 = Motorbike("XY 666", 2005)
    c1.set_weight(3500)
    t1.set_weight(9000)
    b1.set_CC(250)
    # Print info
    print(v1)
    print(c1)
    print("The weight of the car is: {:.2f}".format(c1.get_weight()))
    print(t1)
    print("The fee for the truck is: {:.2f}".format(t1.get_fee()))
    print(b1)
    print("The CC of the bike is: {:.2f}".format(b1.get_CC()))
    print()
    # Put the four vehicles into a list.
    # Then loop through the list and call the print function for each of the
    # vehicles.
    # You have to implement this part of the main program!
    # YOUR CODE GOES HERE

    vehicle_list = [v1, c1, t1, b1]
    for x in vehicle_list:
        print(x)

    v1 = c1
    print(v1)
    print()


main()
