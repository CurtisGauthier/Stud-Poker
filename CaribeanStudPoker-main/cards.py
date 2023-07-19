import random

ranks = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'jack', 12: 'queen', 13: 'king', 14: 'ace'}
suits = ["clubs", "spades", "hearts", "diamonds"]
hand_strength = {1: 'Royal-flush', 2: 'Straight-flush', 3: 'Quads', 4: 'Fullhouse', 5: 'Flush', 6: 'Straight', 7: 'Threes', 8: 'Two-pair', 9: 'Pair', 10: 'Card-high'}

class Card:
    def __init__(self, current_cards):
        while True:
            rank = random.choice(list(ranks.keys()))
            suit = random.choice(suits)
            if (suit, rank) not in current_cards:
                self.rank = rank
                self.suit = suit
                current_cards.append((self.suit, self.rank))
                break

    def getSuit(self):
        return self.suit
    
    def getRank(self):
        return self.rank
    
    def printCard(self):
        print(ranks[self.rank] + self.suit, end='  ')

    def returnImageLink(self):
        return str(ranks[self.rank] + '_of_' + str(self.suit))
    
    def createCustomCard(self, rank, suit):
        self.rank = rank
        self.suit = suit

    
class Hand:
    def __init__(self, current_cards):
        self.cards = []
        for i in range(5):
            card = Card(current_cards)
            self.cards.append(card)

    def getCards(self):
        return self.cards

    def printCards(self):
        for card in self.cards:
            card.printCard()

    def createCustomHand(self, cards):
        self.cards = cards

    def getRanks(self):
        ranks = []
        for card in self.cards: ranks.append(card.getRank())
        return ranks

