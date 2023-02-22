"""Utility functions for the project."""

import numpy as np


def place_kings(brd):
    """Place kings on the board."""
    while True:
        (
            rank_white,
            file_white,
            rank_black,
            file_black,
        ) = np.random.randint(0, 8, size=4)
        diff_list = [
            abs(rank_white - rank_black),
            abs(file_white - file_black),
        ]
        if sum(diff_list) > 2 or set(diff_list) == set([0, 2]):
            brd[rank_white][file_white] = "K"
            brd[rank_black][file_black] = "k"
            break


def pawn_on_promotion_square(piece, piece_rank):
    """Check if pawn is in the last row."""
    if piece == "P" and piece_rank == 0:
        return True
    elif piece == "p" and piece_rank == 7:
        return True
    return False


def fen_from_board(brd):
    """Create FEN from board.""" ""
    fen = ""
    for x in brd:
        n = 0
        for y in x:
            if y == " ":
                n += 1
            else:
                if n != 0:
                    fen += str(n)
                fen += y
                n = 0
        if n != 0:
            fen += str(n)
        fen += "/" if fen.count("/") < 7 else ""
    fen += " w - - 0 1"
    return fen


def populate_board_det(brd, w_pieces, b_pieces):
    """Populate the board with the pieces."""
    for x in range(2):
        if x == 0:
            pieces = w_pieces
        else:
            pieces = b_pieces

        while len(pieces) != 0:
            print(pieces)
            piece_rank, piece_file = np.random.randint(0, 8, size=2)
            piece = pieces[-1]
            print(piece, piece_rank, piece_file)
            promotion = pawn_on_promotion_square(piece, piece_rank)
            if brd[piece_rank][piece_file] == " " and promotion is False:
                brd[piece_rank][piece_file] = piece
                pieces.pop()


clean_board = [[" " for x in range(8)] for y in range(8)]
b_pieces = ["Q"]
w_pieces = []
place_kings(clean_board)
populate_board_det(clean_board, w_pieces, b_pieces)
# Q 5 4
clean_board
pawn_on_promotion_square("Q", 5)
fen_from_board(clean_board)


type(rank_white)
clean_board[rank_white, rank_black]

teste = [1, 2, 3]
teste.pop()
teste
