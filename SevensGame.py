from Card import Card
import Utilities
from Player import Player
from Layout import Layout
import random
from typing import List
from typing import Dict


class SevensGame:

    card_counter = 0

    def __init__(self):
        self.deck = []
        self.faces: List[str] = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.suits: Dict[str,str] = {"S": "Spades", "H": "Hearts", "C": "Clubs", "D": "Diamonds"}
        self.players: List[Player] = []
        self.generate_deck()
        self.layouts: Dict[str,Layout] = {}
        self.current_player = None
        self.possible_card_selections: List[str] = []
        self.winners:List[str] = []

    def generate_deck(self):
        for suit in self.suits.keys():
            for face in self.faces:
                self.deck.append(Card(suit, face))
                self.card_counter += 1
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
                card = p.get_card("D7")
                self.add_new_layout(card.get_suit())
                self.add_card_to_layout_deck(card)
                p.get_deck().pop("D7")
                break

    def get_next_player(self):
        if self.players.index(self.current_player)+1 >= len(self.players):
            index = 0
        else:
            index = self.players.index(self.current_player) + 1
        self.current_player = self.players[index]

    def start_game_process(self):
        self.get_next_player()

    def check_layout_possible_selections(self):
        self.possible_card_selections.clear()
        for l in self.layouts.values():
            minimum = Utilities.get_card_below(l.get_suit(), l.get_faces()[list(l.get_faces().keys())[0]])
            maximum = Utilities.get_card_above(l.get_suit(), l.get_faces()[list(l.get_faces().keys())[len(l.get_faces())-1]])
            if minimum.find('MIN') is not True and maximum.find('MAX') is not True:
                self.possible_card_selections.append(minimum)
                self.possible_card_selections.append(maximum)

    def check_if_player_has_cards(self):
        if self.current_player.check_has_card("S7"):
            self.current_player.get_playable_cards().append(self.current_player.get_card("S7"))
        elif self.current_player.check_has_card("H7"):
            self.current_player.get_playable_cards().append(self.current_player.get_card("H7"))
        elif self.current_player.check_has_card("C7"):
            self.current_player.get_playable_cards().append(self.current_player.get_card("C7"))
        else:
            for c in self.possible_card_selections:
                if self.current_player.check_has_card(c):
                    self.current_player.get_playable_cards().append(self.current_player.get_card(c))

    def current_player_can_play(self):
        return len(self.current_player.get_playable_cards()) > 0

    def play_players_card(self):
        if len(self.current_player.get_playable_cards()) == 1:
            selected_card_index = 0
        else:
            selected_card_index = random.randint(0, len(self.current_player.get_playable_cards())-1)
        selected_card = self.current_player.get_playable_cards()[selected_card_index]
        if self.layouts.keys().__contains__(selected_card.get_suit()):
            self.add_card_to_layout_deck(selected_card)
        else:
            self.add_new_layout(selected_card.get_suit())
            self.add_card_to_layout_deck(selected_card)
        self.current_player.get_playable_cards().clear()
        self.current_player.get_deck().pop(selected_card.get_suit()+selected_card.get_face())
        if len(self.current_player.get_deck()) == 0:
            self.winners.append(self.current_player.get_name())

    def add_new_layout(self, suit):
        layout = Layout(suit)
        self.layouts[layout.get_suit()] = layout

    def add_card_to_layout_deck(self,card):
        self.layouts[card.get_suit()].add_to_deck(card)
        self.card_counter -=1





