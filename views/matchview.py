#! /usr/bin/env python3
# coding: utf-8


class MatchView:
    """ Vues relatives aux matchs """
    
    @staticmethod
    def get_result_match(white_player, black_player):
        """ Résultat du match """
        print("############")
        return int(input(f"Blanc: \n{white_player.name} {white_player.first_name} \n\ncontre \n\nNoir : \n {black_player.name} {black_player.first_name} \n\nSaisissez le résultat du match (1 - Victoire du joueur Blanc / 2 - Nul / 3 - Victoire du joueur Noir): "))
    
    @staticmethod
    def display_match(white_player, black_player):
        """affiche le numéro du joueur pour l'ajout"""
        counter += 1
        print(f"Ajout du joueur {counter}")