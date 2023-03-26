import pytest

from src.square import Square


@pytest.fixture
def tuple_of_squares() -> tuple[Square]:
    return (Square(1, 1), Square(2, 2), Square(3, 4))
