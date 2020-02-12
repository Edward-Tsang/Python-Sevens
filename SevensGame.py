from Card import Card
import random
from Player import Player
from Layout import Layout


class SevensGame:

    def __init__(self):
        self.deck = []
        self.faces = {"A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"}
        self.suits = {"S": "Spades", "H": "Hearts", "C": "Clubs", "D": "Diamonds"}
        self.players = []
        self.generate_deck()
        self.layouts = []
        self.current_player = None
        self.possible_card_selections = []

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
                if len(self.deck) > 0:
                    p.add_to_deck(self.deck[len(self.deck)-1])
                    self.deck.pop()
                else:
                    break

    def get_seven_of_diamonds(self):
        for p in self.players:
            if p.check_has_card("D7"):
                self.current_player = p
                layout = Layout("D")
                layout.add_to_deck(7)
                self.layouts.append(layout)
                p.get_deck().pop("D7")
                break

    def get_next_player(self):
        if self.players.index(self.current_player)+1 > len(self.players):
            index = 0
        else:
            index = self.players.index(self.current_player) + 1
        self.current_player = self.players[index]

    def start_game_process(self):
        self.get_next_player()

    # def check_layout_possible_selections(self):
    #     for l in self.layouts:
    #









