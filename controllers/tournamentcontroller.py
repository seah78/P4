#! /usr/bin/env python3
# coding: utf-8

from controllers.roundcontroller import RoundController
import datetime

from controllers.playercontroller import PlayerController

import utils.constants as constant

from models.tournament import Tournament
from models.player import Player

from views.tournamentview import TournamentView
from views.playerview import PlayerView 
from views.errorview import ErrorView


"""
créer une liste de player
créer le tournoi avec la liste de player
lancer les rondes et le matchs
"""

class TournamentController:
    """Gestion du tournoi"""

    def __init__(self):
        self.tournament = None

    def new_tournament(self):
        """creation d'un tournoi"""
        name = self.get_tournament_name()
        place = self.get_tournament_place()
        start_date = self.get_tournament_start_date()
        end_date = self.get_tournament_end_date()
        time = self.get_tournament_time()
        description = self.get_tournament_description()
        self.tournament = Tournament(name, place, start_date, end_date, time, description)

        for counter in range(constant.DEFAULT_PLAYERS):
            PlayerView.display_counter_player(counter)
            name = PlayerController.get_player_name()
            first_name = PlayerController.get_player_first_name()
            birth_date = PlayerController.get_player_birth_date()
            gender = PlayerController.get_player_gender()
            ranking_elo = PlayerController.get_player_ranking_elo()
            player = Player(name, first_name, birth_date, gender, ranking_elo)
            self.tournament.add_player(player)


        #for counter in range(constant.DEFAULT_ROUNDS):
        
        #return RoundController(self.tournament)

    def get_tournament_name(self):
        """recupération du nom du tournoi"""
        name = TournamentView.get_name_tournament()
        while not name.isalpha():
            ErrorView.get_alpha_message_error("Nom")
            name = TournamentView.get_name_tournament()
        return name

    def get_tournament_place(self):
        """ récupération du lieu du tournoi"""
        place = TournamentView.get_place_tournament()
        while not place.isalpha():
            ErrorView.get_alpha_message_error("Lieu")
            place = TournamentView.get_place_tournament()
        return place

    def get_tournament_start_date(self):
        """récupération de la date de début"""
        loop_valid_date = False
        while not loop_valid_date:
            start_date = TournamentView.get_start_date_tournament()
            try:
                start_date = datetime.datetime.strptime(start_date, '%d-%m-%Y')
                loop_valid_date = True
            except ValueError:
                ErrorView.get_date_message_error()
                loop_valid_date = False
        return start_date

    def get_tournament_end_date(self):
        """récupération de la date de fin"""
        loop_valid_date = False
        while not loop_valid_date:
            start_date = TournamentView.get_end_date_tournament()
            try:
                start_date = datetime.datetime.strptime(start_date, '%d-%m-%Y')
                loop_valid_date = True
            except ValueError:
                ErrorView.get_date_message_error()
                loop_valid_date = False
        return start_date

    def get_tournament_time(self):
        """récupération de la durée d'un match du tournoi"""
        while True:
            try:
                match_time = TournamentView.get_match_time_tournament()
                if match_time < 1 or match_time > 3:
                    raise ValueError
            except ValueError:
                ErrorView.get_int_message_error("Durée d'un match")
            else:
                break
        return constant.MATCH_TIME[match_time - 1]

    def get_tournament_description(self):
        """récupération de la description"""
        return TournamentView.get_description_tournament()







    def display_tournament(self):
        pass


# Recherche sur la fonction zip









"""
    def __init__(self):
        self.controller = None

    def start(self):
        self.controller = TournamentMenuController()
        while self.controller:
            self.controller = self.controller()    


class TournamentMenuController:
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self):
        # 1. Construire un menu
        self.menu.add("auto", "Creer un tournoi", CreationTournamentMenuController())
        self.menu.add("auto", "Liste des tournois", ListTournamentController())
        self.menu.add("q", "quitter", EndScreenController())

        # 2. Demander à la vue d'afficher le menu et de collecter la réponse de l'utilisateur
        user_choice = self.view.get_user_choice()

        # 3. Retourner le controller associé au choix de l'utilisateur au contrôleur principal
        return user_choice.handler


class CreationTournamentMenuController:
    def __call__(self):
        print("dans le menu de creation")
        return TournamentMenuController()


class ListTournamentMenuController:
    def __call__(self):
        print("dans la liste des tournois")
        return TournamentMenuController()


class RankingTournamentController:
    pass


class TimerTournamentController:
    pass

class EndScreenController:
    def __call__(self):
        print("A une prochaine !")




"""