import pytest

from src.square import Square, rotate


@pytest.mark.parametrize(
    "input,expected", [
    (Square(0, 0), Square(0, 0)), 
    (Square(1, 2), Square(-2, 1)), 
    (Square(-2, -3), Square(3, -2))
])
def test_rotate_returns_Square_rotated_90_degrees_counter_clockwise(
    input: Square, expected: Square
):
    output = rotate(input)

    assert output == expected
