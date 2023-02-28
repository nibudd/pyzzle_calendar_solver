import pickle


class Square(tuple):
    def __init__(self, tup: tuple) -> "Square":
        if len(tup) != 2:
            raise InvalidSquareError(f"Invalid tuple length of {len(tup)}. Tuple must be of length 2.")

        if any(not isinstance(val, int) for val in tup):
            raise InvalidSquareError("Invalid values int tuple. All values must be `int`s")

        super().__init__()
    
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
        return Square((-self.row, self.col))

    def translate(self, translation: tuple) -> "Square":
        move = Square(translation)
        return Square((self.row + move.row, self.col + move.col))

    def rotate(self) -> "Square":
        return Square((self.col, -self.row))


class InvalidSquareError(Exception):
    pass
