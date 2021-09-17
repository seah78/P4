#! /usr/bin/env python3
# coding: utf-8

"""Vues de l'application et des menus"""


class MenuView:

    """
    Vues des menus
    """

    def __init__(self, menu):
        self.menu = menu

    def _display_menu(self):
        print("Choisissez votre option : \n")

        for key, entry in self.menu.items():
            print(f"{key}: {entry}\n")

    def user_choice(self):
        self._display_menu()

    @staticmethod
    def get_user_choice():
        return input(">> ")

    @staticmethod
    def display_principal_menu():
        print("Menu principal")

    @staticmethod
    def display_report_menu():
        print("Menu des rapports")


class ReportView:
    @staticmethod
    def display_report():
        print("\nAffichage du rapport")

    @staticmethod
    def display_player(player):
        print(
            f" NOM : '{player['name']}',"
            f" PRÉNOM : '{player['first_name']}',"
            f" DATE DE NAISSANCE : '{player['birth_date']}',"
            f" SEXE : '{player['gender']}',"
            f" CLASSEMENT GÉNÉRAL : '{player['ranking_elo']}'."
        )
        
    @staticmethod
    def display_player_round(player):
        print(
            f" NOM : '{player['name']}',"
            f" PRÉNOM : '{player['first_name']}',"
            f" SCORE : '{player['score']}'."
        )

    @staticmethod
    def display_match(indice, white_player, black_player, white_score, black_score):
        print(
            f"Match {indice}\n"
            f"Blanc : '{white_player['name']}' , '{white_player['first_name']}' {white_score}\n"
            f"Noir : '{black_player['name']}' , '{black_player['first_name']}' {black_score}\n"
        )


class ReturnView:
    @staticmethod
    def display_return():
        print("\nRetour au menu principal")
    
    @staticmethod    
    def return_menu():
        return input("\nAppuyez sur [Enter] pour retourner au menu principal")


class EndView:
    @staticmethod
    def quit():
        print("\nAu revoir")
