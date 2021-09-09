#! /usr/bin/env python3
# coding: utf-8

from tinydb import TinyDB, Query, where


"""Models"""
from models.application import Menu
from models.tournament import Tournament
from models.database import Database
"""Views"""
from views.applicationview import MenuView
from views.applicationview import ReportView
from views.applicationview import EndView
from views.errorview import ErrorView
from views.tournamentview import TournamentView
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
            self._menu.add("auto", "Liste des joueurs par ordre alphabétique", ReportAlphaPlayersController())
            self._menu.add("auto", "Liste des joueurs par classement ELO", ReportRankPlayersController())
            self._menu.add("auto", "Liste des joueurs d'un tournoi par par ordre alphabétique", ReportTournamentAlphaPlayersController())
            self._menu.add("auto", "Liste des joueurs d'un tournoi par classement ELO", ReportTournamentRankPlayersController())
            self._menu.add("auto", "Liste des tournois", ReportTournamentController())
            self._menu.add("auto", "Liste des rondes d'un tournoi", ReportRoundsTournamentController())
            self._menu.add("auto", "Liste des matchs d'un tournoi", ReportMatchTournamentController())

        else:
            self._menu.add("auto", "Créer un tournoi.", CreateTournamentController(self._tournament))
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
        for player in alpha_player_list:
            self._view.display_player(player)

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
        for player in rank_player_list:
            self._view.display_player(player)
        return True


class ReportTournamentAlphaPlayersController:
    """
    Affichage du rapport
    """
    
    def __init__(self):
        self._database = Database()
        self._viewreport = ReportView()
        self._viewtournament = TournamentView()
        
    def __call__(self):
        list_doc_id = []
        for tournament in self._database.tournaments:
            self._viewtournament.display_list_tournament(tournament.doc_id, tournament["name"])
            list_doc_id.append(tournament.doc_id)
            
        id_tournament = TournamentController.get_tournament(list_doc_id)
        tournament = self._database.tournaments.get(doc_id = id_tournament)
        
        alpha_player_list = sorted(tournament['players'], key=lambda k: k['name'])
        self._viewreport.display_report()
        for player in alpha_player_list:
            self._viewreport.display_player(player)

        return True


class ReportTournamentRankPlayersController:
    """
    Affichage du rapport
    """
    
    def __init__(self):
        self._database = Database()
        self._viewreport = ReportView()
        self._viewtournament = TournamentView()
                
    def __call__(self):
        list_doc_id = []
        for tournament in self._database.tournaments:
            self._viewtournament.display_list_tournament(tournament.doc_id, tournament["name"])
            list_doc_id.append(tournament.doc_id)
            
        id_tournament = TournamentController.get_tournament(list_doc_id)
        tournament = self._database.tournaments.get(doc_id = id_tournament)
        
        rank_player_list = sorted(tournament['players'], key=lambda k: k['ranking_elo'])
        self._viewreport.display_report()
        for player in rank_player_list:
            self._viewreport.display_player(player)

        return True

    
class ReportTournamentController:
    """
    Affichage du rapport
    """
    
    def __init__(self):
        self._database = Database()
        self._viewreport = ReportView()
        self._viewtournament = TournamentView()
                
    def __call__(self):
        self._viewreport.display_report()
        for tournament in self._database.tournaments:
            self._viewtournament.display_all_items_list_tournament(tournament.doc_id, 
                                                                   tournament["name"], 
                                                                   tournament["place"], 
                                                                   tournament["start_date"], 
                                                                   tournament["end_date"], 
                                                                   tournament["total_rounds"])

        return True

    
class ReportRoundsTournamentController:
    """
    Affichage du rapport
    """
    
    def __init__(self):
        self._database = Database()
        self._viewreport = ReportView()
        self._viewtournament = TournamentView()
        
    def __call__(self):
        list_doc_id = []
        for tournament in self._database.tournaments:
            self._viewtournament.display_list_tournament(tournament.doc_id, tournament["name"])
            list_doc_id.append(tournament.doc_id)
            
        id_tournament = TournamentController.get_tournament(list_doc_id)
        tournament = self._database.tournaments.get(doc_id = id_tournament)
        
        for round in tournament["rounds"]:
            self._viewtournament.display_round_tournament(round)
            for player in round["players"]:
                self._viewreport.display_player(player)

        return True
    

class ReportMatchTournamentController:
    """
    Affichage du rapport
    """
    
    def __init__(self):
        self._database = Database()
        self._viewreport = ReportView()
        self._viewtournament = TournamentView()
        
    def __call__(self):
        list_doc_id = []
        for tournament in self._database.tournaments:
            self._viewtournament.display_list_tournament(tournament.doc_id, tournament["name"])
            list_doc_id.append(tournament.doc_id)

        id_tournament = TournamentController.get_tournament(list_doc_id)
        tournament = self._database.tournaments.get(doc_id = id_tournament)

        for round in tournament["rounds"]:
            self._viewtournament.display_round_tournament(round)
            for indice, match in enumerate(round["matchs"], start=1):
                self._viewreport.display_match(indice,
                                               match["white_player"], 
                                               match["black_player"], 
                                               match["white_score"], 
                                               match["black_player"])
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