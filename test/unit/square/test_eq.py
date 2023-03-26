import pytest

from src.square import Square


@pytest.mark.parametrize("input", [(0, 0), (1, 2), (13, 21)])
def test_Squares_with_same_arguments_are_equal(input: tuple[int]):
    assert Square(*input) == Square(*input)


@pytest.mark.parametrize(
    "first,second", [((0, 0), (0, 1)), ((1, 2), (1, 1)), ((13, 21), (13, 22))]
)
def test_Squares_with_different_arguments_are_not_equal(
    first: tuple[int], second: tuple[int]
):
    assert Square(*first) != Square(*second)
