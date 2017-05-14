from __future__ import division
import numpy as np


class Player(object):
    deck = []

    def __init__(self, bank):
        self.bank = bank

    def adjustbank(self, amount):
        return self.bank + amount

    def takecards(self, cards):
        self.deck.append(cards)

    def sums(self):
        return sum(self.deck)

    def reveal(self):
        print
        self.deck


class Computer(object):
    deck = []

    def __init__(self):
        print('ss')

    def takecards(self, cards):
        self.deck.append(cards)

    def sums(self):
        return sum(self.deck)

    def reveal(self):
        print
        self.deck[0]


class TotalDeck(object):
    def __init__(self):
        print('deckcreated')
        self.cards = range(1, 14) * 4

    def givecards(self):
        card = int(np.random.choice(self.cards, 1))
        self.cards.remove(card)
        return card


new = TotalDeck()
newplayer = Player(1000)
comp = Computer()

card = new.givecards()
newplayer.takecards(card)
card = new.givecards()
newplayer.takecards(card)
card = new.givecards()
comp.takecards(card)
card = new.givecards()
comp.takecards(card)

while True:
    newplayer.reveal()
    comp.reveal()
    answer = input("do you want to continue ")
    if answer == 'yes':
        card = new.givecards()
        newplayer.takecards(card)
    else:
        print
        'do nothing'
    if newplayer.sums() >= 21:
        break
    elif comp.sums() == 21:
        break
    else:
        continue

print('congrats')
