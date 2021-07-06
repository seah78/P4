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
        data = {"Nom" : self.name,
                "Prénom" : self.first_name,
                "Date de naissance" : self.birth_date,
                "Sexe" : self.gender,
                "Classement ELO" : self.ranking_elo,
                "score" : self.score }
        return data
        
    def serializer_player(self):
        data = {"Nom" : self.name,
                "Prénom" : self.first_name,
                "Date de naissance" : self.birth_date,
                "Sexe" : self.gender,
                "Classement ELO" : self.ranking_elo}
        return data
