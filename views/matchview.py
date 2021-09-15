#! /usr/bin/env python3
# coding: utf-8


class MatchView:
    """Vues relatives aux matchs"""

    @staticmethod
    def get_result_match(white_player, black_player):
        """Résultat du match"""
        print("############")
        return int(
            input(
                f"Blanc: \n{white_player.name} {white_player.first_name} \n\n"
                f"contre \n\n"
                f"Noir : \n {black_player.name} {black_player.first_name} \n\n"
                f"Saisissez le résultat du match (1 - Victoire du joueur Blanc / "
                f"2 - Nul / "
                f"3 - Victoire du joueur Noir): "
            )
        )
