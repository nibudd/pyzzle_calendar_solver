from typing import Any

import pytest

from src.piece import PieceService, PieceTypeError
from src.square import Square


@pytest.mark.parametrize(
    "tup", [((1, 1), 1.1), ("hi", (2, 3)), ((2, 2), True), (2, (2, 3))]
)
def test_tuples_containing_non_Square_values_raise_PieceTypeError(tup: tuple[Any]):
    with pytest.raises(PieceTypeError):
        PieceService(tup, "X")


def test_tuple_containing_only_Squares_returns_Piece_object():
    sut = PieceService((Square(1, 2), Square(0, 1), Square(3, 4)), "X")

    assert isinstance(sut, PieceService)


@pytest.mark.parametrize("id", [
    1, 2.3, True, (4, 5.5), [6.6, 7]
])
def test_non_str_id_raises_PieceTypeError(id: Any):
    with pytest.raises(PieceTypeError):
        PieceService(((1, 1), (2, 2), (3, 3)), id)