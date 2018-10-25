import random

class Card(object):
    def __init__(self, rank=0, suit=''):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return "{:<20s}".format(str(self.rank))


class Deck(object):
    def __init__(self, cards):


class PlayingHand(object):
    def __init__(self):
        pass

    def add_card(self):
        pass


    def NUMBER_CARDS(self):
        return 13


def test_cards():
     card1 = Card()
     print(card1)
     card2 = Card(5,'s')
     print(card2)
     card3 = Card('Q','D')
     print(card3)
     card4 = Card('x', 7)
     print(card4)


def print_4_hands(hand1, hand2, hand3, hand4):
 ''' Prints the 4 hands '''
    print(hand1)
    print(hand2)
    print(hand3)
    print(hand4)


def deal_4_hands(deck, hand1, hand2, hand3, hand4):
    ''' Deals cards for 4 hands
    :type handobjectect
    '''
    for i in range(PlayingHand.NUMBER_CARDS):
        hand1.add_card(deck.deal())
        hand2.add_card(deck.deal())
        hand3.add_card(deck.deal())
        hand4.add_card(deck.deal())


def test_hands(deck):
     hand1 = PlayingHand()
     hand2 = PlayingHand()
     hand3 = PlayingHand()
     hand4 = PlayingHand()
     print("The 4 hands:")
     print_4_hands(hand1, hand2, hand3, hand4)
     deal_4_hands(deck, hand1, hand2, hand3, hand4)
     print("The 4 hands after dealing:")
     print_4_hands(hand1, hand2, hand3, hand4)

random.seed(10)
test_cards()
deck = Deck()
deck.shuffle()

print("The deck:")
print(deck)
test_hands(deck)

print("The deck after dealing:")
print(deck)
