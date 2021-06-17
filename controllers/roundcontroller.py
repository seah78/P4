#! /usr/bin/env python3
# coding: utf-8

from models.round import Round


class RoundController:
    
    def __init__(self, current_tournament):
        self.tournament = current_tournament
        self.total_rounds = self.tournament.total_rounds
        self.counter_rounds = self.tournament.counter_rounds
        print("Dans le roundcontroller")
  
    """
    liste = [(12, 45),(56, 67), (34,1),(89,90),(45,6), (67,23)]

    print(liste)
    liste2 = sorted(liste, key= lambda x : x[1])
    print(liste)
    print(liste2)
    """  
  
  
    def first_round(self):
        pass

    def next_round(self):
        pass
