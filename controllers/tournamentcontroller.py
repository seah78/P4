#! /usr/bin/env python3
# coding: utf-8

from datetime import datetime
from tinydb import TinyDB, Query, where

"""Models"""
from models.player import Player
from models.database import Database
"""Views"""
from views.tournamentview import TournamentView
from views.playerview import PlayerView 
from views.errorview import ErrorView
"""Controllers"""
from controllers.roundcontroller import RoundController
from controllers.playercontroller import PlayerController
"""Utils"""
import utils.constants as constant
from utils.clear import Clear


"""
créer une liste de player
créer le tournoi avec la liste de player
lancer les rondes et le matchs
"""


list_player = [Player("Joueur" , "Un", (datetime.now().strftime("%d-%m-%Y")), "M", 1600), 
               Player("Joueur" , "Deux", (datetime.now().strftime("%d-%m-%Y")), "M", 1705), 
               Player("Joueur" , "Trois", (datetime.now().strftime("%d-%m-%Y")), "M", 1499),
               Player("Joueur" , "Quatre", (datetime.now().strftime("%d-%m-%Y")), "M", 999),
               Player("Joueur" , "Cinq", (datetime.now().strftime("%d-%m-%Y")), "M", 1495),
               Player("Joueur" , "Six", (datetime.now().strftime("%d-%m-%Y")), "M", 1186),
               Player("Joueur" , "Sept", (datetime.now().strftime("%d-%m-%Y")), "M", 1008),
               Player("Joueur" , "Huit", (datetime.now().strftime("%d-%m-%Y")), "M", 1498)]

    
class CreateTournamentController:
    """ 
    Récupère les informations pour la création d'un tournoi 
    """
    
    def __init__(self, tournament):
        self._tournament = tournament
        self._tournament_controller = TournamentController()
        self._player_controller = PlayerController()
        self._round_controller = RoundController()
        self._view = TournamentView()
        self._database = Database()
        
    def __call__(self):

        self._tournament.name = self._tournament_controller.get_tournament_name()
        self._tournament.place = "Test" #self._tournament_controller.get_tournament_place()
        self._tournament.start_date = (datetime.now().strftime("%d-%m-%Y")) #self._tournament_controller.get_tournament_start_date()
        self._tournament.end_date = "" # (datetime.now().strftime("%d-%m-%Y")) #self._tournament_controller.get_tournament_end_date()
        self._tournament.total_rounds = constant.DEFAULT_ROUNDS
        self._tournament.counter_rounds = constant.COUNTER_ROUNDS
        self._tournament.match_time = "Blitz" #self._tournament_controller.get_tournament_time()
        self._tournament.description = "test" #self._tournament_controller.get_tournament_description()
        #self.tournament = Tournament(name, place, start_date, end_date, time, total_rounds, counter_rounds, description)

        """
        for counter in range(constant.DEFAULT_PLAYERS):
            PlayerView.display_counter_player(counter)
            name = self._player_controller.get_player_name()
            first_name = self._player_controller.get_player_first_name()
            birth_date = self._player_controller.get_player_birth_date()
            gender = self._player_controller.get_player_gender()
            ranking_elo = PlayerController.get_player_ranking_elo()
            player = Player(name, first_name, birth_date, gender, ranking_elo)
            self._tournament.add_player(player)
        """
        """Gérer l'enregistrement du joueur"""
        """Controleur pour vérifier si un joueur existe déjà"""

        self._tournament.list_players = list_player


        while self._tournament.counter_rounds != self._tournament.total_rounds + 1:
            Clear.screen()

            print(f"counter rounds {self._tournament.counter_rounds}, total rounds {self._tournament.total_rounds}")
            if self._tournament.counter_rounds == 1:
                self._tournament.add_round(self._round_controller.first_round(self._tournament.list_players, self._tournament.counter_rounds))
            else:
                self._tournament.add_round(self._round_controller.next_round(self._tournament.list_players , self._tournament.counter_rounds))
                if self._tournament.counter_rounds == self._tournament.total_rounds:
                    self._tournament.end_date = (datetime.now().strftime("%d-%m-%Y")) #self.get_tournament_end_date()
            if self._tournament.counter_rounds != self._tournament.total_rounds:
                self._tournament.counter_rounds += 1
                answer_continue = TournamentController.get_tournament_continue()
                if answer_continue != 2:
                    continue
            break
        self._database.save_tournament(self._tournament.serializer())
        return True

class ReloadTournamentController:
    """
    Recharge les informations d'un tournoi non terminé
    """
    def __init__(self, tournament):
        self._tournament = tournament
        self._tournament_controller = TournamentController()
        self._round_controller = RoundController()
        self._view = TournamentView()
        self._database = Database()
        
    def __call__(self):

        """gérer si aucun tournoi à recharger"""

        list_doc_id = []
        for tournament in self._database.tournaments:
            if tournament["end_date"] is "":
                self._view.display_list_reload_tournament(tournament.doc_id, tournament["name"])
            list_doc_id.append(tournament.doc_id)
                
        id_reload_tournament = TournamentController.get_tournament_reload(list_doc_id)
        
        
        self._tournament = self._tournament.deserializer(id_reload_tournament)
        while self._tournament.counter_rounds != self._tournament.total_rounds + 1:
            Clear.screen()

            print(f"counter rounds {self._tournament.counter_rounds}, total rounds {self._tournament.total_rounds}")
            if self._tournament.counter_rounds == 1:
                self._tournament.add_round(self._round_controller.first_round(self._tournament.list_players, self._tournament.counter_rounds))
            else:
                self._tournament.add_round(self._round_controller.next_round(self._tournament.list_players , self._tournament.counter_rounds))
                if self._tournament.counter_rounds == self._tournament.total_rounds:
                    self._tournament.end_date = (datetime.now().strftime("%d-%m-%Y")) #self.get_tournament_end_date()
            if self._tournament.counter_rounds != self._tournament.total_rounds:
                self._tournament.counter_rounds += 1
                answer_continue = TournamentController.get_tournament_continue()
                if answer_continue != 2:
                    continue
            break
        self._database.update_tournament(self._tournament.serializer(), id_reload_tournament)
        return True





class TournamentController:
    """Gestion du tournoi"""

    def __init__(self):
        self.tournament = None

    def get_tournament_name(self):
        """recupération du nom du tournoi"""
        name = TournamentView.get_name_tournament()
        while not name.replace(" ", "").isalnum():
            ErrorView.get_alpha_message_error("Nom")
            name = TournamentView.get_name_tournament()
        return name

    def get_tournament_place(self):
        """ récupération du lieu du tournoi"""
        place = TournamentView.get_place_tournament()
        while not place.replace(" ", "").isalpha():
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
    
    @staticmethod
    def get_tournament_continue():
        """Contrôle de la réponse pour continuer ou non le tournoi"""
        while True:
            try:
                answer = TournamentView.get_continue_tournament()
                if answer < 1 or answer > 2:
                    raise ValueError
            except ValueError:
                ErrorView.get_int_message_error("Continuer")
            else:
                break
        return answer
    
    @staticmethod
    def get_tournament_reload(tournaments):
        """Contrôle de la saisie pour la recharge du tournoi"""
        while True:
            try:
                reload_tournament = TournamentView.get_reload_tournament()
                if reload_tournament not in tournaments:
                    raise ValueError
            except ValueError:
                ErrorView.get_int_list_reload_message_error()
            else:
                break
        return reload_tournament






    def display_tournament(self):
        pass


# Recherche sur la fonction zip









