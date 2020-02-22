import SevensGame
import Utilities


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
        while game.card_counter != 0:
            game.check_layout_possible_selections()
            game.check_if_player_has_cards()
            if game.current_player_can_play():
                print(game.list_playable_cards())
                selected_card = get_players_card(game)
                # game.play_players_card()
            else:
                print("You have no playable cards")
                game.get_next_player()
        print("winners in order:")
        for n in game.winners:
            print(n)


def get_players_card(game: SevensGame):
    selected_card: str = input("Player "+game.current_player.get_name()+", Please input card you want to play:")
    if Utilities.check_input_valid_card(selected_card,game.list_playable_cards()):
        return selected_card
    else:
        print("Card invalid")
        get_players_card(game)

if __name__ == "__main__":
    main()

