import csv
import random
from datetime import datetime
from warchest import Board, Player, GameTerminalView
from warchest.unit_cards import *
from warchest.config import Config

class WarChestGame:
    
    def start_game(self) -> str:
        # create board and setup
        self.board: Board = Board()
        self.board.setup()

        # setup players
        self.setup_players()

        # show initial board
        GameTerminalView.show(self.board)

        winner: Player = self.play_game()
        return  winner.name

    def setup_players(self) -> None:
        # create players and setup
        self.players: list[Player] = [Player(name="Crow", symbol='^'), Player(name="Wolf", symbol='v')]
        self.initiative_index: int = random.randint(0, len(self.players)-1)
        self.players[self.initiative_index].set_initiative()

        # select random unit cards from random set
        random_set = random.sample(range(8), 4)
        # add cards to recruitment 
        for i in range(8):
            if i in random_set:
                self.players[0].add_unit_card(Config.UNITS[i]())
            else:
                self.players[1].add_unit_card(Config.UNITS[i]())
        
        for player in self.players:
            player.fill_bag()


    ############### ACTIONS ####################
    def initiative(self) -> None:
        '''Same action for all units. Select unit and discard coin'''
        if not self.current_player.has_initiative():
            unit_type: str = GameTerminalView.select_discard_coin(message="Piece to discard from hand", options=self.current_player.hand_string())
            self.current_player.discard(type=unit_type)
            self.set_initiative()
        else:
            GameTerminalView.show("The player already has the initiative.")
    
    def set_initiative(self) -> None:
        '''Sets the initiative for the next round'''
        before_player: Player = self.players[self.initiative_index]
        self.current_player.set_initiative()
        before_player.unset_initiative()
        self.initiative_index = self.players.index(self.current_player)

    def forfeit(self) -> None:
        '''Same action for all units. Select unit and discard coin for passing'''
        unit_type: str = GameTerminalView.select_discard_coin(message="Piece to discard from hand", options=self.current_player.hand_string())
        self.current_player.discard(type=unit_type)

    def recruit(self) -> None:
        unit_type: str = GameTerminalView.select_discard_coin(message="Piece to discard from hand to recruit the same kind", options=self.current_player.hand_string())
        self.current_player.discard(type=unit_type)


    def execute_action(self, action: str) -> None:
        method = getattr(self, action)
        method()

    def play_game(self) -> Player:
        winner: Player = None
        self.current_player: int = 0
        while not winner:
            index: int = self.initiative_index
            i: int = 0
            while not winner and i < len(self.players): # for each player
                self.current_player: Player = self.players[index]
                self.current_player.get_hand(Config.HAND_SIZE)
                
                # show player info
                GameTerminalView.show(self.current_player)

                while self.current_player.has_coins_in_hand():
                    action: str = GameTerminalView.select_action()
                    self.execute_action(action)
   
                index = (index + 1) % len(self.players)
                i += 1                   
                # Check game ending
                winner = self.current_player.is_winner()
                # show player info
                GameTerminalView.show(self.board)
            
        return winner

    def show_statistics(self) -> None:
        with open('./files/statistics.txt', 'r') as input_file:
            reader = csv.reader(input_file)
            header_row = next(reader)
            print(f"\t{header_row[0]}\t{header_row[1]}\t{header_row[2]}")
            for line in reader: #read line by line
                print(f"\t{line[0]}\t{line[1]}\t\t{line[2]}")

    def store_winner(self, winner: str) -> None:
        # it appends a new winner 
        # in future versions, check if the player is in previous data to sum games won
        with open('./files/statistics.txt', 'w') as output_file:
            csv_writer = csv.writer(output_file)
            csv_writer.writerow([winner.name, 1, datetime.now()])