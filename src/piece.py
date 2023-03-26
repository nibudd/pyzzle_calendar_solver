from typing import Iterable, Self

from src.square import Square


class Piece(tuple):
    def __init__(self, iterable: Iterable) -> Self:
        if any(not isinstance(val, Square) for val in iterable):
            raise InvalidPieceError("Invalid values in tuple. All values must be `Square`s")

        tuple.__init__(iterable)

    def flip(self: tuple[Square]) -> Self:
        """Flips the piece over, as if reflected across the x-axis

        Returns:
            Piece: A new piece that is a mirror image of the original
        """
        reflected = (square.reflect_across_x() for square in self)
        translation = (0, 2 * max(square.y for square in self))
        return Piece(square.translate(translation) for square in reflected)

    def move(self: tuple[Square], translation: tuple) -> Self:
        """Moves piece a number of squares equal to `translation`

        Args:
            translation (tuple): A tuple indicating the number of squares the piece will move

        Returns:
            Self: A new piece that is the same shape of the original but offset by `translation`
        """
        return Piece(square.translate(translation) for square in self)


class InvalidPieceError(Exception):
    pass
