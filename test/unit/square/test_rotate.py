import pytest

from src.square import Square


@pytest.mark.parametrize("input,expected", [
    ((0, 0), (0, 0)),
    ((1, 2), (-2, 1)),
    ((-2, -3), (3, -2))
])
def test_rotate_returns_Square_rotated_90_degrees_counter_clockwise(input: tuple[int], expected: tuple[int]):
    sut = Square(*input)

    assert sut.rotate_90deg_counter_clockwise() == Square(*expected)
