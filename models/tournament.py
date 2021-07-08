#! /usr/bin/env python3
# coding: utf-8

import datetime

class Tournament:
    """Modèle de tournoi"""

    def __init__(self, name=None, place=None, start_date=None, end_date=None, match_time=None, total_rounds=None, counter_rounds=None, description=None):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.total_rounds = total_rounds
        self.counter_rounds = counter_rounds
        self.list_rounds = []
        self.list_players = []
        self.match_time = match_time
        self.description = description

    def add_player(self, player):
        self.list_players.append(player)

    def add_round(self, round):
        self.list_rounds.append(round)

    def serializer(self):
        return {"name" : self.name,
                "place" : self.place,
                "star_date" : self.start_date,
                "end_date" : self.end_date,
                "total_rounds" : self.total_rounds,
                "counter_rounds" : self.counter_rounds,
                "rounds" : [round.serializer() for round in self.list_rounds],
                "players" : [player.serializer() for player in self.list_players],
                "match_time" : self.match_time,
                "description" : self.description}