import random


class Card(object):
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, score=0):
        self.K = 10
        self.J = 10
        self.Q = 10
        self.A = 11
        self.score = score

    def update_score(self, num=0):
        self.score += num

    def __str__(self):
        return self.cards


def draw_cards(number_of_cards):
    picked_cards = Card.cards[:number_of_cards]
    for x in range(len(picked_cards)):
        print("Card no. {}: {}".format(x+1, picked_cards[x]))
    return picked_cards


def draw_number_of_cards():
    try:
        number_of_cars = int(input("Number of cards (min 2, max 5): "))
        return number_of_cars
    except ValueError:
        print("")


def update_score(picked_cards, card):
    for x in picked_cards:
        if x.isdigit():
            x = int(x)
            card.update_score(x)
        elif x == 'A':
            card.update_score(11)
        elif x == 'K':
            card.update_score(10)
        elif x == 'J':
            card.update_score(10)
        elif x == 'Q':
            card.update_score(10)


def play_again(s):
    y_n = input("Play again? ")
    if y_n == 'y':
        s.score = 0
    else:
        exit()


def main():
    playing = True
    print("Scoring a blackjack hand")
    print("-" * 24)
    s = Card()
    while playing:
        random.shuffle(Card.cards)
        number_of_cars = draw_number_of_cards()
        drawn_cards = draw_cards(number_of_cars)
        update_score(drawn_cards, s)
        if s.score == 21:
            print("You win!")
        if s.score > 21:
            print("Busted!")
            play_again(s)
            continue
        print("Your score is {}".format(s.score))
        print('')
        y_or_n = input("Score a again? ")
        print('')
        if y_or_n == 'n':
            quit()


main()
