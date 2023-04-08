from src.piece import PieceService

class Board:
    def __init__(self, x: int, y: int) -> None:
        if type(x) != int or type(y) != int:
            raise BoardTypeError(f"Invalid arguments to {self.__class__.__name__}: {(type(x), type(y))}")
        
        self._board = {
            (i, j): None
            for i in range(x)
            for j in range(y)
        }

        self._x = x
        self._y = y

    def add_piece(self, piece: PieceService) -> None:
        for square in piece:
            key = (square.x, square.y)
            if self._board[key] is not None:
                raise PiecePlacementError(f"Can't place {piece} on occupied {square}: '{self._board[key]}'")

            self._board[key] = piece.id

    def _get_letter(self, x: int, y: int) -> str:
        letter = self._board[(x, y)]
        if letter is None:
            return " "

        return letter

    def __str__(self) -> str:
        top_rep = "+ --- "
        top_finish = "+"
        mid_rep = "|  {}  "
        mid_finish = "|"

        top = "".join([top_rep] * self._x + [top_finish])

        strings = []
        for y in range(self._y - 1, -1, -1):
            strings.append(top)
            
            mid_strings = []
            for x in range(0, self._x):
                letter = self._get_letter(x, y)
                mid_strings.append(mid_rep.format(letter))
            mid_strings.append(mid_finish)
            strings.append("".join(mid_strings))

        strings.append(top)
        return "\n".join(strings)

    
class BoardTypeError(TypeError):
    pass


class PiecePlacementError(Exception):
    pass