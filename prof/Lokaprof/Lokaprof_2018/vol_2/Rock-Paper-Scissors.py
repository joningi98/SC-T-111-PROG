import random

# Constants
ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'
QUIT = 'q'


def random_seed():
    seed = int(input("Random seed: "))
    random.seed(seed)


def choose_weapon():
    choosing = True
    weapons = [ROCK, PAPER, SCISSORS, QUIT]
    while choosing:
        user_choice = input("Enter weapon (r/p/s): ").lower()
        if user_choice in weapons:
            return user_choice
        else:
            continue


def computers_weapon():
    available_weapons = [ROCK, PAPER, SCISSORS]
    return random.choice(available_weapons)


def end_game(win, loss, tie):
    print("User won: {}\nComputer won: {}\nTie: {}".format(win, loss, tie))
    quit()


def result(user_weapon, cpu_weapon, win, loss, tie):
    print("Computer weapon: {}".format(cpu_weapon))
    print("User weapon: {}".format(user_weapon))
    if user_weapon == "r" and cpu_weapon == 'p':
        print("Computer wins!")
        loss += 1
    if user_weapon == "r" and cpu_weapon == 's':
        print("User wins!")
        win += 1
    if user_weapon == cpu_weapon:
        print("Tie!")
        tie += 1
    if user_weapon == "p" and cpu_weapon == 'r':
        print("User wins!")
        win += 1
    if user_weapon == "p" and cpu_weapon == 's':
        print("Computer wins!")
        loss += 1
    if user_weapon == "s" and cpu_weapon == "r":
        print("Computer wins!")
        loss += 1
    if user_weapon == "s" and cpu_weapon == "p":
        print("User wins!")
        win += 1
    return win, loss, tie


def main():
    random_seed()
    win = 0
    loss = 0
    tie = 0
    game = True
    while game:
        weapon = choose_weapon()
        cpu_weapon = computers_weapon()
        if weapon == 'q':
            end_game(win, loss, tie)
        win, loss, tie = result(weapon, cpu_weapon, win, loss, tie)


main()
