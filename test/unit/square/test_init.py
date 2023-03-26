from typing import Any

import pytest

from src.square import Square, SquareTypeError


@pytest.mark.parametrize("input", [(1, 1.1), ("hi", 2), (2, True)])
def test_non_int_arguments_raise_SquareTypeError(input: tuple[Any]):
    with pytest.raises(SquareTypeError):
        Square(*input)
