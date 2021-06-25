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
    
    def __init__(self, current_tournament):
        self.round = None
        
        
        self.tournament = current_tournament
        self.total_rounds = self.tournament.total_rounds
        self.counter_rounds = self.tournament.counter_rounds
        self.list_match = []
        self.manage_round()
        
    def manage_round(self):
        """Gestion des rounds"""
        while self.counter_rounds != self.total_rounds:
            if self.counter_rounds == 1:
                self.first_round()
            else:
                self.next_round(self.counter_rounds)
            self.counter_rounds += 1

    def first_round(self):
        """premier round"""
        name = self.get_name_round()
        start_timestamp = datetime.now().strftime("%d-%m-%Y")
        RoundView.display_name_round(name)        
        list_player = sorted(self.tournament.list_players, key=lambda player: player.ranking_elo)
        for i in range(0,4):
            self.list_match.append(MatchController.match_result(list_player[i], list_player[i+4]))
        end_timestamp = datetime.now().strftime("%d-%m-%Y")

        
        """
        self.name_round = name_round
        self.start_timestamp = start_timestamp
        self.end_timestamp = end_timestamp
        self.players_list = []
        self.ranking_list = []
        self.match_list = []
        """
        self.round = Round(name, start_timestamp, end_timestamp, list_player)

    def next_round(self):
        name = self.get_name_round()
        start_timestamp = datetime.now().strftime("%d-%m-%Y")
        RoundView.display_name_round(name)
        
        """ tri par classement puis par rang en cas d'également pour réaliser l'apariement du round suivant """  
    
    def get_name_round(self):
        return "Round " + str(self.counter_rounds)
    
    def end_round():
        pass
    
        
        """
        liste = [(12, 45),(56, 67), (34,1),(89,90),(45,6), (67,23)]

        print(liste)
        liste2 = sorted(liste, key= lambda x : x[1])
        print(liste)
        print(liste2)
        """
