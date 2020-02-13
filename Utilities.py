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
