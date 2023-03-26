from typing import Any

import pytest

from src.square import Square, InvalidSquareError


def test_x_returns_element_0():
    sut = Square((0, 1))
    assert sut.x == 0


def test_y_returns_element_1():
    sut = Square((0, 1))
    assert sut.y == 1


def test_hashes_of_Square_with_same_tuple_are_equal():
    sut_1 = Square((0, 1))
    sut_2 = Square((0, 1))

    assert sut_1.hash == sut_2.hash


def test_hashes_of_Square_with_different_tuples_are_not_equal():
    sut_1 = Square((0, 1))
    sut_2 = Square((4, 4))

    assert sut_1.hash != sut_2.hash


@pytest.mark.parametrize("tup", [
    (),
    (1,),
    (3, 3, 3),
    (4, 4, 4, 4)
])
def test_InvalidSquareError_raised_for_tuples_of_length_other_than_2(tup: tuple[int]):
    with pytest.raises(InvalidSquareError):
        Square(tup)


@pytest.mark.parametrize("tup", [
    (1, 1.1),
    ("hi", 2, 3),
    (1, 2, True)
])
def test_tuples_containing_non_int_values_raise_InvalidSquareError(tup: tuple[Any]):
    with pytest.raises(InvalidSquareError):
        Square(tup)
