import random


class Board(object):
    def __init__(self, size):
        self.board_size = size
        self.row = []

        for x in range(0, self.board_size):
            row = [0] * size
            self.row.append(row)

    def place_ship(self):
        placing_ships = True
        while placing_ships:
            try:
                for a in range(4):
                    x = random.randint(0, 4)
                    y = random.randint(0, 4)
                    self.row[x][y] = 'B'
                placing_ships = False
            except IndexError:
                print("Please enter a correct input")

    def shoot(self):
        while True:
            a, b = input("Enter the location to shoot: ").split()
            x = int(a)
            y = int(b)
            if self.row[x][y] == 'B':
                print("Hit!")
                self.row[x][y] = 'X'
                print(self.__str__())
                break
            if self.row[x][y] == 'O' or self.row[x][y] == 'X':
                print("Cannot fire, previous target selected!\nFind a new target sir")
            else:
                print("Miss!")
                self.row[x][y] = 'O'
                print(self.__str__())

    def check_victory(self):
        if 'B' not in self.__str__():
            print("\nVictory!\n")
            quit()

    def __str__(self):
        s = ''
        for x in range(self.board_size):
            for y in range(self.board_size):
                if self.row[x][y] == 0:
                    s += "{:<2s}".format(".")
                else:
                    s += "{:<2s}".format(str(self.row[x][y]))
            s += '\n'
        return s


def main():
    game = True
    p1 = Board(5)
    p1.place_ship()
    print(p1)
    while game:
        p1.shoot()
        p1.check_victory()



main()
