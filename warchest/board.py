from typing import Optional, Dict, Tuple
from enum import Enum
from warchest.pieces import ControlMarker, Coin


class CellType(Enum):
    CROW = "C"
    WOLF = "W"
    NEUTRAL = "@"
    EMPTY = "."

    def __str__(self):
        return str(self.name)


class Board:
    """
    This class represents the game board.
        n contains the size
        start_zones_per_player is the number of ocuppied starting zones by each player
        content is a dict with all the placed units
        layout is a dict with the board distribution
    """

    def __init__(self, size: int = 9, starting_zones_per_player: int = 2) -> None:
        self.n: int = size
        self.start_zones_per_player: int = starting_zones_per_player
        self.content: Dict[Tuple[str, int], Optional[Coin]] = {}
        self.layout: Dict[Tuple[str, int], Optional[CellType]] = {}

    def _layout_from_file(self) -> None:
        # in future versions the filepath could be a input of the main program

        with open(f"./files/layout{self.n}.txt", "r") as input_file:
            i: int = 0
            for line in input_file:  # read line by line
                elements = line.split()  # trim \n and separate elements
                j: int = 0
                for e in elements:
                    cell = CellType(e)
                    if (
                        cell is CellType.CROW
                        or cell is CellType.WOLF
                        or cell is CellType.NEUTRAL
                    ):
                        self.layout[(self._string_column(i), j)] = cell
                    j = j + 1
                i = i + 1

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

    def check_movement(self, coords: tuple[str, int], player: str) -> bool:
        return self.check_adjacency(
            coords=coords, player=player
        ) and self.check_empty_cell(coords=coords, player=player)

    def check_adjacency(self, coords: tuple[str, int], player: str) -> bool:
        adjacent: bool = False
        player_mark: CellType = CellType(
            player.upper()[0]
        )  # obtains the char for W or C

        adjacency_cells: list = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                adjacency_cells.append((chr(ord(coords[0]) + i), coords[1] + j))
        adjacency_cells.remove(coords)

        print(adjacency_cells)
        control_zones: list = [k for k, v in self.layout.items() if v is player_mark]
        for cz in control_zones:
            if cz in adjacency_cells:
                adjacent = True
        return adjacent

    def check_empty_cell(self, coords: tuple[str, int], player: str) -> bool:
        return coords not in self.content

    def place_unit(self, coin, coords: tuple[str, int]):
        self.content[coords] = coin

    def _string_column(self, index: int) -> chr:
        return chr(ord("a") + index)

    def __str__(self) -> str:
        # header
        header: str = " "
        divisor: str = " "
        for i in range(self.n):
            header += "  " + str(i)
            divisor += "---"

        # content
        content: str = ""
        for row in range(self.n):
            output: str = f"{self._string_column(row)}|"
            for col in range(self.n):
                key_obj: tuple = (self._string_column(row), col)

                if key_obj in self.content:
                    output += " " + str(self.content[key_obj])
                else:
                    if key_obj in self.layout:
                        output += " @ "
                    else:
                        output += " . "
            content += output + "\n"
        return "\n" + header + "\n" + divisor + "\n" + content + "\n"
