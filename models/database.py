#! /usr/bin/env python3
# coding: utf-8


from tinydb import TinyDB, Query, where


class Database:
    
    
    def __init__(self):
        self.db = TinyDB("utils/database.json", indent=4)
        self.tournaments = self.db.table("tournaments")
        self.players = self.db.table("players")
    
    
    
    def save_tournament(self, serializer):
        self.tournaments.insert(serializer)
        
    def save_player(self, serializer):
        self.players.insert(serializer)
    
    """
    @staticmethod
    def save_tournament(serializer):
        database = TinyDB('utils/database.json', indent=4)
        tournament = database.table("tournaments")
        tournament.insert(serializer)
        
    @staticmethod
    def save_player(serializer):
        database = TinyDB('utils/database.json', indent=4)
        tournament = database.table("players")
        tournament.insert(serializer)
    """