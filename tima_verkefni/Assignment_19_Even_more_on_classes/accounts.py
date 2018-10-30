
class Account(object):
    percent = 0
    bonus = 0

    def __init__(self, balance):
        self.balance = balance

    def update_balance(self):
        if self.bonus != 0:
            new_balance = self.balance*self.percent
            self.balance = new_balance + self.balance*self.bonus
        else:
            self.balance = self.balance*self.percent

    def __str__(self):
        return str("Balance: {}".format("%.2f" % self.balance))


class SavingsAccount(Account):
    percent = 0.05
    bonus = 1.1


class DebitAccount(Account):
    percent = 1.02


def print_accounts(accounts):
    for x in accounts:
        print(x)


def update_accounts(accounts):
    for x in accounts:
        x.update_balance()


def main():
    s1 = SavingsAccount(1000)
    d1 = DebitAccount(1000)
    s2 = SavingsAccount(2000)
    d2 = DebitAccount(4000)

    accounts = [s1, d1, s2, d2]

    print_accounts(accounts)
    update_accounts(accounts)

    print_accounts(accounts)
    update_accounts(accounts)

    print_accounts(accounts)
    update_accounts(accounts)

main()