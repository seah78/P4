#! /usr/bin/env python3
# coding: utf-8

class Player:
    """Joueur"""

    def __init__(
        self,
        name=None,
        first_name=None,
        birth_date=None,
        gender=None,
        ranking_elo=0,
        score=0.0,
    ):
        self.name = name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.ranking_elo = ranking_elo
        self.score = score
        self.opponant = []

    def __str__(self):
        return {f"Nom : {self.name} \n"
                f"Prénom : {self.first_name} \n"
                f"Date de naissance : {self.birth_date} \n"
                f"Sexe : {self.gender} \n"
                f"Classement Elo : {self.ranking_elo} \n"
                f"Score : {self.score}"}

    def set_opponant(self, opponant):
        self.opponant = opponant
    

    def serializer(self):
        return {
            "name": self.name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "gender": self.gender,
            "ranking_elo": self.ranking_elo,
            "score": self.score,
            #"opponant": self.opponant
        }

    def serializer_player(self):
        return {
            "name": self.name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "gender": self.gender,
            "ranking_elo": self.ranking_elo,
        }
