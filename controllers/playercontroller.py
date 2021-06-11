#! /usr/bin/env python3
# coding: utf-8
# 

import datetime

from models.player import Player
from views.playerview import PlayerView 
from views.errorview import ErrorView

    
class PlayerController:    

    def get_player_name():
        """Récupération du nom du joueur"""
        name = PlayerView.get_name_player()
        while not name.isalpha():
            ErrorView.get_alpha_message_error("Nom")
            name = PlayerView.get_name_player()
        return name

    def get_player_first_name():
        """Récupération du prénom du joueur"""
        first_name = PlayerView.get_first_name_player()
        while not first_name.isalpha():
            ErrorView.get_alpha_message_error("Prénom")
            first_name = PlayerView.get_first_name_player()
        return first_name

    def get_player_birth_date():
        """Récupération de la date de naissance"""
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
        """Récupération du sexe"""
        gender = PlayerView.get_gender_player()
        while gender != "M" or gender != "F":
            ErrorView.get_gender_message_error()
            gender = PlayerView.get_gender_player()
        return gender

    def get_player_ranking_elo():
        """Récupération du classement elo"""
        while True:
            try:
                ranking_elo = PlayerView.get_ranking_elo_player()
                if not ranking_elo > 0:
                    raise ValueError
            except ValueError:
                ErrorView.get_int_message_error("Classement Elo")
            else:
                break
        return ranking_elo