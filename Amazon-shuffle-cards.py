# Given a deck of cards, the task is to shuffle them
from enum import Enum
from typing import List
from random import randint


class CardFace(Enum):
    ACE = (1, 'A')
    TWO = (2, '2')
    THREE = (3, '3')
    FOUR = (4, '4')
    FIVE = (5, '5')
    SIX = (6, '6')
    SEVEN = (7, '7')
    EIGHT = (8, '8')
    NINE = (9, '9')
    TEN = (10, '10')
    JACK = (11, 'J')
    QUEEN = (12, 'Q')
    KING = (13, 'K')

    def __init__(self, val: int, short_name: str):
        self.val = val
        self.short_name = short_name


class CardSuit(Enum):
    SPADE = 1
    HEART = 2
    DIAMOND = 3
    CLUB = 4


class Card:
    def __init__(self, suit: CardSuit, face: CardFace):
        self.suit = suit.name
        self.face = face.name
        self.alias = face.short_name
        self.val = face.val

    def __repr__(self):
        return f"({self.suit}, {self.alias})"

    def __str__(self):
        return f"({self.suit}, {self.face})"


class Deck:
    def __init__(self):
        cards = []
        for suit in CardSuit:
            for face in CardFace:
                cards.append(Card(suit, face))
        self.cards = cards
        self.__original = cards

    def reset(self):
        # reset the deck to the initial state
        self.cards = self.__original

    def sort(self):
        # sort the deck:
        # 1. suits are sorted in alphabetical order
        # 2. cards in each suit are sorted in incresing order
        self.cards.sort(key=lambda card: (card.suit, card.val))

    def shuffle(self):
        # shuffle the deck
        for i in range(len(self.cards)):
            # some random index to swap with
            swapWith = randint(0, len(self.cards) - 1)
            self.cards[i], self.cards[swapWith] = self.cards[swapWith], self.cards[i]

    def draw(self, k: int) -> List[Card]:
        # randomly draw cards from the deck
        if k < 0 or k >= len(self.cards):
            raise ValueError('You can''t draw cards less than 0 or more than number of cards left in the deck')
        if k == 0:
            return []
        res = []
        while len(res) < k:
            i = randint(0, len(self.cards) - 1)
            res.append(self.cards.pop(i))
        return res

    def drawFromTop(self, k: int) -> List[Card]:
        # draw cards from top of the deck
        if k < 0 or k >= len(self.cards):
            raise ValueError('You can''t draw cards less than 0 or more than number of cards left in the deck')
        if k == 0:
            return []
        res = []
        while len(res) < k:
            res.append(self.cards.pop())
        return res

    def drawFromBottom(self, k: int) -> List[Card]:
        # draw cards from bottom of the deck
        if k < 0 or k >= len(self.cards):
            raise ValueError('You can''t draw cards less than 0 or more than number of cards left in the deck')
        if k == 0:
            return []
        res = []
        while len(res) < k:
            res.append(self.cards.pop(0))
        return res


d = Deck()
print(d.cards)
d.sort()
print(d.cards)
d.shuffle()
print(d.cards)
hand = d.draw(4)
print(hand)
print(len(d.cards))
d.reset()
print(d.cards)
