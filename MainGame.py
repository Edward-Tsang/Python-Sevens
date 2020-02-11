import SevensGame

def main():
    game  = SevensGame.SevensGame()
    game.generateDeck()
    for card in game.deck:
        print(card.get_suit())


if __name__ == "__main__":
    main()

