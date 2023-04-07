from dataclasses import dataclass

import square

@dataclass
class PieceConfig:
    squares: list[square.SquareConfig]
    id: str