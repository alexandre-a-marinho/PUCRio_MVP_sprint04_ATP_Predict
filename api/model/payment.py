from sqlalchemy import Column, String, Integer, Date, Float
from datetime import date
from typing import Union

from model import Base


class Payment(Base):
    __tablename__ = 'payments'

    id = Column("pk_payment", Integer, primary_key = True)
    surface = Column(String(20), default = "Hard")
    year = Column(Integer, default = 2023)
    tourney_level = Column(String(1), default = "M")
    best_of_x_sets = Column(Integer, default = 3)
    tourney_round = Column(String(4), default = "F")
    first_name = Column(String(40))
    first_hand = Column(String(4), default = "R")
    first_id = Column(Integer)
    first_rank = Column(Float, defaul = 2.0)
    first_rank_points = Column(Float, default = 8500.0)
    first_age = Column(Float, default = 26.0)
    first_height = Column(Float, default = 180.0)
    second_name = Column(String(40))
    second_hand = Column(String(4), default = "L")
    second_id = Column(Integer)
    second_rank = Column(Float, default = 4.0)
    second_rank_points = Column(Float, default = 7000.0)
    second_age = Column(Float, default = 26.0)
    second_height = Column(Float, default = 180.0)
    winner = Column(String(40))

    def __init__(self, surface:str, year:int, tourney_level:str, best_of_x_sets:int, tourney_round:str,
                 first_name:str, first_hand:str, first_id:int, first_rank:float, first_rank_points:float, first_age:float, first_height:float,
                 second_name:str, second_hand:str, second_id:int, second_rank:float, second_rank_points:float, second_age:float, second_height:float,
                 winner_code:int):
        """Creates a Payment.

        Arguments:
        description = description of the goods/services being paid for
        category = category of the goods/services being paid for (exs: Market, Sports, Restaurant, Trip, etc)
        subcategory = subcategory of the goods/services being paid for (ex: em Mercado: Hortifruti, Higiene, Açougue, etc)
        value: total value of the Payment, in Reais (R$). It's the sum of all installments
        nb_installments = number of monthly installments
        insertion_date: when the Payment was inserted in the database
        """
        self.surface = surface
        self.year = year
        self.tourney_level = tourney_level
        self.best_of_x_sets = best_of_x_sets
        self.tourney_round = tourney_round
        self.first_name = first_name
        self.first_hand = first_hand
        self.first_id = first_id
        self.first_rank = first_rank
        self.first_rank_points = first_rank_points
        self.first_age = first_age
        self.first_height = first_height
        self.second_name = second_name
        self.second_hand = second_hand
        self.second_id = second_id
        self.second_rank = second_rank
        self.second_rank_points = second_rank_points
        self.second_age = second_age
        self.second_height = second_height
        
        if (winner_code == 0):
            self.winner = first_name
        elif (winner_code == 1):
            self.winner = second_name
        else:
            self.winner = "invalid winner code"
            
    @staticmethod
    def getUncodedWinner(winner_code, form):
        if (winner_code == 0):
            return  form.first_name
        elif (winner_code == 1):
            return  form.second_name
        else:
            return "invalid winner code"
