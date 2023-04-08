from typing import Self

from .square import Square


def reflect(square: Square) -> Square:
    """Creates a reflection of the square across the x-axis

    Returns:
        Square: A Square that is the original Square's reflection in across the x-axis
    """
    return Square(square.x, -square.y)

def rotate(square: Square) -> Square:
    """Creates a 90-degree counter-clockwise rotation of the original Square

    Returns:
        Square: The 90-degree counter-clockwise rotation of the original Square
    """
    return Square(-square.y, square.x)

def translate(square: Square, move: Square) -> Square:
    """Creates a translation of the original square by move

    Args:
        translation (tuple): how the new Square is displaced from the first

    Returns:
        Square: The translation of the original Square
    """
    return Square(square.x + move.x, square.y + move.y)
