import pytest

from src.board import Board, PiecePlacementError
from src.piece import PieceService


def test_can_add_piece_to_empty_squares():
    piece = PieceService.from_iterables(((0, 0), (0, 1), (1, 1)), "X")
    board = Board(3, 3)

    board.add_piece(piece)


def test_adding_piece_to_occupied_squares_raises_PiecePlacementError():
    piece_1 = PieceService.from_iterables(((0, 0), (0, 1), (1, 1)), "X")
    piece_2 = PieceService.from_iterables(((1, 0), (0, 1), (2, 1)), "Y")
    board = Board(3, 3)

    board.add_piece(piece_1)

    with pytest.raises(PiecePlacementError):
        board.add_piece(piece_2)