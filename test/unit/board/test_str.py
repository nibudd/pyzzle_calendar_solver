from src.board import Board
from src.piece import Piece


def test_1x1_board_check():
    board = Board(1, 1)
    expected = "\n".join([
        "+ --- +",
        "|     |",
        "+ --- +"
    ])

    sut = str(board)

    assert sut == expected


def test_1x1_board_with_piece_X_check():
    board = Board(1, 1)
    expected = "\n".join([
        "+ --- +",
        "|  X  |",
        "+ --- +"
    ])
    piece = Piece.from_iterables(((0, 0),), "X")
    board.add_piece(piece)

    sut = str(board)

    assert sut == expected


def test_3x3_board_with_piece_L_check():
    board = Board(3, 3)
    expected = "\n".join([
        "+ --- + --- + --- +",
        "|  L  |     |     |",
        "+ --- + --- + --- +",
        "|  L  |     |     |",
        "+ --- + --- + --- +",
        "|  L  |  L  |     |",
        "+ --- + --- + --- +",
    ])
    piece = Piece.from_iterables((
        (0, 2), (0, 1), (0, 0), (1, 0)
    ), "L")
    board.add_piece(piece)

    sut = str(board)

    assert sut == expected