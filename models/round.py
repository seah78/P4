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
    
    def add_player(self, list_player):
        self.players_list.extend(list_player)
        
    def add_ranking(self, list_ranking):
        self.ranking_list.extend(list_ranking)

    def add_match(self, list_match):
        self.match_list.extend(list_match)
    
    def serializer(self):
        return {"name_round" : self.name_round,
                "start_timestamp" : self.start_timestamp,
                "end_timestamp" : self.end_timestamp,
                "players" : [player.serializer() for player in self.players_list],
                "matchs" : [match.serializer() for match in self.match_list]}
        