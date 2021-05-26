#! /usr/bin/env python3
# coding: utf-8

import datetime

class Player:
    """ Joueur """

    def __init__(self, name, first_name, birth_date, gender, ranking, score):
        self.name = name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.ranking = ranking
        self.score = score


    """ Calcul de l'age"""
    def age(self):
        if self.birth_date > datetime.date.today().replace(year = self.birth_date.year):
            return datetime.date.today().year - self.birth_date.year - 1
        else:
            return datetime.date.today().year - self.birth_date.year



