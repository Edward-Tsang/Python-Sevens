import Card
import random

deck = []
faces = {"A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"}
suits = {"S": "Spades", "H": "Hearts", "C": "Clubs", "D": "Diamonds"}


def generateDeck():
    for suit in suits.keys():
        for face in faces:
            deck.append(Card.Card(suit,face))
    random.shuffle(deck)

generateDeck()

for card in deck:
    print(card.get_suit())





