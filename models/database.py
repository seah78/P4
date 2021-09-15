#! /usr/bin/env python3
# coding: utf-8


from tinydb import TinyDB, Query


class Database:
    """
    Modèle de la base de donnée
    """

    def __init__(self):
        self.db = TinyDB("utils/database.json", indent=4)
        self.tournaments = self.db.table("tournaments")
        self.players = self.db.table("players")

    def save_tournament(self, serializer):
        """Sauvegarde du tournoi"""
        self.tournaments.insert(serializer)

    def update_tournament(self, serializer, id_tournament):
        """Mise à jour du tournoi"""
        search_tournament = self.tournaments.get(doc_id=id_tournament)
        name_tournament = search_tournament["name"]
        Tournament = Query()
        self.tournaments.update(serializer, Tournament.name == name_tournament)

    def save_player(self, serializer):
        """Sauvegarde du joueur"""
        self.players.insert(serializer)

    def update_player_rank(self, ranking_elo, name, first_name):
        """Mise à jour du classement ELO"""
        Player = Query()
        self.players.update(
            {"ranking_elo": ranking_elo},
            Player.name == name and Player.first_name == first_name,
        )
