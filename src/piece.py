from typing import Iterable

from src.square import Square


class Piece(tuple):
    def __init__(self, iterable: Iterable) -> "Piece":
        if any(not isinstance(val, Square) for val in iterable):
            raise InvalidPieceError("Invalid values in tuple. All values must be `Square`s")

        tuple.__init__(iterable)

    def flip(self) -> "Piece":
        reflected = (square.reflect() for square in self)
        translation = (max(square.row for square in self), 0)
        return Piece(square.translate(translation) for square in reflected)


class InvalidPieceError(Exception):
    pass
