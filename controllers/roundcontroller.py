#! /usr/bin/env python3
# coding: utf-8

from models.round import Round


class RoundController:
    
    def __init__(self, current_tournament):
        self.tournament = current_tournament
        self.total_rounds = self.tournament.total_rounds
        self.counter_rounds = self.tournament.counter_rounds
        print("Dans le roundcontroller")
  
    def first_round(self):
        pass

    def other_round(self):
        pass
 


