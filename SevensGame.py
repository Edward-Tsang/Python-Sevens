from Card import Card
import random
from Player import Player


class SevensGame:

    def __init__(self):
        self.deck = []
        self.faces = {"A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"}
        self.suits = {"S": "Spades", "H": "Hearts", "C": "Clubs", "D": "Diamonds"}
        self.players = []
        self.generate_deck()
        self.layouts = []

    def generate_deck(self):
        for suit in self.suits.keys():
            for face in self.faces:
                self.deck.append(Card(suit, face))
        random.shuffle(self.deck)

    def generate_player(self, name):
        self.players.append(Player(name))

    def deal_cards(self):
        while len(self.deck) > 0:
            for p in self.players:
                if(len(self.deck) > 0):
                    p.add_to_deck(self.deck[len(self.deck)-1])
                    self.deck.pop()
                else:
                    break

    def get_seven_of_diamonds(self):
        for p in self.players:
            if p.check_has_card("D7"):
                layout = [p.get_card("D7")]
                self.layouts.append(layout)
                p.get_deck().pop("D7")










