#! /usr/bin/env python3
# coding: utf-8

from controllers.tournamentcontroller import TournamentController

"""Models"""
from models.application import Menu
"""Views"""
from views.applicationview import MenuView
from views.applicationview import EndView
from views.errorview import ErrorView
"""Controllers"""
from controllers.databasecontroller import DataBase
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
            self._controller = self._controller()
                    

class MenuController:
    """
    Menu de l'utilisateur
    """
    
    def __init__(self):
        self._menu = Menu()
        self._view = MenuView(self._menu)
        self._errorview = ErrorView()
        self._user_choice = None
        self._answer = True
    
    def __call__(self):
        self._menu.add("auto", "Créer un tournoi.", TournamentController())
        self._menu.add("auto", "Recharger un tournoi.", DataBase.reload_database(self))

        self._menu.add("Q", "Quitter", EndController())
        
        self._view.user_choice()
        answer = self._view.get_user_choice()
        
        while self._answer:
            if answer.upper() in self._menu:
                self._user_choice = self._menu[answer.upper()]
                self._answer = False
            else:
                self._errorview.get_menu_message_error()
                answer = self._view.get_user_choice()

        
        return self._user_choice.handler
        
class EndController:
    """
    Pour quitter l'application
    """
    
    def __init__(self):
        self.view = EndView()
        
    def __call__(self):
        self.view.quit()
        print("EndController")