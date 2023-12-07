from sqlalchemy import Column, String, Integer, Date, Float, CheckConstraint
from datetime import date
from typing import Union

from model import Base

class Match(Base):
    __tablename__ = 'matches'

    id = Column("pk_match", Integer, primary_key = True)
    surface = Column(String(20), default = "Hard")
    year = Column(Integer, default = 2023)
    tourney_level = Column(String(1), default = "M")
    best_of_x_sets = Column(Integer, default = 3)
    tourney_round = Column(String(4), default = "F")
    first_name = Column(String(40))
    first_id = Column(Integer)
    first_rank = Column(Float, default = 2.0)
    first_rank_points = Column(Float, default = 8500.0)
    first_hand = Column(String(4), default = "R")
    first_height = Column(Float, default = 180.0)
    first_age = Column(Float, default = 26.0)
    second_name = Column(String(40))
    second_id = Column(Integer)
    second_rank = Column(Float, default = 4.0)
    second_rank_points = Column(Float, default = 7000.0)
    second_hand = Column(String(4), default = "L")
    second_height = Column(Float, default = 180.0)
    second_age = Column(Float, default = 26.0)
    winner = Column(String(40))

    def __init__(self, surface:str, year:int, tourney_level:str, best_of_x_sets:int, tourney_round:str,
                 first_name:str, first_hand:str, first_id:int, first_rank:float, first_rank_points:float, first_age:float, first_height:float,
                 second_name:str, second_hand:str, second_id:int, second_rank:float, second_rank_points:float, second_age:float, second_height:float,
                 winner_code:int):
        """Creates a Match.

        Arguments:
        surface = court surface type ("Carpet", "Grass", "Hard", "Clay")
        year = year in which the match took place
        tourney_level = level of difficulty of the tournament ()"A": ATP 250/500, "D": Davis Cup, "F": ATP Finals , "G": Grand Slam, "M": MAster 1000)
        best_of_x_sets: Maximum nuber of sets to be played in the match (3, 5)
        tourney_round = tournament rounf ("BR", "ER", "F": final, "QF": quarter-final, "R128", "R16", "R32", "R64", "RR": round robin, "SF": semi-final)
        first_name: name of player 1
        first_id: ATP id of player 1
        first_rank: ATP rank of player 1
        first_rank_points: ATP rank points of player 1
        first_hand: dominant hand of player 1 ("L": left, "R": right)
        first_height: height of player 1
        first_age: age of player 1
        second_name: name of player 2
        second_id: ATP id of player 2
        second_rank: ATP rank of player 2
        second_rank_points: ATP rank points of player 2
        second_hand: dominant hand of player 2 ("L": left, "R": right)
        second_height: height of player 2
        second_age: age of player 2
        """
        self.surface = surface
        self.year = year
        self.tourney_level = tourney_level
        self.best_of_x_sets = best_of_x_sets
        self.tourney_round = tourney_round
        self.first_name = first_name
        self.first_id = first_id
        self.first_rank = first_rank
        self.first_rank_points = first_rank_points
        self.first_hand = first_hand
        self.first_height = first_height
        self.first_age = first_age
        self.second_name = second_name
        self.second_id = second_id
        self.second_rank = second_rank
        self.second_rank_points = second_rank_points
        self.second_hand = second_hand
        self.second_height = second_height
        self.second_age = second_age
        
        if (winner_code == 0):
            self.winner = first_name
        elif (winner_code == 1):
            self.winner = second_name
        else:
            self.winner = "invalid winner code"
            
    @staticmethod
    def get_uncoded_winner(winner_code, form):
        """Gets winner string name based ou winner integer code.
        
        Arguments:
        winner_code = match winner integer code (0 or 1)
        form = match form containing string names of the players
        """
        if (winner_code == 0):
            return  form.first_name
        elif (winner_code == 1):
            return  form.second_name
        else:
            return "Invalid winner code!"
