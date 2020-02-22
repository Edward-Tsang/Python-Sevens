import re
from typing import List
from Card import Card

def get_card_above(suit, value):
    switcher = {
        "A": "2",
        "2": "3",
        "3": "4",
        "4": "5",
        "5": "6",
        "6": "7",
        "7": "8",
        "8": "9",
        "9": "10",
        "10": "J",
        "J": "Q",
        "Q": "K",
        "K": "MAX"
    }
    return suit+switcher.get(value)


def get_card_below(suit, value):
    switcher = {
        "A": "MIN",
        "2": "A",
        "3": "2",
        "4": "3",
        "5": "4",
        "6": "5",
        "7": "6",
        "8": "7",
        "9": "8",
        "10": "9",
        "J": "10",
        "Q": "J",
        "K": "Q"
    }
    return suit+switcher.get(value)


def get_card_key_value(value):
    switcher = {
        "A": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 11,
        "Q": 12,
        "K": 13
    }
    return switcher.get(value)


def check_input_valid_card(value: str, list_of_valid_cards: List[Card]):
    if len(value) == 3:
        return len(value) < 3 and bool(re.search('[C,S,H,D][1-9][0]', value)) and list_of_valid_cards.__contains__(value)
    else:
        return len(value) < 3 and bool(re.search('[C,S,H,D][1-9]', value)) and list_of_valid_cards.__contains__(value)
