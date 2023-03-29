from typing import Any

import pytest

from src.board import Board, BoardTypeError


@pytest.mark.parametrize("x,y", [
    (1.1, 2),
    (2, True),
    ("string", 3)
])
def test_non_int_arguments_raise_BoardTypeError(x: Any, y: Any):
    with pytest.raises(BoardTypeError):
        Board(x, y)