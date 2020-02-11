import Card
import random

class SevensGame:

    def __init__(self):
        self.deck = []
        self.faces = {"A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"}
        self.suits = {"S": "Spades", "H": "Hearts", "C": "Clubs", "D": "Diamonds"}

    def generateDeck(self):
        for suit in self.suits.keys():
            for face in self.faces:
                self.deck.append(Card.Card(suit, face))
        random.shuffle(self.deck)





