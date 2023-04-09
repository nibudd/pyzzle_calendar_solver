import pytest

from src.piece import Piece, move
from src.square import Square


@pytest.mark.parametrize(
    "piece,translation,expected",
    [
        (
            Piece((Square(1, 0), Square(2, 2), Square(3, 1)), "X"), 
            Square(0, 0), 
            Piece((Square(1, 0), Square(2, 2), Square(3, 1)), "X")
        ),
        (
            Piece((Square(1, 0), Square(2, 2), Square(3, 1)), "X"), 
            Square(1, 1), 
            Piece((Square(2, 1), Square(3, 3), Square(4, 2)), "X")
        ),
        (
            Piece((Square(1, 0), Square(2, 2), Square(3, 1)), "X"), 
            Square(1, 2), 
            Piece((Square(2, 2), Square(3, 4), Square(4, 3)), "X")
        ),
    ],
)
def test_pieces_symmetric_across_0_axis_are_unchanged(
    piece: Piece, translation: Square, expected: Piece
):
    moved = move(piece, translation)

    assert moved == expected
