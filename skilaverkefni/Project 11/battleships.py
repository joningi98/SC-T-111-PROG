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
                    i, j = input("Enter location x, y: ").split()
                    x = int(i)
                    y = int(j)
                    self.row[x][y] = 'B'
                    print(self.__str__())
                placing_ships = False
            except IndexError:
                print("Please enter a correct input")

    def shoot(self):
        ships_destroyed = 0
        if ships_destroyed == 4:
            print("Victory")
            quit()
        while True:
            a, b = input("Enter the location to shoot: ").split()
            x = int(a)
            y = int(b)
            if self.row[x][y] == 'B':
                print("Hit!")
                ships_destroyed += 1
                self.row[x][y] = 'X'
                print(self.__str__())
                break
            if self.row[x][y] == 'O' or self.row[x][y] == 'X':
                print("Cannot fire, previous target selected!\nFind a new target sir")
            else:
                print("Miss!")
                self.row[x][y] = 'O'
                print(self.__str__())

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
    while game:
        p1.shoot()



main()
