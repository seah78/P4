#! /usr/bin/env python3
# coding: utf-8

import datetime

class Player:
    """ Joueur """

    def __init__(self, name=None, first_name=None, birth_date=None, gender=None, ranking_elo=0, score=0.0):
        self.name = name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.ranking_elo = ranking_elo
        self.score = score
        self.opponant = []

    def __str__(self):
        return (f"Nom : {self.name} \nPrénom : {self.first_name}\nDate de naissance : {self.birth_date} \nSexe : {self.gender} \nClassement Elo : {self.ranking_elo} \nScore : {self.score}")

    """        
        def __repr__(self):
            pass
    """        


    """Calcul de l'age """

    """
    def age(self):
        if self.birth_date > datetime.date.today().replace(year = self.birth_date.year):
            return datetime.date.today().year - self.birth_date.year - 1
        else:
            return datetime.date.today().year - self.birth_date.year
    """

    def update_ranking(self):
        pass

    def update_score(self):
        pass

    def serializer(self):
        return {"name" : self.name,
                "first_name" : self.first_name,
                "birth_date" : self.birth_date,
                "gender" : self.gender,
                "ranking_elo" : self.ranking_elo,
                "score" : self.score }
        
    def serializer_player(self):
        return {"name" : self.name,
                "first_name" : self.first_name,
                "birth_date" : self.birth_date,
                "gender" : self.gender,
                "ranking_elo" : self.ranking_elo}

"""
    def deserializer(self):
        database = TinyDB('utils/database.json', indent=4)

        
        Tournaments = Query()
        tournament = database.search(Tournaments.name == 'Test Serializer')[0]


        player["name"], player["first_name"], player["birth_date"], player["gender"], player["ranking_elo"], player["score"]
"""