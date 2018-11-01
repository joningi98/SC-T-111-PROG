class Island:

    def __init__(self, size):
        self.grid_size = size
        self.grid = []

        for x in range(0, size):
            row = [0] * size
            self.grid.append(row)

    def __str__(self):
        s = ''
        for j in range(self.grid_size - 1, -1, -1):
            for i in range(self.grid_size):
                if self.grid[j][i] == 0:
                    s += '{:<2s}'.format('.')
                else:
                    s += '{:<2s}'.format(self.grid[j][i])
            s += '\n'
        return s

    def set_animal_on_island(self, animal):
        self.grid_size[animal.x][animal.y] = animal


class Animal:

    def __init__(self, island, x=0, y=0, name='A'):
        self.island = island
        self.x = x
        self.y = y
        self.name = name

    def __str__(self):
        return self.name


def main():
    tenerife = Island(5)
    print(tenerife)
    monkey = Animal(tenerife, 2, 1, 'M')
    tenerife.set_animal_on_island(monkey)


main()
