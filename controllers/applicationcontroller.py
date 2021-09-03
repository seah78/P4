#! /usr/bin/env python3
# coding: utf-8

from views.tournamentview import TournamentView
from tinydb import TinyDB, Query, where


"""Models"""
from models.application import Menu
from models.tournament import Tournament
from models.database import Database
"""Views"""
from views.applicationview import MenuView
from views.applicationview import ReportView
from views.applicationview import ReturnView
from views.applicationview import EndView
from views.errorview import ErrorView
"""Controllers"""
from controllers.tournamentcontroller import ReloadTournamentController
from controllers.tournamentcontroller import CreateTournamentController
from controllers.tournamentcontroller import TournamentController
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
        
    def __call__(self):
                
        # Effacer l'écran.
        #Clear().screen()

        self._menu.add("auto", "Gestion des tournois.", TournamentMenuController())
        self._menu.add("auto", "Rapports", ReportMenuController())

        self._menu.add("Q", "Quitter", EndController())

        # DISPLAY MENU AND GET USER CHOICE.
        #self._view.welcome_home()

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

class TournamentMenuController:

    def __init__(self):
        self._menu = Menu()
        self._view = MenuView(self._menu)
        self._errorview = ErrorView()
        self._user_choice = None
        self._answer = True
        self._tournament = Tournament()
        self._database = Database()

    def __call__(self):
        # Effacer l'écran.
        #Clear().screen()

        # ADD MENUS.
        # IF A TOURNAMENT IN DATA BASE IS NOT FINISHED.


        if self._database.tournaments.contains(where('end_date') ==  ""):
            self._menu.add("auto", "Créer un tournoi.", CreateTournamentController(self._tournament))
            self._menu.add("auto", "Recharger un tournoi.", ReloadTournamentController(self._tournament))

        else:
            self._menu.add("auto", "Créer un tournoi.", CreateTournamentController(self._tournament))
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
        #Clear.screen()

        self._view.display_report_menu()
        
        self._menu.add("auto", "Liste des joueurs par ordre alphabétique", ReportAlphaPlayersController())
        self._menu.add("auto", "Liste des joueurs par classement ELO", ReportRankPlayersController())
        self._menu.add("auto", "Liste des joueurs d'un tournoi par par ordre alphabétique", ReportTournamentAlphaPlayersController())
        self._menu.add("auto", "Liste des joueurs d'un tournoi par classement ELO", ReportTournamentRankPlayersController())
        self._menu.add("auto", "Liste des tournois", ReportTournamentController())
        self._menu.add("auto", "Liste des rondes d'un tournoi", ReportRoundsTournamentController())
        self._menu.add("auto", "Liste des matchs d'un tournoi", ReportMatchTournamentController())

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


class ReportAlphaPlayersController:
    """
    Affichage du rapport
    """
    
    def __init__(self):
        self._database = Database()
        self._view = ReportView()
        
    def __call__(self):
        alpha_player_list = sorted(self._database.players, key=lambda k: k['name'])
        self._view.display_report()
        self._view.display_players_alpha(alpha_player_list)

        return True

    
class ReportRankPlayersController:
    """
    Affichage du rapport
    """
    
    def __init__(self):
        self._database = Database()
        self._view = ReportView()
        
    def __call__(self):
        rank_player_list = sorted(self._database.players, key=lambda k: k['ranking_elo'])
        self._view.display_report()
        self._view.display_players_rank(rank_player_list)

        return True


class ReportTournamentAlphaPlayersController:
    """
    Affichage du rapport
    """
    
    def __init__(self):
        self._database = Database()
        self._tournament = Tournament
        self._viewreport = ReportView()
        self._viewtournament = TournamentView
        
    def __call__(self):
        list_doc_id = []
        for tournament in self._database.tournaments:
            self._viewtournament.display_list_tournament(tournament.doc_id, tournament["name"])
            list_doc_id.append(tournament.doc_id)
            
        id_tournament = TournamentController.get_tournament(list_doc_id)
        self._tournament = self._tournament.deserializer(id_tournament)


        
        rank_player_list = sorted(self._database.tournaments, key=lambda k: k['ranking_elo'])
        self._viewreport.display_report()
        self._viewreport.display_players_rank(rank_player_list)

        return True

class ReportTournamentRankPlayersController:
    """
    Affichage du rapport
    """
    
    def __init__(self):
        self._database = Database()
        self._view = ReportView()
        
    def __call__(self):
        rank_player_list = sorted(self._database.tournaments, key=lambda k: k['ranking_elo'])
        self._view.display_report()
        self._view.display_players_rank(rank_player_list)

        return True
    
class ReportTournamentController:
    """
    Affichage du rapport
    """
    
    def __init__(self):
        self._database = Database()
        self._view = ReportView()
        
    def __call__(self):
        rank_player_list = sorted(self._database.tournaments, key=lambda k: k['ranking_elo'])
        self._view.display_report()
        self._view.display_players_rank(rank_player_list)

        return True
    
class ReportRoundsTournamentController:
    """
    Affichage du rapport
    """
    
    def __init__(self):
        self._database = Database()
        self._view = ReportView()
        
    def __call__(self):
        rank_player_list = sorted(self._database.tournaments, key=lambda k: k['ranking_elo'])
        self._view.display_report()
        self._view.display_players_rank(rank_player_list)

        return True
    

class ReportMatchTournamentController:
    """
    Affichage du rapport
    """
    
    def __init__(self):
        self._database = Database()
        self._view = ReportView()
        
    def display_players_rank(self):
        rank_player_list = sorted(self._database.tournaments, key=lambda k: k['ranking_elo'])
        self._view.display_report()
        self._view.display_players_rank(rank_player_list)

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