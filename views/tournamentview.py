#! /usr/bin/env python3
# coding: utf-8

class TournamentView:
    """Vues relatives au tournoi"""
	
    @staticmethod
    def get_name_tournament():
        """saisie du nom du tournoi"""
        name = input("Entrer le nom du tournoi : ")
        return name
	
    @staticmethod
    def get_place_tournament():
        """saisie du lieu du tournoi"""
        place = input("Entrer le lieu du tournoi : ")
        return place

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