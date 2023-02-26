"""Notebook to database module."""

import pandas as pd
import re
from chessdotcom_api import Player_Profile
import chess


def get_games(username, year, month):
    """Get games from chess.com api."""

    player = Player_Profile(username)

    df = player.games(year, month)

    games_pgn = []
    for i in df["pgn"]:
        games_pgn.append(i.split("\n")[-2])

    return games_pgn, df


def get_moves(game_pgn):
    """Get moves from game_pgn."""

    pattern = r"\{.*?\}"
    pattern2 = r"\d+\.{3}"
    pattern3 = r"\d+\.{1}"
    # pattern matches everything between curly brackets

    new_string = re.sub(pattern, "", game_pgn)
    new_string = re.sub(pattern2, "", new_string)
    new_string = re.sub(pattern3, "", new_string)
    # replaces all matches with an empty string

    return new_string.split()[:-1]


username = "fe_lipe_br"
games, df = get_games(username, 2022, 10)

white = df["white.username"].iloc[0]
black = df["black.username"].iloc[0]
moves_pgn = get_moves(games[0])

board_fen = []
move_list = []
board = chess.Board()
board_fen.append(board.fen())
for move in moves_pgn:
    board.push_san(move)
    board_fen.append(board.fen())
    move_list.append(move)

white_len = [white] * len(board_fen)
black_len = [black] * len(board_fen)
white_len
black_len

df_db = pd.DataFrame(
    {"white_username": white_len, "black_username": black_len, "fen": board_fen}
)
df_db

board.fen()
board.fen()
# 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
board.push_san("e4")
board.fen()
# 'rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1'

df.to_feather("games.feather")
