import pytest

from src.square import Square


@pytest.mark.parametrize("input,expected", [
    ((0, 0), (0, 0)),
    ((1, 1), (-1, 1))
])
def test_reflect_returns_Square_reflected_across_0_axis(input: tuple[int], expected: tuple[int]):
    sut = Square(input)

    assert sut.reflect() == expected
