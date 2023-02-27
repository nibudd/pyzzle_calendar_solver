import pytest

from src.square import Square, InvalidSquareError


@pytest.mark.parametrize("start,move,expected", [
    ((0, 0), (0, 0), (0, 0)),
    ((0, 0), (1, 2), (1, 2)),
    ((1, 1), (-2, 0), (-1, 1))
])
def test_translate_returns_Square_reflected_across_0_axis(start: tuple[int], move: tuple[int], expected: tuple[int]):
    sut = Square(start)

    assert sut.translate(move) == expected


@pytest.mark.parametrize("move", [
    (1,),
    (3, 3, 3),
    (4, 4, 4, 4)
])
def test_InvalidSquareError_raised_for_translations_of_length_other_than_2(move: tuple[int]):
    sut = Square((1, 2))
    
    with pytest.raises(InvalidSquareError):
        sut.translate(move)
