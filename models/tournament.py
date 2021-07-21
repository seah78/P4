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
                "start_date" : self.start_date,
                "end_date" : self.end_date,
                "total_rounds" : self.total_rounds,
                "counter_rounds" : self.counter_rounds,
                "rounds" : [round.serializer() for round in self.list_rounds],
                "players" : [player.serializer() for player in self.list_players],
                "match_time" : self.match_time,
                "description" : self.description}


    def deserializer(self):
        database = TinyDB('utils/database.json', indent=4)
        Tournaments = Query()
        tournament = database.search(Tournaments.name == 'Test Serializer')[0]

        self.name = tournament["name"]
        self.place = tournament["place"]
        self.start_date = tournament["start_date"]
        self.end_date = tournament["end_date"]
        self.total_rounds = tournament["total_rounds"]
        self.counter_rounds = tournament["counter_rounds"]
        self.time = tournament["match_time"]
        self.description = tournament["description"]

        
        for player in tournament["players"]:
            reload_player = Player(player["name"], player["first_name"], player["birth_date"], player["gender"], player["ranking_elo"], player["score"]) #ajouter oppoant
            self.add_player(reload_player)
        player_list = []
        ranking_list = []
        match_list = []
        for round in tournament["rounds"]:
            for player_round in round["players"]:
                self.list_players.append(Player(player_round["name"], player_round["first_name"], player_round["birth_date"], player_round["gender"], player_round["ranking_elo"], player_round["score"]))
            for match_round in round["matchs"]:
                .append(Match(match_round["white_player"], match_round["black_player"], match_round["white_score"], match_round["black_score"]))

            reload_round = Round(round["name_round"], round["start_timestamp"], round["end_timestamp"])
            reload_round.add_player(player_list)
            reload_round.add_ranking(ranking_list)
            reload_round.add_match(match_list)
            reload_tournament.add_round(reload_round)


    @staticmethod
    def deserializer():
        database = TinyDB('utils/database.json', indent=4)

        
        Tournaments = Query()
        tournament = database.search(Tournaments.name == 'Test Serializer')[0]
        print(tournament)
        
        
        name = tournament["name"]
        place = tournament["place"]
        start_date = tournament["start_date"]
        end_date = tournament["end_date"]
        total_rounds = tournament["total_rounds"]
        counter_rounds = tournament["counter_rounds"]
        time = tournament["match_time"]
        description = tournament["description"]
        reload_tournament = Tournament(name, place, start_date, end_date, time, total_rounds, counter_rounds, description)

        
        for player in tournament["players"]:
            reload_player = Player(player["name"], player["first_name"], player["birth_date"], player["gender"], player["ranking_elo"], player["score"]) #ajouter oppoant
            reload_tournament.add_player(reload_player)
        player_list = []
        ranking_list = []
        match_list = []
        for round in tournament["rounds"]:
            for player_round in round["players"]:
                player_list.append(Player(player_round["name"], player_round["first_name"], player_round["birth_date"], player_round["gender"], player_round["ranking_elo"], player_round["score"]))
            for match_round in round["matchs"]:
                match_list.append(Match(match_round["white_player"], match_round["black_player"], match_round["white_score"], match_round["black_score"]))

            reload_round = Round(round["name_round"], round["start_timestamp"], round["end_timestamp"])
            reload_round.add_player(player_list)
            reload_round.add_ranking(ranking_list)
            reload_round.add_match(match_list)
            reload_tournament.add_round(reload_round)
        return reload_tournament