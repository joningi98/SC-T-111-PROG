class VendingMachine(object):
    def __init__(self, balance=0.0):
        self.balance = balance

    def nickel(self):
        self.balance += 0.05

    def dime(self):
        self.balance += 0.10

    def quarter(self):
        self.balance += 0.25

    def dollar(self):
        self.balance += 1.00

    def __str__(self):
        return self.balance


def main():
    v1 = VendingMachine()
    while True:
        print("A packet of candy costs $ 1.50. You have inserted $ {}.".format("%.2f" % v1.balance))
        print("Please insert coins:")
        print("\tn - Nickel\n\td - Dime\n\tq - Quarter\n\tD - Dollar")
        user_pick = input("")
        if user_pick == 'n':
            v1.nickel()
        elif user_pick == 'd':
            v1.dime()
        elif user_pick == 'q':
            v1.quarter()
        elif user_pick == 'D':
            v1.dollar()
        else:
            print("'{}' is not a valid coin.".format(user_pick))

        if v1.balance >= 1.50:
            change = v1.balance - 1.50
            print("Enjoy your candies. Your change is $ {}. Please visit again.".format("%.2f" % change))
            break


main()