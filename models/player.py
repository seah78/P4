#! /usr/bin/env python3
# coding: utf-8

import datetime

class Player:
	"""docstrings"""

	def __init__(self):
		self.name = ""
		self.first_name = ""
		self.birth_date = ""
		self.gender = ""
		self.ranking = ""
		self.score = ""


	""" Calcul de l'age"""
	def age(self):
	    if self.birth_date > datetime.date.today().replace(year = self.birth_date.year):
	        return datetime.date.today().year - self.birth_date.year - 1
	    else:
	        return datetime.date.today().year - self.birth_date.year

player = Player()	
player.name = "HERLANT"
player.first_name = "Sébastien"
player.birth_date = datetime.date(1978, 3, 3)
player.gender = "M"
player.ranking = 1500
player.score = 150

print(f"Joueur blanc : {player.name} {player.first_name} {player.age()} ans")

