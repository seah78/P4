#! /usr/bin/env python3
# coding: utf-8

from datetime import datetime
from views.roundview import RoundView
from models.round import Round
from controllers.matchcontroller import MatchController


class RoundController:
    """Gestion des rounds"""

    def __init__(self):
        self.round = Round()
        # self.tournament = current_tournament
        # self.total_rounds = self.tournament.total_rounds
        # self.counter_rounds = self.tournament.counter_rounds
        self.list_match = []
        # self.manage_round()

    def first_round(self, tournament_list_players, counter_rounds):
        """premier round"""
        name = RoundController.get_name_round(counter_rounds)
        start_timestamp = datetime.now().strftime("%d-%m-%Y")
        # self.list_match = []
        RoundView.display_name_round(name)

        """Tri par classement elo"""
        list_player = sorted(
            tournament_list_players, key=lambda player: player.ranking_elo
        )

        """affectation des joueurs pour les matchs de la première ronde"""
        for i in range(4):
            self.list_match.append(
                MatchController.match_result(list_player[i], list_player[i + 4])
            )
        end_timestamp = datetime.now().strftime("%d-%m-%Y")

        """Classement des joueurs en fonction de leurs score"""
        list_ranking = sorted(list_player, key=lambda player: player.score)

        self.round = Round(name, start_timestamp, end_timestamp)
        self.round.add_player(list_player)
        self.round.add_ranking(list_ranking)
        self.round.add_match(self.list_match)
        return self.round

    def next_round(self, tournament_list_players, counter_rounds):
        self.list_match = []
        name = RoundController.get_name_round(counter_rounds)
        start_timestamp = datetime.now().strftime("%d-%m-%Y")
        RoundView.display_name_round(name)

        """Vérification des paires de joueurs"""
        players = RoundController.get_player(tournament_list_players)
        self.round.add_player(players)

        i = 0
        while len(players) > 0:
            player_white = players[i]
            player_black = players[i + 1]

            while player_black.ranking_elo in player_white.opponant:
                i += 1
                player_black = players[i + 1]

            self.list_match.append(
                MatchController.match_result(player_white, player_black)
            )
            del players[0]
            del players[i]

            i = 0

        end_timestamp = datetime.now().strftime("%d-%m-%Y")

        """Classement des joueurs en fonction de leurs score"""
        list_ranking = sorted(players, key=lambda player: player.score)

        self.round = Round(name, start_timestamp, end_timestamp)
        # self.round.add_player(list_players)
        self.round.add_ranking(list_ranking)
        self.round.add_match(self.list_match)
        return self.round

    @staticmethod
    def get_player(tournament_list_players):
        players = [player for player in tournament_list_players]

        players.sort(key=lambda x: x.ranking_elo, reverse=True)
        players.sort(key=lambda x: x.score, reverse=True)

        return players

    @staticmethod
    def get_name_round(counter_rounds):
        return "Round " + str(counter_rounds)

    def end_round():
        pass
