#! /usr/bin/env python3
# coding: utf-8


class TournamentView:
    """Vues relatives au tournoi"""

    @staticmethod
    def get_name_tournament():
        """saisie du nom du tournoi"""
        return input("Entrer le nom du tournoi : ")

    @staticmethod
    def get_place_tournament():
        """saisie du lieu du tournoi"""
        return input("Entrer le lieu du tournoi : ")

    @staticmethod
    def get_start_date_tournament():
        """saisie de la date de début du tournoi"""
        return input("Saisissez la date de début de tournoi (jj-mm-aaaa) : ")

    @staticmethod
    def get_end_date_tournament():
        """saisie de la date de fin du tournoi"""
        return input("Saisissez la date de fin de tournoi (jj-mm-aaaa) : ")

    @staticmethod
    def get_match_time_tournament():
        """saisie de la durée d'un match pour le tournoi"""
        return int(
            input(
                "Saisissez le numéro de la durée d'un match (1 - Bullet, 2 - Blitz, 3 - Coup rapide) : "
            )
        )

    @staticmethod
    def get_description_tournament():
        """saisie de la description du tournoi"""
        return str(input("Saisissez la description du tournoi : "))

    @staticmethod
    def display_name_tournament(name):
        """affichage du nom du tournoi"""
        print(f"Nom du tournoi : {name}")

    @staticmethod
    def display_list_reload_tournament(doc_id, name):
        """affichage de la liste des tournois non-terminés"""
        print(f"Tournoi {doc_id} : {name}")

    @staticmethod
    def display_place_tournament(place):
        """affichage du lieu du tournoi"""
        print(f"Lieu du tournoi : {place}")

    @staticmethod
    def get_continue_tournament():
        """Question pour continuer le tournoi"""
        return int(
            input("Souhaitez-vous continuer le tournoi ? (1 - Oui / 2 - Non) : ")
        )

    @staticmethod
    def get_reload_tournament():
        """Question pour le choix du tournoi à recharger"""
        return int(input("Saisissez l'id du tournoi à recharger : "))
