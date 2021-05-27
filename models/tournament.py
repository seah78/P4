#! /usr/bin/env python3
# coding: utf-8

import datetime

DEFAULT_ROUNDS = 4

class Tournament:
    """docstrings"""

    def __init__(self):
        self.name = ""
        self.place = ""
        self.start_date = ""
        self.end_date = ""
        self.number_rounds=DEFAULT_ROUNDS
        self.list_rounds = []
        self.list_players = []
        self.time = ""
        self.description = ""

    def creation_tournament(self):
        pass

	def add_player(self):
		pass

	def add_round(self):
		pass

	def order_ranking_player(self):
		pass

