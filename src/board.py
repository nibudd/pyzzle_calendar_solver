from src.piece import Piece

class Board:
    def __init__(self, x: int, y: int) -> None:
        if type(x) != int or type(y) != int:
            raise BoardTypeError(f"Invalid arguments to {self.__class__.__name__}: {(type(x), type(y))}")
        
        self._board = {
            (i, j): None
            for i in range(x)
            for j in range(y)
        }

    def add_piece(self, piece: Piece) -> None:
        for square in piece:
            key = (square.x, square.y)
            if self._board[key] is not None:
                raise PiecePlacementError(f"Can't place {piece} on occupied {square}: '{self._board[key]}'")

            self._board[key] = piece.id

    
class BoardTypeError(TypeError):
    pass


class PiecePlacementError(Exception):
    pass