#! /usr/bin/env python3
# coding: utf-8

class Database:
    
    def __init__(self):
        self.dbtournament = None
        
    def savetournament(self):
        pass
    
    def reloadtournament(self):
        pass
    
    def updatetournament(self):
        pass
    
"""    
class Player:
    def __init__(self, name, elo, score):
        self.name = name
        self.elo = elo
        self.score = score
        
        
    def serializer(self):
        data = {"name" : self.name,
                "elo" : self.elo,
                "score" : self.score}
        return data
        
    def serializer_player(self):
        data = {"name" : self.name,
                "elo" : self.elo}
        return data


players = [Player("Ranga", 34, 3), Player("GrÃ©gory", 12, 3), Player("Jean-Marie", 3, 0), Player("toto", 100, 1), Player("Albert", 45, 2), Player("Charles", 23, 1), Player("Marie", 9, 2), Player("Laura", 4, 0)]

class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score_player1 = 0
        self.score_player2 = 0
        
    def serializer(self):
        data = {"player1" : self.player1.serializer(),
                "player2" : self.player2.serializer(),
                "score_player1" : self.score_player1,
                "score_player2" : self.score_player2}
        return data
        
class Round:
    def __init__(self, number):
        self.number = number
        self.matchs = []
        
    def add_match(self, player1, player2): #1
        match = Match(player1, player2)
        self.matchs.append(match)
        
    def serializer(self):
        data = {"number" : self.number,
                "matchs" : [match.serializer() for match in self.matchs]}
        return data

class Tournament:
    def __init__(self, name, place):
        self.name = name
        self.place = place
        self.players = players
        self.rounds = list()
        
    def add_round(self, round):
        self.rounds.append(round)
        
        
    def serializer(self):
        data = {"name" : self.name,
                "place" : self.place,
                "players" : [player.serializer() for player in self.players],
                "rounds" : [round.serializer() for round in self.rounds]
        }
        return data
        
        
tournament = Tournament("Tournament-Test", "Paris")
round = Round("1")
round.add_match(players[0], players[1])
round.add_match(players[2], players[3])
round.add_match(players[4], players[5])
round.add_match(players[6], players[7])

round2 = Round("2")
round2.add_match(players[0], players[7])
round2.add_match(players[1], players[6])
round2.add_match(players[2], players[5])
round2.add_match(players[3], players[4])

tournament.add_round(round)
tournament.add_round(round2)

print(tournament.serializer())
"""


"""
class Player:
    def __init__(self, name, elo, score=0):
        self.name = name
        self.elo = elo
        self.score = score
        
        
    def serializer(self):
        data = {"name" : self.name,
                "elo" : self.elo,
                "score" : self.score}
        return data
        
    def serializer_player(self):
        data = {"name" : self.name,
                "elo" : self.elo}
        return data


players = [Player("Ranga", 34, 3), Player("Gregory", 12, 3), Player("Jean-Marie", 3, 0), Player("toto", 100, 1), Player("Albert", 45, 2), Player("Charles", 23, 1), Player("Marie", 9, 2), Player("Laura", 4, 0)]

class Match:
    def __init__(self, player1, player2, score_player1 = 0, score_player2 = 0):
        self.player1 = player1
        self.player2 = player2
        self.score_player1 = 0
        self.score_player2 = 0
        
    def serializer(self):
        data = {"player1" : self.player1.serializer(),
                "player2" : self.player2.serializer(),
                "score_player1" : self.score_player1,
                "score_player2" : self.score_player2}
        return data
        
class Round:
    def __init__(self, number):
        self.number = number
        self.matchs = []
        
    def add_match(self, player1, player2): #1
        match = Match(player1, player2)
        self.matchs.append(match)
        
    def add_reload_match(self, match):
        self.matchs.append(match)
        
    def serializer(self):
        data = {"number" : self.number,
                "matchs" : [match.serializer() for match in self.matchs]}
        return data

class Tournament:
    def __init__(self, name, place):
        self.name = name
        self.place = place
        self.players = players
        self.rounds = list()
        
    def add_player(self, player):
        self.players.append(player)
        
    def add_round(self, round):
        self.rounds.append(round)
        
        
    def serializer(self):
        data = {"name" : self.name,
                "place" : self.place,
                "players" : [player.serializer() for player in self.players],
                "rounds" : [round.serializer() for round in self.rounds]
        }
        return data
        

class TournamentControler:
    def __init__(self):
        self.tournament = None
        self.json = None
        
    def new_tournament(self):
        self.tournament = Tournament("Tournament-Test", "Paris")
        round = Round("1")
        round.add_match(players[0], players[1])
        round.add_match(players[2], players[3])
        round.add_match(players[4], players[5])
        round.add_match(players[6], players[7])
        
        round2 = Round("2")
        round2.add_match(players[0], players[7])
        round2.add_match(players[1], players[6])
        round2.add_match(players[2], players[5])
        round2.add_match(players[3], players[4])
        
        self.tournament.add_round(round)
        self.tournament.add_round(round2)
        self.json = self.tournament.serializer()
        
    def reload_tournament(self):
        self.tournament = None # je met none car dans le cas normal il serait à None.
        #Il va aller lire le json et récupérer l'information du tournoi qu'on veut reprendre (Dans notre exemple self.json)
        self.deserilizer()
        number_round_to_run = 4 - len(self.json["rounds"])
        print(number_round_to_run)
        
        if number_round_to_run == 4:
            pass
            #run_first_round()
        else:
            for i in range(len(self.json["rounds"]) + 1, 5):
                pass
                #run_round(i)
        
    def deserilizer(self):
        self.tournament = Tournament(self.json["name"], self.json["place"])
        self.tournament.players = []
        
        for player in self.json["players"]:
            reload_player = Player(player["name"], player["elo"], player["score"])
            self.tournament.add_player(reload_player)
            
        for round in self.json["rounds"]:
            reload_round = Round(round["number"])
            for match in round["matchs"]:
                player1 = Player(match["player1"]["name"], match["player1"]["elo"], match["player1"]["score"])
                player2 = Player(match["player2"]["name"], match["player1"]["elo"], match["player1"]["score"])
                
                reload_match = Match(player1, player2, match["score_player1"], match["score_player2"])
                
                reload_round.add_reload_match(reload_match)
            self.tournament.add_round(reload_round)
            #return tournament
        print(self.tournament.serializer())
        
        
        
        
tournamentControler = TournamentControler()  
tournamentControler.new_tournament()
#On arrête le programme

tournamentControler.reload_tournament()
"""