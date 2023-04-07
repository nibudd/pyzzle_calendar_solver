from dataclasses import dataclass

from board import BoardConfig
from piece import PieceConfig


@dataclass
class Config:
    board: BoardConfig
    pieces: list[PieceConfig]