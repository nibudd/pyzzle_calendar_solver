import pytest

from src.square import Square, reflect


@pytest.mark.parametrize("input,expected", [
    (Square(0, 0), Square(0, 0)), 
    (Square(1, 1), Square(1, -1))
])
def test_reflect_returns_Square_reflected_across_0_axis(
    input: Square, expected: Square
):
    output = reflect(input)

    assert output == expected
