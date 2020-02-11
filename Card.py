class Card:

    __suit = ""
    __face = ""

    def __init__(self, suit, face):
        self.__suit = suit
        self.__face = face

    def get_suit(self):
        return self.__suit

    def set_suit(self, suit):
        self.__suit = suit

    def get_face(self):
        return self.__face

    def set_face(self, face):
        self.__face = face

