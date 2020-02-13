from Card import Card


class Player:

    def __init__(self, name):
        self.__name = name
        self.__deck = {}
        self.__playable_cards = []

    def get_deck(self):
        return self.__deck

    def set_deck(self, deck: []):
        self.__deck = deck

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def add_to_deck(self, card: Card):
        self.__deck[card.get_suit()+card.get_face()] = card

    def check_has_card(self, value):
        return self.__deck.keys().__contains__(value)

    def get_card(self, value):
        return self.__deck[value]

    def get_playable_cards(self):
        return self.__playable_cards
