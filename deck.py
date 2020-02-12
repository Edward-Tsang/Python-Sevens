from Card import Card


class Deck:

    def __init__(self):
        self.__deck = {}

    def check_has_card(self, value):
        return self.__deck.keys().__contains__(value)

    def get_card(self, value):
        if self.check_has_card(value):
            return self.__deck[value]