import pickle
from typing import Iterable


class Square(tuple):
    def __init__(self, iterable: Iterable) -> "Square":
        if len(iterable) != 2:
            raise InvalidSquareError(f"Invalid tuple length of {len(iterable)}. Tuple must be of length 2.")

        if any(not isinstance(val, int) for val in iterable):
            raise InvalidSquareError("Invalid values in tuple. All values must be `int`s")

        tuple.__init__(iterable)
    
    @property
    def row(self) -> int:
        return self[0]

    @property
    def col(self) -> int:
        return self[1]

    @property
    def hash(self) -> str:
        return pickle.dumps(tuple(self))

    def reflect(self) -> "Square":
        """Creates a reflection of the square across the 0-axis

        Returns:
            Square: A Square that is the original Square's reflection in across the 0-axis
        """        
        return Square((-self.row, self.col))

    def translate(self, translation: tuple) -> "Square":
        """Creates a translation of the original Square

        Args:
            translation (tuple): how the new Square is displaced from the first

        Returns:
            Square: The translation of the original Square
        """        
        move = Square(translation)
        return Square((self.row + move.row, self.col + move.col))

    def rotate(self) -> "Square":
        """Creates a 90-degree counter-clockwise rotation of the original Square

        Returns:
            Square: The 90-degree counter-clockwise rotation of the original Square 
        """        
        return Square((self.col, -self.row))


class InvalidSquareError(Exception):
    pass
