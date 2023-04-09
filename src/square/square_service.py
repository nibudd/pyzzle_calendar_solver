from typing import Self

from .square import Square


def reflect(square: Square) -> Square:
    """Creates a reflection of the square across the x-axis

    Args:
        square (Square): The square to be reflected

    Returns:
        Square: A Square that is the original Square's reflection in across the x-axis
    """
    return Square(square.x, -square.y)

def rotate(square: Square) -> Square:
    """Creates a 90-degree counter-clockwise rotation of the original square's position vector

    Args:
        square (Square): The position vector of the square to be rotated

    Returns:
        Square: The 90-degree counter-clockwise rotation of the original square's position vector
    """
    return Square(-square.y, square.x)

def translate(square: Square, move: Square) -> Square:
    """Creates a translation of the original square by move

    Args:
        square (Square): The original position vector
        move (Square): A position vector to be added on to square

    Returns:
        Square: The sum of position vectors `square` and `move`
    """
    return Square(square.x + move.x, square.y + move.y)
