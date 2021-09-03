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
        print("Affichage du rapport")

    @staticmethod
    def display_players_alpha(alpha_player_list):
        print("\nPAR ORDRE ALPHABÉTIQUE :\n")

        for player in alpha_player_list:
            print(f" NOM : '{player['name']}',"
                  f" PRÉNOM : '{player['first_name']}',"
                  f" DATE DE NAISSANCE : '{player['birth_date']}',"
                  f" SEXE : '{player['gender']}',"
                  f" CLASSEMENT GÉNÉRAL : '{player['ranking_elo']}'.")
            
    @staticmethod
    def display_players_rank(rank_player_list):
        print("\nPAR CLASSEMENT ELO :\n")

        for player in rank_player_list:
            print(f" NOM : '{player['name']}',"
                  f" PRÉNOM : '{player['first_name']}',"
                  f" DATE DE NAISSANCE : '{player['birth_date']}',"
                  f" SEXE : '{player['gender']}',"
                  f" CLASSEMENT GÉNÉRAL : '{player['ranking_elo']}'.")

    
class ReturnView:
    
    @staticmethod
    def display_return():
        print("Retour au menu principal")
        
            
class EndView:
    
    @staticmethod
    def quit():
        print("Au revoir")