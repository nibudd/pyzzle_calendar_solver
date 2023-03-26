import pytest

from src.piece import Piece


@pytest.mark.parametrize("inputs,translation,translated", [
    (
        ((1, 0), (2, 2), (3, 1)), 
        (0, 0),
        ((1, 0), (2, 2), (3, 1))
    ),
    (
        ((1, 0), (2, 2), (3, 1)), 
        (1, 1),
        ((2, 1), (3, 3), (4, 2))
    ),
    (
        ((1, 0), (2, 2), (3, 1)), 
        (1, 2),
        ((2, 2), (3, 4), (4, 3))
    )
])
def test_pieces_symmetric_across_0_axis_are_unchanged(inputs: tuple[int], translation: tuple, translated: tuple[int]):
    piece = Piece.from_iterables(inputs)
    sut = piece.move(*translation)

    assert sut == Piece.from_iterables(translated)
