#! /usr/bin/env python3
# coding: utf-8


"""Models"""
from models.application import Menu
from models.tournament import Tournament
from models.database import Database
"""Views"""
from views.applicationview import MenuView
from views.applicationview import ReportView
from views.applicationview import ReturnView
from views.applicationview import EndView
from views.tournamentview import TournamentView
from views.errorview import ErrorView
"""Controllers"""
from controllers.tournamentcontroller import CreateTournamentController
from controllers.tournamentcontroller import ReloadTournamentController
"""Utils"""
from utils.clear import Clear



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
            choice = self._controller()
            if not choice():
                break
            self._controller = MenuController()
        
        
        """
        self._controller = MenuController()
        while self._controller:
            self._controller = self._controller()
        """          

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
        
        self._tournament = Tournament()
        self._database = Database()
    
    def __call__(self):
        
        Clear.screen()
        
        self._menu.add("auto", "Créer un tournoi.", CreateTournamentController(self._tournament))
        self._menu.add("auto", "Recharger un tournoi.", ReloadTournamentController(self._tournament))
        self._menu.add("auto", "Rapports", ReportMenuController())

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

        self._answer = True
        return self._user_choice.handler


class ReportMenuController:
    """
    Menu des rapports
    """
    
    def __init__(self):
        self._menu = Menu()
        self._view = MenuView(self._menu)
        self._errorview = ErrorView()
        self._user_choice = None
        self._answer = True
        self._database = Database()

    def __call__(self):
        Clear.screen()

        print("Menu des rapports") #Créer une vue
        
        self._menu.add("auto", "Liste des joueurs par ordre alphabétique", ReportController())
        self._menu.add("auto", "Liste des joueurs par classement ELO", ReportController())
        self._menu.add("auto", "Liste des joueurs d'un tournoi par par ordre alphabétique", ReportController())
        self._menu.add("auto", "Liste des joueurs d'un tournoi par classement ELO", ReportController())
        self._menu.add("auto", "Liste des tournois", ReportController())
        self._menu.add("auto", "Liste des rondes d'un tournoi", ReportController())
        self._menu.add("auto", "Liste des matchs d'un tournoi", ReportController())

        self._menu.add("R", "Retour", ReturnController())
        
        self._view.user_choice()
        answer = self._view.get_user_choice()
        
        while self._answer:
            if answer.upper() in self._menu:
                self._user_choice = self._menu[answer.upper()]
                self._answer = False
            else:
                self._errorview.get_menu_message_error()
                answer = self._view.get_user_choice()

        self._answer = True
        return self._user_choice.handler

class ReportController:
    """
    Affichage du rapport
    """
    
    def __init__(self):
        self.view = ReportView()
        
    def __call__(self):
        self.view.display_report()
        return True


class ReturnController:
    """
    Pour retourner au menu principal
    """
    
    def __init__(self):
        self.view = ReturnView()
        
    def __call__(self):
        self.view.display_return()
        return True

        
class EndController:
    """
    Pour quitter l'application
    """
    
    def __init__(self):
        self.view = EndView()
        
    def __call__(self):
        self.view.quit()
        return False