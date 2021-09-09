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
    def display_list_tournament(doc_id, name):
        """affichage de la liste des tournois"""
        print(f"Tournoi {doc_id} : {name}")

    @staticmethod
    def display_all_items_list_tournament(doc_id, name, place, start_date, end_date, total_rounds):        
        """affichage de la liste des tournois avec les informations du tournoi"""
        print(f"Tournoi {doc_id} : {name},"
              f" Lieu : {place},"
              f" Date de début : {start_date},"
              f" Date de fin : {end_date},"
              f" Nombre de rondes : {total_rounds}")

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
    def get_tournament():
        """Question pour le choix du tournoi à recharger"""
        return int(input("Saisissez l'id du tournoi : "))

    @staticmethod
    def display_round_tournament(round):
        """Affichage des informations d'un round"""
        print(f" Nom du round : '{round['name_round']}',"
                  f" Date de début : '{round['start_timestamp']}',"
                  f" Date de fin : '{round['end_timestamp']}'")