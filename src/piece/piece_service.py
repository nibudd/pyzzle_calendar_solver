from copy import deepcopy
from typing import Iterable, Self

from .piece import Piece
from src import square


def flip(piece: Piece) -> Piece:
    """Flips the piece over, as if reflected across the x-axis

    Returns:
        Piece: A new piece that is a mirror image of the original
    """
    reflected = (square.reflect(s) for s in piece.squares)

    move_y = max(s.y for s in piece.squares) + min(s.y for s in piece.squares)
    move = square.Square(0, move_y)

    return Piece((square.translate(s, move) for s in reflected), piece.id)

# def move(self: Iterable[Square], x: int, y: int) -> Self:
#     """Moves piece a number of squares equal to `translation`

#     Args:
#         translation (tuple): A tuple indicating the number of squares the piece will move

#     Returns:
#         Self: A new piece that is the same shape of the original but offset by `translation`
#     """
#     return PieceService((square.translate(x, y) for square in self), self.id)

# def rotate(self, reps: int = 1) -> Self:
#     """Rotates a piece 90 degrees counter-clockwise the indicated number of times

#     Args:
#         reps (int, optional): The number of 90 degree reotations to perform. Defaults to 1.

#     Returns:
#         Self: A new piece that is the same shape o the original rotated 90 degrees counter-clockwise the indicated number of times
#     """
#     min_reps = reps % 4
#     rotated = []
#     for square in self:
#         _square: Square = deepcopy(square)
#         for _ in range(min_reps):
#             _square = _square.rotate_90deg_counter_clockwise()

#         rotated.append(_square)

#     return PieceService(rotated, self.id)

# @classmethod
# def from_iterables(cls, iterables: Iterable[Iterable[int]], id: str) -> Self:
#     squares = (Square(*iterable) for iterable in iterables)
#     return PieceService(squares, id)


class PieceTypeError(TypeError):
    pass
