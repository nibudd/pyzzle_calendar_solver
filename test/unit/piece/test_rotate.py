import pytest

from src.square import Square
from src.piece import Piece


@pytest.mark.parametrize("squares,reps,rotated", [
    (
        (Square((1, 0)), Square((2, 2)), Square((3, 1))), 
        0,
        (Square((1, 0)), Square((2, 2)), Square((3, 1)))
    ),
    (
        (Square((1, 0)), Square((2, 2)), Square((3, 1))), 
        1,
        (Square((0, 1)), Square((-2, 2)), Square((-1, 3)))
    ),
    (
        (Square((1, 0)), Square((2, 2)), Square((3, 1))), 
        2,
        (Square((-1, 0)), Square((-2, -2)), Square((-3, -1)))
    ),
    (
        (Square((1, 0)), Square((2, 2)), Square((3, 1))), 
        3,
        (Square((0, -1)), Square((2, -2)), Square((1, -3)))
    ),
    (
        (Square((1, 0)), Square((2, 2)), Square((3, 1))), 
        4,
        (Square((1, 0)), Square((2, 2)), Square((3, 1)))
    )
])
def test_pieces_symmetric_across_0_axis_are_unchanged(squares: tuple[Square], reps: int, rotated: Piece):
    piece = Piece(squares)
    sut = piece.rotate(reps)

    assert sut == rotated
