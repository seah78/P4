#! /usr/bin/env python3
# coding: utf-8

import datetime
from dateutil.parser import parse

from controllers.tournamentcontroller import TournamentController 

start = TournamentController()
start.new_tournament()
#start.display_tournament()


