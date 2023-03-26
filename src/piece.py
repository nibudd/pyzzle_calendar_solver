from copy import deepcopy
from typing import Iterable, Self

from src.square import Square


class Piece(tuple):
    def __new__(cls, squares: Iterable[Square]) -> Self:
        if all(isinstance(square, Square) for square in squares):
            return super().__new__(cls, squares)

        raise PieceTypeError(
            f"Invalid arguments to {cls.__name__}: {(type(x) for x in squares)}"
        )

    def flip(self: tuple[Square]) -> Self:
        """Flips the piece over, as if reflected across the x-axis

        Returns:
            Piece: A new piece that is a mirror image of the original
        """
        reflected = (square.reflect_across_x_axis() for square in self)
        move_y = max(square.y for square in self) + min(square.y for square in self)
        return Piece(square.translate(y=move_y) for square in reflected)

    def move(self: tuple[Square], x: int, y: int) -> Self:
        """Moves piece a number of squares equal to `translation`

        Args:
            translation (tuple): A tuple indicating the number of squares the piece will move

        Returns:
            Self: A new piece that is the same shape of the original but offset by `translation`
        """
        return Piece(square.translate(x, y) for square in self)

    def rotate(self: tuple[Square], reps: int = 1) -> Self:
        """Rotates a piece 90 degrees counter-clockwise the indicated number of times

        Args:
            reps (int, optional): The number of 90 degree reotations to perform. Defaults to 1.

        Returns:
            Self: A new piece that is the same shape o the original rotated 90 degrees counter-clockwise the indicated number of times
        """
        min_reps = reps % 4
        rotated = []
        for square in self:
            _square = deepcopy(square)
            for _ in range(min_reps):
                _square = _square.rotate_90deg_counter_clockwise()

            rotated.append(_square)

        return Piece(rotated)

    @classmethod
    def from_iterables(cls, iterables: Iterable[Iterable[int]]) -> Self:
        return super().__new__(cls, (Square(*iterable) for iterable in iterables))

    def __eq__(self, other: Self) -> bool:
        return all(pair[0] == pair[1] for pair in zip(self, other))


class PieceTypeError(TypeError):
    pass
