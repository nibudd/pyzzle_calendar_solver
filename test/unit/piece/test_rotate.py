import pytest

from src.square import Square
from src.piece import Piece


@pytest.mark.parametrize(
    "squares,reps,rotated",
    [
        (
            ((1, 0), (2, 2), (3, 1)),
            0,
            ((1, 0), (2, 2), (3, 1)),
        ),
        (
            ((1, 0), (2, 2), (3, 1)),
            1,
            ((0, 1), (-2, 2), (-1, 3)),
        ),
        (
            ((1, 0), (2, 2), (3, 1)),
            2,
            ((-1, 0), (-2, -2), (-3, -1)),
        ),
        (
            ((1, 0), (2, 2), (3, 1)),
            3,
            ((0, -1), (2, -2), (1, -3)),
        ),
        (
            ((1, 0), (2, 2), (3, 1)),
            4,
            ((1, 0), (2, 2), (3, 1)),
        ),
    ],
)
def test_pieces_symmetric_across_0_axis_are_unchanged(
    squares: tuple[tuple[int]], reps: int, rotated: tuple[tuple[int]]
):
    piece = Piece.from_iterables(squares, "X")
    sut = piece.rotate(reps)

    assert sut == Piece.from_iterables(rotated, "X")
