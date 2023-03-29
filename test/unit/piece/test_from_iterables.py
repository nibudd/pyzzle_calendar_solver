import pytest
from typing import Iterable

from src.piece import Piece


@pytest.mark.parametrize(
    "iterables",
    [
        ((1, 1), (2, 2), (3, 3)),
        ([1, 1], [2, 2], [3, 3]),
    ],
)
def test_returns_a_Piece(iterables: Iterable[Iterable[int]]):
    assert isinstance(Piece.from_iterables(iterables, "X"), Piece)
