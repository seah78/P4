#! /usr/bin/env python3
# coding: utf-8

from datetime import datetime

from models.round import Round


class RoundController:
    
    def __init__(self, current_tournament):
        self.tournament = current_tournament
        self.total_rounds = self.tournament.total_rounds
        self.counter_rounds = self.tournament.counter_rounds
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


        print(name)        
        print(start_timestamp)
        for i in self.tournament.list_players:
            print(i)
        
        list_player = sorted(self.tournament.list_players, key=lambda player: player[self.tournament.list_players.ranking_elo])
        
        for i in list_player:
            print(i)
        
        liste = [(12, 45),(56, 67), (34,1),(89,90),(45,6), (67,23)]

        print(liste)
        liste2 = sorted(liste, key= lambda x : x[1])
        print(liste)
        print(liste2)
        
        

        



    def next_round(self, counter_round):
        pass
    
    def get_name_round(self):
        return "Round " + str(self.counter_rounds)
    
    def end_round():
        pass
