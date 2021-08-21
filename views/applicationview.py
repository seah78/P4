#! /usr/bin/env python3
# coding: utf-8

"""Vues de l'application et des menus"""


class MenuView:
    
    """
    Vues des menus
    """
    
    def __init__(self, menu):
        self.menu = menu
        
    def _display_menu(self):
        print("Choisissez votre option : \n")
        
        for key, entry in self.menu.items():
            print(f"{key}: {entry}\n")
            
    def user_choice(self):
        self._display_menu()
       
    @staticmethod    
    def get_user_choice():
        return input(">> ")
    
    @staticmethod
    def display_principal_menu():
        print("Menu principal")
        
    @staticmethod
    def display_report_menu():
        print("Menu des rapports")
    

class ReportView:
    
    @staticmethod
    def display_report():
        print("Affichage du rapport")

    
class ReturnView:
    
    @staticmethod
    def display_return():
        print("Retour au menu principal")
        
            
class EndView:
    
    @staticmethod
    def quit():
        print("Au revoir")