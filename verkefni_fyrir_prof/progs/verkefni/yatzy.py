import random


class Dice:
    def __init__(self):
        self.number = 0

    def throw(self):
        self.number = random.randint(1, 6)
        return self.number


class DiceThrower:
    def __init__(self, how_many=5):
        self.number_of_dice = how_many
        self.dice_list = [-1 for i in range(self.number_of_dice)]
        self.__dice_class = Dice()

    def throw(self):
        for x in range(0, self.number_of_dice):
            self.dice_list[x] = self.__dice_class.throw()
        return self.dice_list

    def rethrow(self, rethrow_list=[]):
        for item in rethrow_list:
            self.dice_list[item] = self.__dice_class.throw()
        return self.dice_list


def main_menu():
    print("1: New game\n2: Quit")
    user_input = input('Enter your choice(1/2)please: ')

    if user_input == '1':
        return True
    else:
        return False


def print_sheet(yatzy_sheet):
    print("0: Small Row {}".format(yatzy_sheet[0]))
    print("1: Big Row {}".format(yatzy_sheet[1]))
    print("2: Full House {}".format(yatzy_sheet[2]))
    print("3: Chance {}".format(yatzy_sheet[3]))
    print("4: Yatzy {}".format(yatzy_sheet[4]))


def dice_menu(dice_thrower):
    still_throwing = True
    number_of_throws = 0

    while still_throwing:
        user_dice = dice_thrower.throw()
        number_of_throws += 1
        rethrowing_allowed = True

        print(user_dice)

        while rethrowing_allowed:
            rethrow = input('Do you want to Rethrow? (Y/N): ').upper()
            if rethrow == 'Y':
                s = input("Enter the dices you want to rethrow (0 - 4) space between please: ")
                dice = s.split()
                rethrow_dice = [eval(x) for x in dice]

                user_dice = dice_thrower.rethrow(rethrow_dice)
                number_of_throws += 1

                print(user_dice)
            else:
                rethrowing_allowed = False

            if number_of_throws == 3:
                rethrowing_allowed = False

        still_throwing = False
    return user_dice


def sheet_menu(dice, yatzy_sheet):
    print_sheet(yatzy_sheet)
    user_input = int(input('Enter your choice(0 - 4)please: '))
    yatzy_sheet[user_input] = sum(dice)
    print_sheet(yatzy_sheet)


def main():
    # Do not change this code
    dt = DiceThrower()
    sheet = [0, 0, 0, 0, 0]
    game_is_on = main_menu()

    while game_is_on:
        for i in range(0, 5):
            dice = dice_menu(dt)
            sheet_menu(dice, sheet)

        print('Final Score', sum(sheet))
        game_is_on = main_menu()


main()
