import pytest

from src.square import Square
from src.piece import Piece


@pytest.mark.parametrize("squares,translation,translated", [
    (
        (Square((1, 0)), Square((2, 2)), Square((3, 1))), 
        (0, 0),
        (Square((1, 0)), Square((2, 2)), Square((3, 1)))
    ),
    (
        (Square((1, 0)), Square((2, 2)), Square((3, 1))), 
        (1, 1),
        (Square((2, 1)), Square((3, 3)), Square((4, 2)))
    ),
    (
        (Square((1, 0)), Square((2, 2)), Square((3, 1))), 
        (1, 2),
        (Square((2, 2)), Square((3, 4)), Square((4, 3)))
    )
])
def test_pieces_symmetric_across_0_axis_are_unchanged(squares: tuple[Square], translation: tuple, translated: Piece):
    piece = Piece(squares)
    sut = piece.move(translation)

    assert sut == translated
