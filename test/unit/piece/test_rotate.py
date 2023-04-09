import pytest

from src.square import Square
from src.piece import Piece, rotate


@pytest.mark.parametrize(
    "piece,reps,expected",
    [
        (
            Piece((Square(1, 0), Square(2, 2), Square(3, 1)), "X"),
            0,
            Piece((Square(1, 0), Square(2, 2), Square(3, 1)), "X"),
        ),
        (
            Piece((Square(1, 0), Square(2, 2), Square(3, 1)), "X"),
            1,
            Piece((Square(0, 1), Square(-2, 2), Square(-1, 3)), "X"),
        ),
        (
            Piece((Square(1, 0), Square(2, 2), Square(3, 1)), "X"),
            2,
            Piece((Square(-1, 0), Square(-2, -2), Square(-3, -1)), "X"),
        ),
        (
            Piece((Square(1, 0), Square(2, 2), Square(3, 1)), "X"),
            3,
            Piece((Square(0, -1), Square(2, -2), Square(1, -3)), "X"),
        ),
        (
            Piece((Square(1, 0), Square(2, 2), Square(3, 1)), "X"),
            4,
            Piece((Square(1, 0), Square(2, 2), Square(3, 1)), "X"),
        ),
        (
            Piece((Square(1, 0), Square(2, 2), Square(3, 1)), "X"),
            -1,
            Piece((Square(0, -1), Square(2, -2), Square(1, -3)), "X"),
        )
    ],
)
def test_pieces_symmetric_across_0_axis_are_unchanged(
    piece: Piece, reps: int, expected: Piece
):
    rotated = rotate(piece, reps)

    assert rotated == expected
