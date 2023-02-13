"""Some class and functions to get data from chess.com API."""

import pandas as pd
import requests


class Player_Profile:
    """Player profile class."""

    def __init__(self, username):
        """Initialize."""
        self.username = username
        self.profile = self.player_profile()
        self.stats = self.player_stats()
        # self.online = self.isonline()

    def player_profile(self):
        """Get player profile."""
        url = "https://api.chess.com/pub/player/" + self.username
        response = requests.get(url).json()
        return pd.json_normalize(response)

    def player_stats(self):
        """Get player stats."""
        url = "https://api.chess.com/pub/player/" + self.username + "/stats"
        response = requests.get(url).json()
        return pd.json_normalize(response)

    def isonline(self):
        """Check if player is online."""
        url = "https://api.chess.com/pub/player/" + self.username + "/is-online"
        response = requests.get(url).json()
        return response["online"]

    def games(self, year, month):
        """Get player games."""
        url = (
            "https://api.chess.com/pub/player/"
            + self.username
            + "/games/"
            + str(year)
            + "/"
            + str(month)
        )
        response = requests.get(url).json()
        return pd.json_normalize(response["games"])


def titled_players(self, title):
    """Get titled players.

    Valid title abbreviations are: GM, WGM, IM, WIM, FM, WFM, NM, WNM, CM, WCM.
    """
    url = "https://api.chess.com/pub/titled/" + title
    response = requests.get(url).json()
    return pd.DataFrame(response["players"], columns=["username"])
