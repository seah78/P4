#! /usr/bin/env python3
# coding: utf-8


class PlayerView:
    """Vues relatives au joueur"""

    @staticmethod
    def get_name_player():
        """nom du joueur"""
        name = input("Saisissez le nom du joueur : ")
        return name
    
    @staticmethod
    def get_first_name_player():
        """prénom du joueur"""
        first_name = input("Saisissez le prénom du joueur : ")
        return first_name    
    
    @staticmethod
    def get_birth_date_player():
        """date de naissance du joueur"""
        birth_date = input("Saisissez la date de naissance du joueur (jj/mm/aaaa): ")
        return birth_date    
    
    @staticmethod
    def get_gender_player():
        """sexe du joueur"""
        gender = input("Saisissez le sexe du joueur (M/F): ")
        return gender    
    
    @staticmethod
    def get_ranking_elo_player():
        """classement elo du joueur"""
        ranking_elo = input("Saisissez le classement elo du joueur : ")
        return ranking_elo    

    @staticmethod
    def display_counter_player(counter):
        """affiche le numéro du joueur pour l'ajout"""
        counter += 1
        print(f"Ajout du joueur {counter}")
    