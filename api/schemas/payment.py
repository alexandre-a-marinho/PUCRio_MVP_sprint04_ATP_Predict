from pydantic import BaseModel
from typing import List
from model.payment import Payment
from datetime import date

#  --------------------------------------------------------------------------------------
#  Schemas
#  --------------------------------------------------------------------------------------
class PaymentSchema(BaseModel):
    """Defines how a new Payment must be represented for database insertion"""
    surface: str = "Hard"
    year: int = 2023
    tourney_level: str = "G"
    best_of_x_sets: int = 5
    tourney_round: str = "F"
    first_name: str = "Djokovic"
    first_hand: str = "R"
    first_id: int = 1001
    first_rank: float = 1
    first_rank_points: float = 11500
    first_age: float = 36
    first_height: float = 188
    second_name: str = "Alcaraz"
    second_hand: str = "R"
    second_id: int = 1002
    second_rank: float = 2
    second_rank_points: float = 9500
    second_age: float = 20
    second_height: float = 183


class PaymentSearchSchema(BaseModel):
    """Defines the structure of the requisition that searches for Payments.

    The search is made using the Payment Id.
    """
    id: int = 5


class PaymentsListSchema(BaseModel):
    """Defines how to return a Payments list."""
    payments: List[PaymentSchema]


class PaymentViewSchema(BaseModel):
    """Defines how to return a single Payment."""
    id: int = 1
    surface: str = "Hard"
    year: int = 2023
    tourney_level: str = "G"
    best_of_x_sets: int = 5
    tourney_round: str = "F"
    first_name: str = "Djokovic"
    first_hand: str = "R"
    first_id: int = 1001
    first_rank: float = 1
    first_rank_points: float = 11500
    first_age: float = 36
    first_height: float = 188
    second_name: str = "Alcaraz"
    second_hand: str = "R"
    second_id: int = 1002
    second_rank: float = 2
    second_rank_points: float = 9500
    second_age: float = 20
    second_height: float = 183
    winner: str = "Djokovic"


class PaymentDelSchema(BaseModel):
    """Defines the structure of the requisition that deletes a Payment."""
    message: str = "Information regarding deletion success/failure"
    id: int = 5


#  --------------------------------------------------------------------------------------
#  Auxiliary functions
#  --------------------------------------------------------------------------------------
def show_payments(payments: List[Payment]):
    """Returns the representation of a group of Payments."""
    result = []
    for payment in payments:
        result.append({
            "id": payment.id,
            "surface": payment.surface,
            "year": payment.year,
            "tourney_level":payment.tourney_level,
            "best_of_x_sets": payment.best_of_x_sets,
            "tourney_round": payment.tourney_round,
            "first_name": payment.first_name,
            "first_hand": payment.first_hand,
            "first_id": payment.first_id,
            "first_rank": payment.first_rank,
            "first_rank_points":payment.first_rank_points,
            "first_age": payment.first_age,
            "first_height": payment.first_height,
            "second_name": payment.second_name,
            "second_hand": payment.second_hand,
            "second_id": payment.second_id,
            "second_rank": payment.second_rank,
            "second_rank_points": payment.second_rank_points,
            "second_age": payment.second_age,
            "second_height": payment.second_height,
            "winner": payment.winner,
            })

    return {"payments": result}

def show_payment(payment: Payment):
    """Returns the representation of a Payment as per the PaymentViewSchema."""
    return {
        "id": payment.id,
        "surface": payment.surface,
        "year": payment.year,
        "tourney_level":payment.tourney_level,
        "best_of_x_sets": payment.best_of_x_sets,
        "tourney_round": payment.tourney_round,
        "first_name": payment.first_name,
        "first_hand": payment.first_hand,
        "first_id": payment.first_id,
        "first_rank": payment.first_rank,
        "first_rank_points":payment.first_rank_points,
        "first_age": payment.first_age,
        "first_height": payment.first_height,
        "second_name": payment.second_name,
        "second_hand": payment.second_hand,
        "second_id": payment.second_id,
        "second_rank": payment.second_rank,
        "second_rank_points": payment.second_rank_points,
        "second_age": payment.second_age,
        "second_height": payment.second_height,
        "winner": payment.winner,
    }
