from src.board import Board
from src.piece import PieceService


def test_empty_square_returns_space_character():
    board = Board(3, 3)

    sut = board._get_letter(0, 0)

    assert sut == " "


def test_non_empty_square_returns_piece_character():
    board = Board(3, 3)
    piece = PieceService.from_iterables(((0, 0), (0, 1)), "X")
    board.add_piece(piece)

    sut = board._get_letter(0, 0)

    assert sut == "X"