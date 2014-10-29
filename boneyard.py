'''Boneyard will handle bones for games'''

from bone import Bone
from random import shuffle

class Boneyard:
	'''
	Boneyard will hande generation of bones,
	shuffling of bones, display of bones,
	and dealing of bones
	'''

	def __init__(self):
		'''return 'deck' of 28 tuples'''
		'''converting to bone objest but'''
		'''advantage to keeping as tuples'''
		'''however display as intended not'''
		'''possible as tuples'''

		deck = self.shuffle()

		self.deck = []

		for tup in deck:
			self.deck.append(Bone(*tup))

	def shuffle(self):
		'''create bonyard and random order'''

		deck = []

		for x in range(7):
			for y in range(7):
				if (x, y) not in deck and (y, x) not in deck:
					deck.append((x, y))

		shuffle(deck)
		return deck

	def count(self):
		'''get count of remaining bones'''

		return len(self.deck)

	def display(self, order=0):
		'''display bones using Bone display '''

		for x in range(len(self.deck)):
			if x != 0 and x % 7 == 0:
				print()
			self.deck[x].display(order)

		print()
