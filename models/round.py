#! /usr/bin/env python3
# coding: utf-8

import datetime

class Round:
    """Modèle du round"""

    def __init__(self, name_round=None, start_timestamp=None, end_timestamp=None):
        self.name_round = name_round
        self.start_timestamp = start_timestamp
        self.end_timestamp = end_timestamp
        self.players_list = []
        self.ranking_list = []
        self.match_list = []
        
    def add_match(self):
        self.match_list.append(match)
        