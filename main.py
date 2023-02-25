from warchest import WarChestGame, GameTerminalView


if __name__ == "__main__":
    # create the game
    game: WarChestGame = WarChestGame()

    # show statistics
    game.show_statistics()

    winner: str = None
    # start game and return the winner
    if GameTerminalView.start_game():
        winner = game.start_game()
        
    # store winner
    if winner:
        game.store_winner(winner)

