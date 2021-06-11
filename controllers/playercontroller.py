#! /usr/bin/env python3
# coding: utf-8
# 

import datetime

from models.player import Player
from views.playerview import PlayerView 
from views.errorview import ErrorView


    
    
class PlayerController:    

    def get_player_name():
        name = PlayerView.get_name_player()
        while not name.isalpha():
            ErrorView.get_alpha_message_error("Nom")
            name = PlayerView.get_name_player()
        return name

    def get_player_first_name():
        first_name = PlayerView.get_first_name_player()
        while not first_name.isalpha():
            ErrorView.get_alpha_message_error("Prénom")
            first_name = PlayerView.get_first_name_player()
        return first_name

    def get_player_birth_date():
        loop_valid_date = False
        while loop_valid_date == False:
            birth_date = PlayerView.get_birth_date_player()
            try:
                birth_date = datetime.datetime.strptime(birth_date, '%d-%m-%Y')
                loop_valid_date = True
            except ValueError:
                ErrorView.get_date_message_error()
                loop_valid_date = False
        return birth_date


 

        

    def get_player_gender():
        pass
        """
        gender = PlayerView.get_gender_player()
        while not gender.isalpha():
            ErrorManagement.get_alpha_message_error("Nom")
            gender = TournamentView.get_name()
        return gender
        """

    def get_player_ranking_elo():
        pass
        """
        ranking_elo = PlayerView.get_ranking_elo_player()
        while not name.isalpha():
            ErrorManagement.get_alpha_message_error("Nom")
            ranking_elo = TournamentView.get_name()
        return ranking_elo
        """