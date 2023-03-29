import pytest

from src.square import Square
from src.piece import Piece


@pytest.mark.parametrize(
    "inputs",
    [((1, 0), (2, 0), (3, 0)), ((1, 1), (2, 1), (3, 1)), ((1, 5), (2, 5), (3, 5))],
)
def test_pieces_symmetric_across_x_axis_are_unchanged(inputs: tuple[tuple[int]]):
    sut = Piece.from_iterables(inputs, "X")

    assert sut.flip() == sut


@pytest.mark.parametrize(
    "unflipped,flipped",
    [
        (((0, 0), (1, 1)), ((0, 1), (1, 0))),
        (((0, 0), (1, 1), (2, 1)), ((0, 1), (1, 0), (2, 0))),
    ],
)
def test_pieces_asymmetric_across_x_axis_flip_as_expected(
    unflipped: tuple[int], flipped: tuple[int]
):
    sut = Piece.from_iterables(unflipped, "X")

    assert sut.flip() == Piece.from_iterables(flipped, "X")
