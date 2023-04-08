import pytest

from src.square import Square
from src.piece import Piece, flip


@pytest.mark.parametrize(
    "piece",
    [
        Piece((Square(1, 0), Square(2, 0), Square(3, 0)), "X"), 
        Piece((Square(1, 1), Square(2, 1), Square(3, 1)), "X"), 
        Piece((Square(1, 5), Square(2, 5), Square(3, 5)), "X")
    ],
)
def test_pieces_symmetric_across_x_axis_are_unchanged(piece: Piece):
    flipped = flip(piece)

    assert flipped == piece


@pytest.mark.parametrize(
    "unflipped,expected",
    [
        (
            Piece((Square(0, 0), Square(1, 1)), "X"), 
            Piece((Square(0, 1), Square(1, 0)), "X")
        ),
        (
            Piece((Square(0, 0), Square(1, 1), Square(2, 1)), "X"), 
            Piece((Square(0, 1), Square(1, 0), Square(2, 0)), "X")
        ),
    ],
)
def test_pieces_asymmetric_across_x_axis_flip_as_expected(
    unflipped: Piece, expected: Piece
):
    flipped = flip(unflipped)

    assert flipped == expected
