import Utilities
from typing import Dict

class Layout:

    def __init__(self, suit):
        self.__suit: str = suit
        self.__faces: Dict[int,str] = {}

    def add_to_deck(self, card):
        self.__faces[Utilities.get_card_key_value(card.get_face())] = card.get_face()
        temp_faces = self.__faces.copy()
        self.__faces.clear()
        for i in sorted(temp_faces):
            self.__faces[i] = temp_faces[i]

    def get_faces(self):
        return self.__faces

    def get_suit(self):
        return self.__suit
