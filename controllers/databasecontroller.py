#! /usr/bin/env python3
# coding: utf-8

from models.tournament import Tournament
from models.player import Player
from models.round import Round
from models.match import Match


from tinydb import TinyDB, Query

class DataBase:
    
    def __init__(self):
        self.tournament = None
        self.json = TinyDB('utils/database.json', indent=4)
    
    @staticmethod
    def save_database(serializer):
        database = TinyDB('utils/database.json', indent=4)
        database.truncate()
        database.insert(serializer)
    
    
    def reload_database(self):
        pass
    
    
    def deserializer(self):
        name = self.json["name"]
        place = self.json["place"]
        start_date = self.json["start_date"]
        end_date = self.json["end_date"]
        total_rounds = self.json["total_rounds"]
        counter_rounds = self.json["counter_rounds"]
        time = self.json["match_time"]
        description = self.json["description"]
        self.tournament = Tournament(name, place, start_date, end_date, time, total_rounds, counter_rounds, description)

        
        for player in self.json["players"]:
            reload_player = Player(player["name"], player["first_name"], player["birth_date"], player["gender"], player["ranking_elo"], player["score"]) #ajouter oppoant
            self.tournament.add_player(reload_player)

        for round in self.json["rounds"]:
            reload_round = Round()


        self.name_round = name_round
        self.start_timestamp = start_timestamp
        self.end_timestamp = end_timestamp
        self.players_list = []
        self.ranking_list = []
        self.match_list = []    

        while self.tournament.counter_rounds != total_rounds + 1:
            if self.tournament.counter_rounds == 1:
                self.tournament.add_round(RoundController.first_round(self, self.tournament.list_players, self.tournament.counter_rounds))
            else:
                self.tournament.add_round(RoundController.next_round(self, self.tournament.list_players , self.tournament.counter_rounds))
            self.tournament.counter_rounds += 1

    
    
    
    """
    def reload_tournament(self):
        self.tournament = None # je met none car dans le cas normal il serait à None.
        #Il va aller lire le json et récupérer l'information du tournoi qu'on veut reprendre (Dans notre exemple self.json)
        self.deserializer()
        number_round_to_run = 4 - len(self.json["rounds"])
        print(number_round_to_run)
        
        if number_round_to_run == 4:
            pass
            #run_first_round()
        else:
            for i in range(len(self.json["rounds"]) + 1, 5):
                pass
                #run_round(i)
    
    def deserializer(self):
        self.tournament = Tournament(self.json["name"], self.json["place"])
        self.tournament.players = []
        
        for player in self.json["players"]:
            reload_player = Player(player["name"], player["elo"], player["score"])
            self.tournament.add_player(reload_player)
            
        for round in self.json["rounds"]:
            reload_round = Round(round["number"])
            for match in round["matchs"]:
                player1 = Player(match["player1"]["name"], match["player1"]["elo"], match["player1"]["score"])
                player2 = Player(match["player2"]["name"], match["player1"]["elo"], match["player1"]["score"])
                
                reload_match = Match(player1, player2, match["score_player1"], match["score_player2"])
                
                reload_round.add_reload_match(reload_match)
            self.tournament.add_round(reload_round)
            #return tournament
        print(self.tournament.serializer())
    """    


"""
database = TinyDB('database.json')


database.insert({"type": "apple", "count": 7})
"""