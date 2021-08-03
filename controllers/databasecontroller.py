#! /usr/bin/env python3
# coding: utf-8

from models.tournament import Tournament
from models.player import Player
from models.round import Round
from models.match import Match


from tinydb import TinyDB, Query, where


class DataBaseController:
    pass
    
    """
    def __init__(self):
        self.tournament = None

        
    def __call__(self):
        self.deserializer()
        return True
    
    @staticmethod
    def save_tournament(serializer):
        database = TinyDB('utils/database.json', indent=4)
        tournament = database.table("tournament")
        tournament.insert(serializer)
    
    
    def reload_tournament(self):
        pass
    """
    
    """
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
        """


    



