"""Notebook to database module."""

import pandas as pd
from chessdotcom_api import Player_Profile

username = "fe_lipe_br"

player = Player_Profile(username)
player.player_profile()

df = player.games(2022, 10)

df.columns
# Index(['url', 'pgn', 'time_control', 'end_time', 'rated', 'tcn', 'uuid',
#        'initial_setup', 'fen', 'time_class', 'rules', 'white.rating',
#        'white.result', 'white.@id', 'white.username', 'white.uuid',
#        'black.rating', 'black.result', 'black.@id', 'black.username',
#        'black.uuid', 'accuracies.white', 'accuracies.black', 'start_time'],
print(df.head(1)["pgn"][0])

df.to_feather("games.feather")
