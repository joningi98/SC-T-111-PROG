import random


class Card(object):
	RANK = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
	SUIT = ['S', 'H', 'D', 'C']

	def __init__(self, rank='0', suit=''):
		if rank.upper() not in self.RANK:
			rank = '0'
		if suit.upper() not in self.SUIT:
			suit = ''
		self.rank = rank.upper()
		self.suit = suit.upper()

	def is_blank(self):
		if self.rank == '0' or self.suit == '':
			return True
		else:
			return False

	def __str__(self):
		if self.is_blank():
			return "{:>3s}".format("blk")
		else:
			return "{:>3s}".format(str(self.rank + self.suit))


class Deck(object):
	cards = []

	def __init__(self):
		""" Creates list with cards"""
		for x in Card.RANK:
			for y in Card.SUIT:
				self.cards.append(x+y)

	def __str__(self):
		list_deck = []
		str_deck = ''
		for x in range(4):
			my_arr = []
			for y in range(x*13, (x+1)*13):
				if y >= len(self.cards):
					break
				my_arr.append("{:>3s}".format(self.cards[y]))
			list_deck.append(my_arr)
		for x, y in enumerate(list_deck):
			if x == 3:
				str_deck += str(' '.join(y))
			else:
				str_deck += str(' '.join(y) + "\n")
		return str_deck

	def shuffle(self):
		random.shuffle(self.cards)

	def deal(self):
		dealt_card = self.cards.pop(0)
		return dealt_card


class PlayingHand(object):
	NUMBER_CARDS = 13

	def __init__(self):
		self.hand = []
		for x in range(13):
			self.hand.append("blk")

	def __str__(self):
		playing_hand = ""
		for x in self.hand:
			playing_hand += "{:>3s}".format(x)
			playing_hand += " "
		return playing_hand

	def add_card(self, card):
		for x in range(len(self.hand)):
			if self.hand[x] == "blk":
				self.hand[x] = card
				return


def test_cards():
	"""
	:return:
	"""
	card1 = Card()
	print(card1)
	card2 = Card('5', 's')
	print(card2)
	card3 = Card('Q', 'D')
	print(card3)
	card4 = Card('x', '7')
	print(card4)


def print_4_hands(hand1, hand2, hand3, hand4):
	"""
	Prints the 4 hands
	:param hand1:
	:param hand2:
	:param hand3:
	:param hand4:
	:return:
	"""
	print(hand1)
	print(hand2)
	print(hand3)
	print(hand4)


def deal_4_hands(deck, hand1, hand2, hand3, hand4):
	"""
	Deals cards for 4 hands
	:param deck:
	:param hand1:
	:param hand2:
	:param hand3:
	:param hand4:
	:return:
	"""
	for i in range(PlayingHand.NUMBER_CARDS):
		value = deck.deal()
		hand1.add_card(value)
		hand2.add_card(deck.deal())
		hand3.add_card(deck.deal())
		hand4.add_card(deck.deal())


def test_hands(deck):
	"""
	:param deck:
	:return:
	"""
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
