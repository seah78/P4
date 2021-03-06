#! /usr/bin/env python3
# coding: utf-8
#

import datetime
from views.playerview import PlayerView
from views.errorview import ErrorView
import utils.constants as constant


class PlayerController:
    @staticmethod
    def get_player_name():
        """Récupération du nom du joueur"""
        name = PlayerView.get_name_player()
        while not name.replace(" ", "").isalpha():
            ErrorView.get_alpha_message_error("Nom")
            name = PlayerView.get_name_player()
        return name

    @staticmethod
    def get_player_first_name():
        """Récupération du prénom du joueur"""
        first_name = PlayerView.get_first_name_player()
        while not first_name.replace(" ", "").isalpha():
            ErrorView.get_alpha_message_error("Prénom")
            first_name = PlayerView.get_first_name_player()
        return first_name

    @staticmethod
    def get_player_birth_date():
        """Récupération de la date de naissance"""
        loop_valid_date = False
        while not loop_valid_date:
            birth_date = PlayerView.get_birth_date_player()
            try:
                datetime.datetime.strptime(birth_date, "%d-%m-%Y")
                loop_valid_date = True
            except ValueError:
                ErrorView.get_date_message_error()
                loop_valid_date = False
        return birth_date

    @staticmethod
    def get_player_gender():
        """Récupération du sexe"""
        while True:
            try:
                gender = PlayerView.get_gender_player()
                if gender < 1 or gender > 2:
                    raise ValueError
            except ValueError:
                ErrorView.get_int_message_error("Sexe")
            else:
                break
        return constant.GENDER[gender - 1]

    @staticmethod
    def get_player_ranking_elo(name, first_name):
        """Récupération du classement elo"""
        while True:
            try:
                ranking_elo = PlayerView.get_ranking_elo_player(name, first_name)
                if ranking_elo <= 0:
                    raise ValueError
            except ValueError:
                ErrorView.get_int_message_error("Classement Elo")
            else:
                break
        return ranking_elo
