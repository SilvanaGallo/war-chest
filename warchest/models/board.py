from typing import Optional, Dict, Tuple
from enum import Enum
from warchest.models import Unit


class CellType(Enum):
    CROW = 'C'
    WOLF = 'W'
    NEUTRAL = '@'
    EMPTY = '.'

    def __str__(self):
        return str(self.name)



class Board:
    '''
    This class represents the game board. 
        n contains the size
        start_zones_per_player is the number of ocuppied starting zones by each player
        content is a dict with all the placed units 
        layout is a dict with the board distribution
    '''

    def __init__(self, size: int = 9, starting_zones_per_player: int = 2)-> None:
        self.n: int = size
        self.start_zones_per_player: int = starting_zones_per_player
        self.content: Dict[Tuple[str, int], Optional[Unit]] = {}
        self.layout: Dict[Tuple[str, int], Optional[CellType]] = {}
       
    def _layout_from_file(self) -> None:
        # in future versions the filepath could be a input of the main program
        
        with open(f'./layout{self.n}.txt', 'r') as input_file:
            i: int = 0
            for line in input_file: #read line by line
                elements = line.split() #trim \n and separate elements
                j: int = 0
                for e in elements:
                    cell = CellType(e)
                    if cell is CellType.CROW or cell is CellType.WOLF or cell is CellType.NEUTRAL:
                        self.layout[(self._string_column(i), j)] = cell
                    j = j+1
                i = i+1

    def generate_layout(self) -> None:
        # here I want to add equidistant random neutral zones @
        pass

    def setup(self) -> None:
        self._layout_from_file()
        # or self.generate_layout() in future version

        # setting up the starting_zones
        for i, k in self.layout.items():
            if k is CellType.CROW or k is CellType.WOLF:
                self.content[i] = ControlMarker(owner_name=str(k))

    def _string_column(self, index: int) -> chr:
        return chr(ord('a') + index)

    def print(self) -> None:
        # print header
        header: str = ' '
        divisor: str = ' '
        for i in range(self.n):
            header += '  ' + self._string_column(i)
            divisor += '---'
        print(header)
        print(divisor)

        # print content
        for row in range(self.n):
            output: str = f'{row}|'
            for col in range(self.n):
                key_obj: tuple = (self._string_column(row), col)
                output += ' ' + (self.content[key_obj] if key_obj in self.content else '. ')
            print(output)

