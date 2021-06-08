#! /usr/bin/env python3
# coding: utf-8

from models.tournament import Tournament
from models.player import Player

from views.tournamentview import TournamentView
from views.playerview import PlayerView 
from utils.errormanagement import ErrorManagement


"""
créer une liste de player
créer le tournoi avec la liste de player
lancer les rondes et le matchs
"""
DEFAULT_PLAYERS = 8

class TournamentController:
    """Gestion du tournoi"""

    def __init__(self):
        self.tournament = None

    def new_tournament(self):
        name = self.get_tournament_name()
        place = self.get_tournament_place()
        start_date = ""
        end_date = ""
        time = ""
        description = ""
        self.tournament = Tournament(name, place)

        for counter in range(DEFAULT_PLAYERS):
            PlayerView.display_counter_player(counter)
            name = self.get_player_name()
            first_name = self.get_player_first_name()
            birth_date = self.get_player_birth_date()
            gender = self.get_player_gender()
            ranking_elo = self.get_player_ranking_elo()
            player = Player(name, first_name, birth_date, gender, ranking_elo)
            self.tournament.add_player(player)
        
        
    def get_tournament_name(self):
        name = TournamentView.get_name_tournament()
        while not name.isalpha():
            ErrorManagement.get_alpha_message_error("Nom")
            name = TournamentView.get_name_tournament()
        return name

    def get_tournament_place(self):
        place = TournamentView.get_place_tournament()
        while not place.isalpha():
            ErrorManagement.get_alpha_message_error("Lieu")
            place = TournamentView.get_place_tournament()
        return place

    def get_player_name(self):
        name = PlayerView.get_name_player()
        while not name.isalpha():
            ErrorManagement.get_alpha_message_error("Nom")
            name = PlayerView.get_name_player()
        return name

    def get_player_first_name(self):
        first_name = PlayerView.get_first_name_player()
        while not first_name.isalpha():
            ErrorManagement.get_alpha_message_error("Prénom")
            first_name = PlayerView.get_first_name_player()
        return first_name

    def get_player_birth_date(self):
        pass
        """
        birth_date = PlayerView.get_birth_date_player()
        while not birth_date.isalpha():
            ErrorManagement.get_date_message_error()
            name = TournamentView.get_name()
        return name
        """

    def get_player_gender(self):
        pass
        """
        gender = PlayerView.get_gender_player()
        while not gender.isalpha():
            ErrorManagement.get_alpha_message_error("Nom")
            gender = TournamentView.get_name()
        return gender
        """

    def get_player_ranking_elo(self):
        pass
        """
        ranking_elo = PlayerView.get_ranking_elo_player()
        while not name.isalpha():
            ErrorManagement.get_alpha_message_error("Nom")
            ranking_elo = TournamentView.get_name()
        return ranking_elo
        """

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