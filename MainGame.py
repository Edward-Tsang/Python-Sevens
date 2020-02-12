import SevensGame


def main():
    game = SevensGame.SevensGame()
    player_num = int(input("Please enter the number of players: "))
    if player_num < 3:
        print("There must be a minimum of three players. Please try again.")
    else:
        players = player_num
        while players != 0:
            player = player_num - players + 1
            if player > player_num:
                player = player_num
            player_name = input(f"Please enter name of Player {player}:")
            players -= 1
            game.generate_player(player_name)

        game.deal_cards()
        game.get_seven_of_diamonds()


if __name__ == "__main__":
    main()

