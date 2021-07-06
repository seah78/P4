#! /usr/bin/env python3
# coding: utf-8

from tinydb import TinyDB, Query

class DataBase:


    
    @staticmethod    
    def save_database(serializer):
        database = TinyDB('utils/database.json')
        database.insert(serializer)
    
    
    def reload_database(self):
        pass
        


"""
database = TinyDB('database.json')


database.insert({"type": "apple", "count": 7})
"""