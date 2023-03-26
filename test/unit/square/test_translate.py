import pytest

from src.square import Square, SquareTypeError


@pytest.mark.parametrize("start,move,expected", [
    ((0, 0), (0, 0), (0, 0)),
    ((0, 0), (1, 2), (1, 2)),
    ((1, 1), (-2, 0), (-1, 1))
])
def test_translate_returns_Square_reflected_across_0_axis(start: tuple[int], move: tuple[int], expected: tuple[int]):
    sut = Square(*start)

    assert sut.translate(*move) == Square(*expected)


@pytest.mark.parametrize("move", [
    (1, 1.1),
    (2.1, 1)
])
def test_SquareTypeError_raised_for_translations_containing_non_int_values(move: tuple[int]):
    sut = Square(1, 2)
    
    with pytest.raises(SquareTypeError):
        sut.translate(move)
