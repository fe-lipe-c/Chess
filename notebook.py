"""Notebook with exploration of chess.com api."""

import chess
import chess.svg

from chessdotcom_api import Player_Profile


# FEN

board = chess.Board("8/8/8/2k5/4K3/8/8/8 w - - 4 45")
board.legal_moves
board.fen()
# '8/8/8/2k5/4K3/8/8/8 w - - 4 45'
print(board)
# r n b q k b n r
# p p p p p p p p
# . . . . . . . .
# . . . . . . . .
# . . . . . . . .
# . . . . . . . .
# P P P P P P P P
# R N B Q K B N R

player_pieces = ["K"]
opponent_pieces = ["K", "Q"]
player_color = np.random.choice(["w", "b"])

number_pieces = len(player_pieces) + len(opponent_pieces)

for i in range(number_pieces):
    if i == 0:
        row = np.random.randint(1, 9)
        line = np.random.randint(1, 9)


games_pgn = []
for i in df["pgn"]:
    games_pgn.append(i.split("\n")[-2])

int(games_pgn[0].split(" ")[1].replace(".", ""))
games_pgn[0].split(" ")
# ['1.',
#  'd4',
#  '{[%clk',
#  '0:09:50.4]}',
#  '1...',
#  'e5',
#  '{[%clk',
#  '0:09:53.6]}',

# https://api.chess.com/pub/player/fe_lipe_br/games/2022/10

board = chess.Board()
board.legal_moves
# <LegalMoveGenerator at 0x7f8d4bd62690 (Nh3, Nf3, Nc3, Na3, h3, g3, f3, e3, d3, c3, b3, a3, h4, g4, f4, e4, d4, c4, b4, a4)>

chess.Move.from_uci("e2e4") in board.legal_moves
# True

board.push_san("e4")
board.legal_moves
# <LegalMoveGenerator at 0x7f38706d1b50 (Nh6, Nf6, Nc6, Na6, h6, g6, f6, e6, d6, c6, b6, a6, h5, g5, f5, e5, d5, c5, b5, a5)>

board.pop()
# Move.from_uci('e2e4')

board.legal_moves
# <LegalMoveGenerator at 0x7f387051b4d0 (Nh3, Nf3, Nc3, Na3, h3, g3, f3, e3, d3, c3, b3, a3, h4, g4, f4, e4, d4, c4, b4, a4)>

print(board)
# r n b q k b n r
# p p p p p p p p
# . . . . . . . .
# . . . . . . . .
# . . . . . . . .
# . . . . . . . .
# P P P P P P P P
# R N B Q K B N R

board.is_stalemate()
board.is_insufficient_material()
board.is_checkmate()
board.outcome()
