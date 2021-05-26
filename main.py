#! /usr/bin/env python3
# coding: utf-8

import datetime

from models.player import Player 




player = Player("HERLANT", "Sébastien", datetime.date(1978, 3, 3), "M", 1500, 150)   


print(f"Joueur blanc : {player.name} {player.first_name} {player.age()} ans")