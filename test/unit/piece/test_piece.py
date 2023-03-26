from typing import Any

import pytest

from src.piece import Piece, PieceTypeError
from src.square import Square


@pytest.mark.parametrize("tup", [
    ((1, 1), 1.1),
    ("hi", (2, 3)),
    ((2, 2), True),
    (2, (2, 3))
])
def test_tuples_containing_non_Square_values_raise_PieceTypeError(tup: tuple[Any]):
    with pytest.raises(PieceTypeError):
        Piece(tup)


def test_tuple_containing_only_Squares_returns_Piece_object():
    sut = Piece((
        Square(1, 2),
        Square(0, 1),
        Square(3, 4)
    ))

    assert isinstance(sut, Piece)
