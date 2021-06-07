#! /usr/bin/env python3
# coding: utf-8

from models.tournament import Tournament
from models.player import Player
import views.tournamentview
import views.playerview 
import utils.errormanagement

"""
créer une liste de player
créer le tournoi avec la liste de player
lancer les rondes et le matchs
"""
DEFAULT_PLAYERS = 8

class TournamentController:

    def __init__(self):
        self.tournament = None

    def new_tournament(self):
        name = self.get_tournament_name()
        place = self.get_tournament_place()

        for player in range(DEFAULT_PLAYERS):
            name = self
            elo = ...
            player = Player(name, elo)
            self.tournament.add_player(player)

        tournament = Tournament()
        
    def get_tournament_name(self):
        name = TournamentView.get_name()
        while not name.isalpha():
            ErrorManagement.get_alpha_message_error("Nom")
            name = TournamentView.get_name()
        return name

    def get_tournament_place(self):
        place = TournamentView.get_place()
        while not place.isalpha():
            ErrorManagement.get_alpha_message_error("Lieu")
            place = TournamentView.get_name()
        return place

    def get_player_name(self):
        name = PlayerView.get_name_player()
        while not name.isalpha():
            ErrorManagement.get_alpha_message_error("Nom")
            name = TournamentView.get_name()
        return name




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