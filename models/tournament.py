#! /usr/bin/env python3
# coding: utf-8

import datetime

DEFAULT_ROUNDS = 4

class Tournament:
    """docstrings"""

    def __init__(self, name=None, place=None, start_date=None, end_date=None, match_time=None, description=None):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.number_rounds=DEFAULT_ROUNDS
        self.list_rounds = []
        self.list_players = []
        self.match_time = match_time
        self.description = description

    def add_player(self, player):
        self.list_players.append(player)

    def add_round(self):
        self.list_rounds.append(round)


"""
    def reload_tounament(self):
        pass
"""


"""
    def order_ranking_player(self):
        pass
"""
