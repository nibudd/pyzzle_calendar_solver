import pytest

from src.square import Square, translate


@pytest.mark.parametrize(
    "start,move,expected",
    [
        (Square(0, 0), Square(0, 0), Square(0, 0)), 
        (Square(0, 0), Square(1, 2), Square(1, 2)), 
        (Square(1, 1), Square(-2, 0), Square(-1, 1))
    ]
)
def test_translate_returns_expected_translated_square(
    start: Square, move: Square, expected: Square
):
    finish = translate(start, move)

    assert finish == expected
