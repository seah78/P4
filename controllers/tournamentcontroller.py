#! /usr/bin/env python3
# coding: utf-8

from datetime import datetime

"""Models"""
from models.tournament import Tournament
from models.player import Player
"""Views"""
from views.tournamentview import TournamentView
from views.playerview import PlayerView 
from views.errorview import ErrorView
"""Controllers"""
from controllers.roundcontroller import RoundController
from controllers.playercontroller import PlayerController
from controllers.databasecontroller import DataBaseController
"""Utils"""
import utils.constants as constant


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

class TournamentController:
    """Gestion du tournoi"""

    def __init__(self):
        self.tournament = None
        
    def __call__(self):
        self.new_tournament()
        return True

    def new_tournament(self):
        """creation d'un tournoi"""
        name = "Test Serializer" #self.get_tournament_name()
        place = "Test" #self.get_tournament_place()
        start_date = (datetime.now().strftime("%d-%m-%Y")) #self.get_tournament_start_date()
        end_date = (datetime.now().strftime("%d-%m-%Y")) #self.get_tournament_end_date()
        total_rounds = constant.DEFAULT_ROUNDS
        counter_rounds = constant.COUNTER_ROUNDS
        time = "Blitz" #self.get_tournament_time()
        description = "test" #self.get_tournament_description()
        self.tournament = Tournament(name, place, start_date, end_date, time, total_rounds, counter_rounds, description)

        """
        for counter in range(constant.DEFAULT_PLAYERS):
            PlayerView.display_counter_player(counter)
            name = PlayerController.get_player_name()
            first_name = PlayerController.get_player_first_name()
            birth_date = PlayerController.get_player_birth_date()
            gender = PlayerController.get_player_gender()
            ranking_elo = PlayerController.get_player_ranking_elo()
            player = Player(name, first_name, birth_date, gender, ranking_elo)
            self.tournament.add_player(player)
        """
        self.tournament.list_players = list_player


        while self.tournament.counter_rounds != total_rounds + 1:
            if self.tournament.counter_rounds == 1:
                self.tournament.add_round(RoundController.first_round(self, self.tournament.list_players, self.tournament.counter_rounds))
            else:
                self.tournament.add_round(RoundController.next_round(self, self.tournament.list_players , self.tournament.counter_rounds))
            self.tournament.counter_rounds += 1
            answer_continue = self.get_tournament_continue()
            if answer_continue == 2 :
                DataBaseController.save_tournament(self.tournament.serializer())
                break
            else:
                continue
                



    def reload_tournament(self):
        self.tournament = None
        self.tournament = Tournament.deserializer()
        

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
    
    def get_tournament_continue(self):
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






    def display_tournament(self):
        pass


# Recherche sur la fonction zip









"""




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