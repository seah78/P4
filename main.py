#! /usr/bin/env python3
# coding: utf-8

import datetime

from controllers.tournamentcontroller import TournamentController 

"""PLAYERS = {"Sébastien": 1540, "Christophe": 1600, "Christian": 1610, "Francis": 1590, "Martin": 1020, "Paul": 940, "Guillaume": 1100, "Nicolas": 1090}"""


start = TournamentController()
start.new_tournament()
#start.display_tournament()