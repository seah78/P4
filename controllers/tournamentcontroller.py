#! /usr/bin/env python3
# coding: utf-8

from models.tournament import Tournament
from models.player import Player 

class TournamentController:

créer une liste de player
créer le tournoi avec la liste de player
lancer les rondes et le matchs












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