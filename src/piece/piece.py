from dataclasses import dataclass
from typing import Self

from ..square import Square

@dataclass
class Piece:
    squares: tuple[Square]
    id: str

    def __eq__(self, other: Self) -> bool:
        return (
            all(s1 == s2 for s1, s2 in zip(self.squares, other.squares))
            and self.id == other.id
        )