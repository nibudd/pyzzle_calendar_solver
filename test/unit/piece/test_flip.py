import pytest

from src.square import Square
from src.piece import Piece


@pytest.mark.parametrize("squares", [
    (Square((1, 0)), Square((2, 0)), Square((3, 0))),
    (Square((1, 1)), Square((2, 1)), Square((3, 1))),
    (Square((1, 5)), Square((2, 5)), Square((3, 5)))
])
def test_pieces_symmetric_across_0_axis_are_unchanged(squares: tuple[Square]):
    sut = Piece(squares)

    assert sut.flip() == sut
