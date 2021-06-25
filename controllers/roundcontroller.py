#! /usr/bin/env python3
# coding: utf-8

from datetime import datetime
from views.roundview import RoundView

"""Models"""
from models.round import Round
"""Views"""

"""Controllers"""
from controllers.matchcontroller import MatchController
"""Utils"""


class RoundController:
    """Gestion des rounds"""
    
    def __init__(self):
        self.round = Round()
        #self.tournament = current_tournament
        #self.total_rounds = self.tournament.total_rounds
        #self.counter_rounds = self.tournament.counter_rounds
        #self.list_match = []
        #self.manage_round()
    


    def first_round(self, tournament_list_players, counter_rounds):
        """premier round"""
        name = RoundController.get_name_round(counter_rounds)
        start_timestamp = datetime.now().strftime("%d-%m-%Y")
        self.list_match = []
        RoundView.display_name_round(name)        

        """Tri par classement elo"""
        list_player = sorted(tournament_list_players, key=lambda player: player.ranking_elo)

        """affectation des joueurs pour les matchs de la première ronde"""
        for i in range(4):
            self.list_match.append(MatchController.match_result(list_player[i], list_player[i+4]))
        end_timestamp = datetime.now().strftime("%d-%m-%Y")

        """Classement des joueurs en fonction de leurs score"""
        list_ranking = sorted(list_player, key=lambda player: player.score)        

        self.round = Round(name, start_timestamp, end_timestamp)
        self.round.add_player(list_player)
        self.round.add_ranking(list_ranking)
        self.round.add_match(self.list_match)
        return self.round
        

    def next_round(self, previous_round, counter_rounds):
        name = RoundController.get_name_round(counter_rounds)
        start_timestamp = datetime.now().strftime("%d-%m-%Y")
        RoundView.display_name_round(name)
        
        """affectation des joueurs pour les matchs de la première ronde"""
        list_player = previous_round.ranking_list   
        i = 0     
        while i < 8:
            self.list_match.append(MatchController.match_result(list_player[i], list_player[i+1]))
            i+=2
        end_timestamp = datetime.now().strftime("%d-%m-%Y")

        """Classement des joueurs en fonction de leurs score"""    
        list_ranking = sorted(list_player, key=lambda player: player.score)   

        self.round = Round(name, start_timestamp, end_timestamp)
        self.round.add_player(list_player)
        self.round.add_ranking(list_ranking)
        self.round.add_match(self.list_match)
        return self.round

        """ tri par classement puis par rang en cas d'également pour réaliser l'apariement du round suivant """  
    
    @staticmethod
    def get_name_round(counter_rounds):
        return "Round " + str(counter_rounds)
    
    def end_round():
        pass
    
        
        """
        liste = [(12, 45),(56, 67), (34,1),(89,90),(45,6), (67,23)]

        print(liste)
        liste2 = sorted(liste, key= lambda x : x[1])
        print(liste)
        print(liste2)
        """
