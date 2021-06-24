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
        return input("Saisissez la date de début de tournoi (jj-mm-aaaa): ")

    @staticmethod
    def get_end_date_tournament():
        """saisie de la date de fin du tournoi"""
        return input("Saisissez la date de fin de tournoi (jj-mm-aaaa): ")

    @staticmethod
    def get_match_time_tournament():
        """saisie de la durée d'un match pour le tournoi"""
        return int(
            input(
                "Saisissez le numéro de la durée d'un match (1 - Bullet, 2 - Blitz, 3 - Coup rapide) :"
            )
        )

    @staticmethod
    def get_description_tournament():
        """saisie de la description du tournoi"""
        return str(input("Saisissez la description du tournoi :"))
      

    @staticmethod
    def display_name_tournament(name):
        """affichage du nom du tournoi"""
        print(f"Nom du tournoi : {name}")
	
    @staticmethod
    def display_place_tournament(place):
        """affichage du lieu du tournoi"""
        print(f"Lieu du tournoi : {place}")





        
"""
class MenuEntry:
    def __init__(self, option, handler):
        self.option = option
        self.handler = handler

    def __repr__(self):
        return f"MenuEntry({self.option}, {self.handler})"

    def __str__(self):
        return str(self.option)


class Menu:
    def __init__(self):
        self._entries = {}
        self._autokey = 1

    def add(self, key, option, handler):
        if key == "auto":
            key = str(self._autokey)
            self._autokey += 1

        self._entries[str(key)] = MenuEntry(option, handler)

    def items(self):
        return self._entries.items()

    def __contains__(self, choice):
        return str(choice) in self._entries

    def __getitem__(self, choice):
        return self._entries[choice]


if __name__ == "__main__":
    menu = Menu()
    menu.add("auto", "première option du menu", lambda: None)
    menu.add("auto", "seconde option du menu", lambda: None)
    menu.add("q", "dernière option du menu", lambda: None)
    print(menu._entries)

"""