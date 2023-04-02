from copy import deepcopy
from typing import Iterable, Self

from src.square import Square


class Piece(tuple):
    def __new__(cls, squares: Iterable[Square], id: str) -> Self:
        _squares = tuple(squares)   
        if any(not isinstance(square, Square) for square in _squares):
            raise PieceTypeError(
                f"Invalid `squares` argument to {cls.__name__} with types: {(type(x) for x in squares)}"
            )
        
        self = super().__new__(cls, _squares)
        self.__init__(_squares, id)
        return self
    
    def __init__(self, squares: Iterable[Square], id: str) -> None:
        if not isinstance(id, str):
            raise PieceTypeError(
                f"Invalid argument `id` to {self.__class__.__name__} with type: {type(id)}"
            )
        self.id = id

    def flip(self) -> Self:
        """Flips the piece over, as if reflected across the x-axis

        Returns:
            Piece: A new piece that is a mirror image of the original
        """
        reflected = (square.reflect_across_x_axis() for square in self)
        move_y = max(square.y for square in self) + min(square.y for square in self)
        return Piece((square.translate(y=move_y) for square in reflected), self.id)

    def move(self: Iterable[Square], x: int, y: int) -> Self:
        """Moves piece a number of squares equal to `translation`

        Args:
            translation (tuple): A tuple indicating the number of squares the piece will move

        Returns:
            Self: A new piece that is the same shape of the original but offset by `translation`
        """
        return Piece((square.translate(x, y) for square in self), self._id)

    def rotate(self, reps: int = 1) -> Self:
        """Rotates a piece 90 degrees counter-clockwise the indicated number of times

        Args:
            reps (int, optional): The number of 90 degree reotations to perform. Defaults to 1.

        Returns:
            Self: A new piece that is the same shape o the original rotated 90 degrees counter-clockwise the indicated number of times
        """
        min_reps = reps % 4
        rotated = []
        for square in self:
            _square: Square = deepcopy(square)
            for _ in range(min_reps):
                _square = _square.rotate_90deg_counter_clockwise()

            rotated.append(_square)

        return Piece(rotated, self.id)

    @classmethod
    def from_iterables(cls, iterables: Iterable[Iterable[int]], id: str) -> Self:
        squares = (Square(*iterable) for iterable in iterables)
        return Piece(squares, id)

    def __eq__(self, other: Self) -> bool:
        return all(pair[0] == pair[1] for pair in zip(self, other)) and self.id == other.id

    def __ne__(self, other: Self) -> bool:
        return not self.__eq__(other)
    
    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f'squares=({", ".join(str((s.x, s.y)) for s in self)})'
            f", id={repr(self.id)}"
            ")"
        )


class PieceTypeError(TypeError):
    pass
