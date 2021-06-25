#! /usr/bin/env python3
# coding: utf-8

"""Models"""
from models.match import Match
"""Views"""
from views.matchview import MatchView
from views.errorview import ErrorView
"""Controllers"""

"""Utils"""


class MatchController:
    """Gestion des matchs"""

    
    
    
      
    @staticmethod
    def get_match_result(white_player, black_player):
        """récupération du résultat d'un match"""
        while True:
            try:
                match_result = MatchView.get_result_match(white_player, black_player)
                if match_result < 1 or match_result > 3:
                    raise ValueError
            except ValueError:
                ErrorView.get_int_message_error("Résultat d'un match")
            else:
                break
        return match_result

    @staticmethod
    def match_result(white_player, black_player):
        """ enregistrement du score """
        match_result = MatchController.get_match_result(white_player, black_player)
        if match_result == 1:
            white_score = 1.0
            black_score = 0.0
        elif match_result == 2:
            white_score = 0.5
            black_score = 0.5
        else:
            white_score = 0.0
            black_score = 1.0
        return  Match(white_player, black_player, white_score, black_score)
