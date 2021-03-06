#! /usr/bin/env python3
# coding: utf-8


class Match:
    """Modèle du match"""

    def __init__(
        self, white_player=None, black_player=None, white_score=None, black_score=None
    ):
        self.white_player = white_player
        self.black_player = black_player
        self.white_score = white_score
        self.black_score = black_score

    """
    def add_score(self):
        pass
    """

    def serializer(self):
        return {
            "white_player": self.white_player.serializer(),
            "black_player": self.black_player.serializer(),
            "white_score": self.white_score,
            "black_score": self.black_score,
        }
