from Card import Card


class Layout:

    def __init__(self, suit):
        self.suit = suit
        self.__numbers = []

    def add_to_deck(self, card_number):
        self.__numbers.append(card_number)
        self.__numbers.sort()
