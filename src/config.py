from dataclasses import dataclass

from board import BoardConfig
from piece import Piece


@dataclass
class Config:
    board: BoardConfig
    pieces: list[Piece]