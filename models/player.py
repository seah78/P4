#! /usr/bin/env python3
# coding: utf-8

import datetime

class Player:
    """ Joueur """

    def __init__(self, name=None, first_name=None, birth_date=None, gender=None, ranking_elo=0, score=0):
        self.name = name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.ranking_elo = ranking_elo
        self.score = score

    def __str__(self):
        output = f"Nom : {self.name} /n
                    Prénom : {self.first_name} /n
                    Date de naissance : {self.birth_date} /n
                    Sexe : {self.gender} /n
                    Classement Elo : {self.ranking_elo}"


    """ Calcul de l'age"""
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



