from warchest import WarChestGame, Player

def start_game(game: WarChestGame) -> Player:
    play = input("Start game? (y/n): ")

    if play.lower() == 'y':
        winner: Player = game.start_game()
        return  winner
    else:
        print("Incorrect option. Bye.")
        return None

if __name__ == "__main__":
    # create the game
    game: WarChestGame = WarChestGame()

    # show statistics
    game.show_statistics()

    # start game and return the winner
    winner: Player = start_game(game)

    # store winner
    if winner:
        game.store_winner(winner.name)
