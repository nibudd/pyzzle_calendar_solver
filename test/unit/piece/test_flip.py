import pytest

from src.square import Square
from src.piece import Piece


@pytest.mark.parametrize("squares", [
    (Square((0,1)), Square((0, 2)), Square((0, 3))),
])
def test_pieces_symmetric_across_0_axis_are_unchanged(squares: tuple[Square]):
    sut = Piece(squares)

    assert sut.flip() == sut
    assert False
    # update/fix this test
