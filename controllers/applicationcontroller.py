#! /usr/bin/env python3
# coding: utf-8

from controllers.tournamentcontroller import TournamentController

"""Models"""
from models.application import Menu
"""Views"""
from views.applicationview import MenuView
from views.applicationview import EndView

"""Controllers"""

"""Utils"""




class ApplicationController:
    """
    Gestion de l'application et des menus
    """

    def __init__(self):
        self._controller = None
        
    def start(self):
        """
        Boucle qui permet de passer d'un contrôlleur à un autre
        Le menu est le premier controlleur appelé
        S'arrête lorsque le controleur de fin est appelé
        """
        
        
        self._controller = MenuController()
        while self._controller:
            self._controller = self._controller
                    

class MenuController:
    """
    Menu de l'utilisateur
    """
    
    def __init__(self):
        self._menu = Menu()
        self._view = MenuView(self._menu)
        self._user_choice = None
    
    def __call__(self):
        self._menu.add("auto", "Créer un tournoi.", TournamentController())
        self._menu.add("Q", "Quitter", EndController())
        
        self._view.user_choice()
        
        
class EndController:
    """
    Pour quitter l'application
    """
    
    def __init__(self):
        self.view = EndView()
        
    def __call__(self):
        self.view.quit()