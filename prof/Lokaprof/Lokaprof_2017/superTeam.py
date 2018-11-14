class SuperHero(object):
    def __init__(self, name='', age=0, power='n'):
        self.name = name
        self.age = age
        self.power = power

    def set_name(self):
        hero_name = input("Enter the name of the hero: ")
        self.name = hero_name

    def set_age(self):
        hero_age = int(input("Enter age of hero: "))
        self.age = hero_age

    def set_power(self):
        hero_power = input("What is the power of the hero ")
        self.power = hero_power

    def find_hero_power(self):
        if self.power == 'f':
            return 'Flying'
        if self.power == 'g':
            return 'Giant'
        if self.power == 'h':
            return 'Hacker'
        if self.power == 'n':
            return 'None'
        else:
            return 'Weakling'

    def __str__(self):
        return "{} ({}): {}".format(self.name, self.age, self.find_hero_power())


def create_group_super_heroes():
    hero_group = []
    number_of_heroes = int(input("How many heroes would you like to make? "))
    for x in range(number_of_heroes):
        hero_name = input("Enter the name of the hero: ")
        hero_age = int(input("Enter age of hero: "))
        hero_power = input("What is the power of the hero? ").lower()
        hero = SuperHero(hero_name, hero_age, hero_power)
        hero_group.append(hero)
    return hero_group


def print_hero_group(hero_group):
    for x in hero_group:
        print(x)


def main():
    hero_group = create_group_super_heroes()
    print_hero_group(hero_group)


main()