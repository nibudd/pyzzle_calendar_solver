from typing import Any

import pytest

from src.piece import Piece, PieceTypeError
from src.square import Square


def test_pieces_with_equal_squares_and_id_are_equal():
    squares = ((0, 0), (1, 2), (3, 4))
    id = "X"

    piece_1 = Piece.from_iterables(squares, id)
    piece_2 = Piece.from_iterables(squares, id)

    assert piece_1 == piece_2


def test_pieces_with_different_squares_are_not_equal():
    id = "X"

    piece_1 = Piece.from_iterables(((1, 2), (3, 4)), id)
    piece_2 = Piece.from_iterables(((1, 2), (3, 5)), id)

    assert piece_1 != piece_2


def test_pieces_with_different_ids_are_not_equal():
    squares = ((0, 0), (1, 2), (3, 4))

    piece_1 = Piece.from_iterables(squares, "X")
    piece_2 = Piece.from_iterables(squares, "Y")

    assert piece_1 != piece_2