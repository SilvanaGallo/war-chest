import unittest
from warchest.models.board import Board

class TestBoard(unittest.TestCase):

    def test_board_creation(self) -> None:
        board = Board(size=9)

        self.assertEqual(board.n, 9)

    def test_board_creation_without_size(self) -> None:
        board = Board()
        self.assertEqual(board.n, 9)
    
    def test_board_setup(self) -> None:
       board = Board()

       board.print()
       assert True 