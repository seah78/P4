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
        
    def update_tournament(self, serializer, id_tournament):
        item = self.tournaments.get(doc_id=id_tournament)
        print(item)
        #name_tournament = self.tournaments.get(doc_id=id_tournament)
        #print(name_tournament["name"])
        #Tournament = Query()
        #update_tournament = self.tournaments.search(Tournament.name == name_tournament["name"])
        #update_tournament = self.tournaments.get(doc_id=id_tournament)
        #request = Query()
        #print(update_tournament)
        


        
        #self.tournaments.update(serializer, self.tournaments.search(Tournament.name == name_tournament["name"]))
        
        self.tournaments.update(serializer, item)

        
    def save_player(self, serializer):
        self.players.insert(serializer)
    
