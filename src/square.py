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
    def x(self) -> int:
        return self[0]

    @property
    def y(self) -> int:
        return self[1]

    @property
    def hash(self) -> str:
        return pickle.dumps(tuple(self))

    def reflect_across_x(self) -> "Square":
        """Creates a reflection of the square across the x-axis

        Returns:
            Square: A Square that is the original Square's reflection in across the x-axis
        """        
        return Square((self.x, -self.y))

    def translate(self, translation: tuple) -> "Square":
        """Creates a translation of the original Square

        Args:
            translation (tuple): how the new Square is displaced from the first

        Returns:
            Square: The translation of the original Square
        """        
        move = Square(translation)
        return Square((self.x + move.x, self.y + move.y))

    def rotate(self) -> "Square":
        """Creates a 90-degree counter-clockwise rotation of the original Square

        Returns:
            Square: The 90-degree counter-clockwise rotation of the original Square 
        """        
        return Square((self.y, -self.x))


class InvalidSquareError(Exception):
    pass
