import csv
import random
from datetime import datetime
from warchest import Board, Player

class WarChestGame:
    HAND_SIZE = 3

    def setup_players(self) -> None:
        self.players: list[Player] = [Player(name="Crow"), Player(name="Wolf")]
        self.initiative_index: int = random.randint(0, len(self.players)-1)
        self.players[self.initiative_index].set_initiative()
        
        
    def play_game(self) -> Player:
        winner: Player = None
        current_player: int = 0
        while not winner:
            index: int = self.initiative_index
            i: int = 0
            while not winner and i < len(self.players): # for each player
                current_player: Player = self.players[index]
                current_player.get_hand()
                
                # show player info
                current_player.print()

                for i in range(self.HAND_SIZE):
                    action: str = self.select_action()
                    self.execute_action(action)

                # show results
                self.board.print()    
                index = (index + 1) % len(self.players)
                i += 1           
        
                # Check game ending
                winner: Player = self.check_winner()
            
        return winner

    def start_game(self) -> Player:
        
        # create board and setup
        self.board: Board = Board()
        self.board.setup()

        # setup players
        self.setup_players()

        # show initial board
        self.board.print()

        winner: Player = self.play_game()
        return  winner

    def show_statistics(self) -> None:
        with open('./statistics.txt', 'r') as input_file:
            reader = csv.reader(input_file)
            header_row = next(reader)
            print(f"\t{header_row[0]}\t{header_row[1]}\t{header_row[2]}")
            for line in reader: #read line by line
                print(f"\t{line[0]}\t{line[1]}\t\t{line[2]}")

    def store_winner(self, winner: str) -> None:
        # it appends a new winner 
        # in future versions, check if the player is in previous data to sum games won
        with open('./statistics.txt', 'w') as output_file:
            csv_writer = csv.writer(output_file)
            csv_writer.writerow([winner.name, 1, datetime.now()])