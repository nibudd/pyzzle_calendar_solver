from typing import Self


class Square:
    def __init__(self, x: int, y: int) -> None:
        """A square on the game board

        Args:
            x (int): The x-coordinate of the sqaure
            y (int): The y-coordinate of the sqaure

        Raises:
            SquareTypeError: Raised if any input is not an `int`
        """
        if type(x) != int or type(y) != int:
            raise SquareTypeError(
                f"Invalid arguments to {self.__class__.__name__}: ({type(x), type(y)})"
            )
        self.x = x
        self.y = y

    def reflect_across_x_axis(self) -> Self:
        """Creates a reflection of the square across the x-axis

        Returns:
            Square: A Square that is the original Square's reflection in across the x-axis
        """
        return Square(self.x, -self.y)

    def translate(self, x: int = 0, y: int = 0) -> Self:
        """Creates a translation of the original Square

        Args:
            translation (tuple): how the new Square is displaced from the first

        Returns:
            Square: The translation of the original Square
        """
        if type(x) != int or type(y) != int:
            raise SquareTypeError(
                f"Invalid arguments to {self.translate.__qualname__}: ({type(x), type(y)})"
            )

        return Square(self.x + x, self.y + y)

    def rotate_90deg_counter_clockwise(self) -> Self:
        """Creates a 90-degree counter-clockwise rotation of the original Square

        Returns:
            Square: The 90-degree counter-clockwise rotation of the original Square
        """
        return Square(-self.y, self.x)

    def __eq__(self, other: Self) -> bool:
        return (self.x == other.x) and (self.y == other.y)
    
    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"x={self.x}"
            f", y={self.y}"
            ")"
        )


class SquareTypeError(TypeError):
    pass
