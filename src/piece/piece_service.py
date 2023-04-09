from copy import deepcopy
from typing import Iterable, Self

from .piece import Piece
from src import square


def flip(piece: Piece) -> Piece:
    """Flips the piece over, as if reflected across the x-axis

    Args:
        piece (Piece): A piece to flip in place across an x-parallel axis

    Returns:
        Piece: A flipped version of the original piece
    """
    reflected = (square.reflect(s) for s in piece.squares)

    move_y = max(s.y for s in piece.squares) + min(s.y for s in piece.squares)
    move = square.Square(0, move_y)

    return Piece((square.translate(s, move) for s in reflected), piece.id)

def move(piece: Piece, move: square.Square) -> Piece:
    """Moves piece a number of squares represented by `move`

    Args:
        piece (Piece): The piece to be moved
        move (Square): Represents the translation to be performed on piece

    Returns:
        Self: A new piece that is the same shape of the original but offset by `move`
    """
    return Piece((square.translate(s, move) for s in piece.squares), piece.id)

def rotate(piece: Piece, reps: int = 1) -> Self:
    """Rotates a piece 90 degrees counter-clockwise the indicated number of times

    Args:
        piece (Piece): The piece to be rotated
        reps (int, optional): The number of counter-clockwise 90 degree reotations to perform. Negative numbers cause clockwise rotations. Defaults to 1.

    Returns:
        Self: A new piece that is the same shape as the original rotated 90 degrees counter-clockwise the indicated number of times
    """
    max_reps = 4
    _reps = reps % max_reps
    rotated = []

    for sq in piece.squares:        
        for _ in range(_reps):
            sq = square.rotate(sq)

        rotated.append(sq)

    return Piece(rotated, piece.id)
