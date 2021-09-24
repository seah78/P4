#! /usr/bin/env python3
# coding: utf-8


class PlayerView:
    """Vues relatives au joueur"""

    @staticmethod
    def get_name_player():
        """nom du joueur"""
        return input("Saisissez le nom du joueur : ")

    @staticmethod
    def get_first_name_player():
        """prénom du joueur"""
        return input("Saisissez le prénom du joueur : ")

    @staticmethod
    def get_birth_date_player():
        """date de naissance du joueur"""
        return input("Saisissez la date de naissance du joueur (jj-mm-aaaa): ")

    @staticmethod
    def get_gender_player():
        """sexe du joueur"""
        return int(input("Saisissez le sexe du joueur (1 - Masculin / 2 - Féminin): "))

    @staticmethod
    def get_ranking_elo_player(name, first_name):
        """classement elo du joueur"""
        return int(input(f"Saisissez le classement elo du joueur {first_name} {name}: "))

    @staticmethod
    def display_counter_player(counter):
        """affiche le numéro du joueur pour l'ajout"""
        counter += 1
        print(f"\nAjout du joueur {counter}")
        
    @staticmethod
    def update_rank_player():
        """ affiche une information """
        print("\nMise à jour des classements des joueurs")
