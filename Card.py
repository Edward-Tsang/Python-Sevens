

class Card:

    __suit = ""
    __face = ""
    __value = 0

    def __init__(self, suit, face):
        self.__suit: str = suit
        self.__face: str = face
        switcher = {
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10
        }

        self.__value = switcher.get(face)

    def get_suit(self):
        return self.__suit

    def set_suit(self, suit):
        self.__suit = suit

    def get_face(self):
        return self.__face

    def set_face(self, face):
        self.__face = face



