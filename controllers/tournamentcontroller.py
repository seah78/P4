#! /usr/bin/env python3
# coding: utf-8

# import datetime
from pathlib import Path
from datetime import datetime
from tinydb import Query

from models.player import Player
from models.database import Database
from views.tournamentview import TournamentView
from views.playerview import PlayerView
from views.errorview import ErrorView
from controllers.roundcontroller import RoundController
from controllers.playercontroller import PlayerController
import utils.constants as constant
from utils.clear import Clear


class CreateTournamentController:
    """
    Récupère les informations pour la création d'un tournoi
    """

    def __init__(self, tournament):
        self._tournament = tournament
        self._tournament_controller = TournamentController()
        self._player = Player()
        self._player_controller = PlayerController()
        self._round_controller = RoundController()
        self._view = TournamentView()
        self._database = Database()

    def __call__(self):
        Clear.screen()

        self._tournament.name = self._tournament_controller.get_tournament_name()
        self._tournament.place = self._tournament_controller.get_tournament_place()
        self._tournament.start_date = datetime.now().strftime("%d-%m-%Y")
        self._tournament.end_date = ""
        self._tournament.total_rounds = constant.DEFAULT_ROUNDS
        self._tournament.counter_rounds = constant.COUNTER_ROUNDS
        self._tournament.match_time = self._tournament_controller.get_tournament_time()
        self._tournament.description = (
            self._tournament_controller.get_tournament_description()
        )
        
        self.add_player_tournament()

        while self._tournament.counter_rounds != self._tournament.total_rounds + 1:
            Clear.screen()


            if self._tournament.counter_rounds == 1:
                self._tournament.add_round(
                    self._round_controller.first_round(
                        self._tournament.list_players, self._tournament.counter_rounds
                    )
                )
            else:
                self._tournament.add_round(
                    self._round_controller.next_round(
                        self._tournament.list_players, self._tournament.counter_rounds
                    )
                )
                if self._tournament.counter_rounds == self._tournament.total_rounds:
                    self._tournament.end_date = datetime.now().strftime(
                        "%d-%m-%Y"
                    )  # self.get_tournament_end_date()
            if self._tournament.counter_rounds != self._tournament.total_rounds:
                self._tournament.counter_rounds += 1
                answer_continue = TournamentController.get_tournament_continue()
                if answer_continue != 2:
                    continue
            break
        self._database.save_tournament(self._tournament.serializer())
        if not self._tournament.end_date == "":
            Clear.screen()
            PlayerView.update_rank_player()
            self.update_ranking_elo()
        return True

    def add_player_tournament(self):
        Clear.screen()
        for counter in range(constant.DEFAULT_PLAYERS):
            PlayerView.display_counter_player(counter)
            name = self._player_controller.get_player_name()
            first_name = self._player_controller.get_player_first_name()
            birth_date = self._player_controller.get_player_birth_date()
            gender = self._player_controller.get_player_gender()
            ranking_elo = self._player_controller.get_player_ranking_elo(name, first_name)
            player = Player(name, first_name, birth_date, gender, ranking_elo)
            self._tournament.add_player(player)
            
            path = Path("./utils/database.json")
            if path.stat().st_size != 0:
                search_player = Query()
                if self._database.players.search(
                    search_player.name == player.name
                    and search_player.first_name == player.first_name
                ):
                    continue
                else:
                    self._database.save_player(player.serializer_player())
            else:
                self._database.save_player(player.serializer_player())

    def update_ranking_elo(self):
        for player in self._tournament.list_players:
            ranking_elo = PlayerController.get_player_ranking_elo(player.name, player.first_name)
            self._database.update_player_rank(
                ranking_elo, player.name, player.first_name
            )


class ReloadTournamentController:
    """
    Recharge les informations d'un tournoi non terminé
    """

    def __init__(self, tournament):
        self._tournament = tournament
        self._tournament_controller = TournamentController()
        self._player_controller = PlayerController()
        self._round_controller = RoundController()
        self._view = TournamentView()
        self._database = Database()

    def __call__(self):

        list_doc_id = []
        for tournament in self._database.tournaments:
            if tournament["end_date"] == "":
                self._view.display_list_tournament(
                    tournament.doc_id, tournament["name"]
                )
            list_doc_id.append(tournament.doc_id)

        id_reload_tournament = TournamentController.get_tournament(list_doc_id)

        self._tournament = self._tournament.deserializer(id_reload_tournament)
        while self._tournament.counter_rounds != self._tournament.total_rounds + 1:
            Clear.screen()


            if self._tournament.counter_rounds == 1:
                self._tournament.add_round(
                    self._round_controller.first_round(
                        self._tournament.list_players, self._tournament.counter_rounds
                    )
                )
            else:
                self._tournament.add_round(
                    self._round_controller.next_round(
                        self._tournament.list_players, self._tournament.counter_rounds
                    )
                )
                if self._tournament.counter_rounds == self._tournament.total_rounds:
                    self._tournament.end_date = datetime.now().strftime(
                        "%d-%m-%Y"
                    )  # self.get_tournament_end_date()
            if self._tournament.counter_rounds != self._tournament.total_rounds:
                self._tournament.counter_rounds += 1
                answer_continue = TournamentController.get_tournament_continue()
                if answer_continue != 2:
                    continue
            break
        self._database.update_tournament(
            self._tournament.serializer(), id_reload_tournament
        )
        if not self._tournament.end_date == "":
            Clear.screen()
            PlayerView.update_rank_player()
            self.update_ranking_elo()
        return True

    def update_ranking_elo(self):
        for player in self._tournament.list_players:
            ranking_elo = PlayerController.get_player_ranking_elo(player.name, player.first_name)
            self._database.update_player_rank(
                ranking_elo, player.name, player.first_name
            )


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
        """récupération du lieu du tournoi"""
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
                start_date = datetime.datetime.strptime(start_date, "%d-%m-%Y")
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
                start_date = datetime.datetime.strptime(start_date, "%d-%m-%Y")
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
    def get_tournament(tournaments):
        """Contrôle de la saisie du tournoi"""
        while True:
            try:
                reload_tournament = TournamentView.get_tournament()
                if reload_tournament not in tournaments:
                    raise ValueError
            except ValueError:
                ErrorView.get_int_list_tournament_message_error()
            else:
                break
        return reload_tournament

    def display_tournament(self):
        pass


