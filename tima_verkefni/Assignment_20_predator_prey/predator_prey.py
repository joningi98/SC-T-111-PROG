import random


class Island(object):

    def __init__(self, size, number_of_predators=0, number_of_preys=0):
        self.grid_size = size
        self.grid = []

        for x in range(0, size):
            row = [0] * size
            self.grid.append(row)

        self.populate_island(number_of_predators, number_of_preys)

    def __str__(self):
        s = ''
        for j in range(self.grid_size - 1, -1, -1):
            for i in range(self.grid_size):
                if self.grid[i][j] == 0:
                    s += "{:<2s}".format(".")
                else:
                    s += "{:<2s}".format(str(self.grid[i][j]))
            s += '\n'
        return s

    def set_animal_on_island(self, animal):
        self.grid[animal.x][animal.y] = animal

    def empty_cell(self, x, y):
        return self.grid[x][y] == 0

    def populate_island(self, number_of_predators, number_of_preys):
        counter = 0
        while counter < number_of_predators:
            x = random.randint(0, self.grid_size-1)
            y = random.randint(0, self.grid_size-1)

            if self.empty_cell(x, y):
                new_predator = Predator(self, x, y)
                self.set_animal_on_island(new_predator)
                counter += 1

        counter = 0
        while counter < number_of_preys:
            x = random.randint(0, self.grid_size-1)
            y = random.randint(0, self.grid_size-1)

            if self.empty_cell(x, y):
                new_prey = Prey(self, x, y)
                self.set_animal_on_island(new_prey)
                counter += 1
###############################################################
###############################################################


class Animal(object):

    def __init__(self, island, x=0, y=0, name="A"):
        self.island = island
        self.x = x
        self.y = y
        self.name = name

    def __str__(self):
        return self.name


###############################################################
###############################################################

class Predator(Animal):
    def __init__(self, island, x=0, y=0, name="P"):
        Animal.__init__(self, island, x, y, name)


###############################################################
###############################################################

class Prey(Animal):
    def __init__(self, island, x=0, y=0, name="B"):
        Animal.__init__(self, island, x, y, name)


def main():
    tenerife = Island(5, 3, 4)
    print(tenerife)

    man = Animal(tenerife, 2, 1)
    tenerife.set_animal_on_island(man)

    bengal_tiger = Predator(tenerife, 3, 1)
    tenerife.set_animal_on_island(bengal_tiger)

    print(tenerife)


main()
