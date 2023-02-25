import unittest
from warchest import Board, CellType
from warchest.pieces import ControlMarker


class TestBoard(unittest.TestCase):
    def test_board_creation(self) -> None:
        board = Board(size=9, starting_zones_per_player=5)

        self.assertEqual(board.n, 9)
        self.assertEqual(board.start_zones_per_player, 5)

    def test_board_creation_without_parameters(self) -> None:
        board = Board()
        self.assertEqual(board.n, 9)
        self.assertEqual(board.start_zones_per_player, 2)

    def test_board_setup(self) -> None:
        board = Board()
        board.setup()

        sum_layout_crow: int = sum(
            1 for value in board.layout.values() if value is CellType.CROW
        )
        sum_layout_wolf: int = sum(
            1 for value in board.layout.values() if value is CellType.WOLF
        )

        # sum_content_crow: int = sum(
        #     1 for value in board.content.values() if value is ControlMarker
        # )
        # sum_content_wolf: int = sum(
        #     1 for value in board.content.values() if value is ControlMarker
        # )

        self.assertEqual(board.start_zones_per_player, sum_layout_crow)
        self.assertEqual(board.start_zones_per_player, sum_layout_wolf)

        # self.assertEqual(sum_content_crow, sum_layout_crow)
        # self.assertEqual(sum_content_wolf, sum_layout_wolf)
