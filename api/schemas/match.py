from pydantic import BaseModel
from typing import List
from model.match import Match
from datetime import date

#  --------------------------------------------------------------------------------------
#  Schemas
#  --------------------------------------------------------------------------------------
class MatchSchema(BaseModel):
    """Defines how a new Match must be represented for database insertion"""
    surface: str = "Hard"
    year: int = 2022
    tourney_level: str = "M"
    best_of_x_sets: int = 3
    tourney_round: str = "F"
    first_name: str = "Djokovic"
    first_hand: str = "R"
    first_id: int = 104925
    first_rank: float = 1
    first_rank_points: float = 11245
    first_age: float = 36
    first_height: float = 188
    second_name: str = "Alcaraz"
    second_hand: str = "R"
    second_id: int = 106688
    second_rank: float = 2
    second_rank_points: float = 8855
    second_age: float = 20
    second_height: float = 183


class MatchSearchSchema(BaseModel):
    """Defines the structure of the requisition that searches for Matches.

    The search is made using the Match Id.
    """
    id: int = 5


class MatchesListSchema(BaseModel):
    """Defines how to return a Matches list."""
    matches: List[MatchSchema]


class MatchViewSchema(BaseModel):
    """Defines how to return a single Match."""
    id: int = 1
    surface: str = "Hard"
    year: int = 2022
    tourney_level: str = "M"
    best_of_x_sets: int = 3
    tourney_round: str = "F"
    first_name: str = "Djokovic"
    first_hand: str = "R"
    first_id: int = 104925
    first_rank: float = 1
    first_rank_points: float = 11245
    first_age: float = 36
    first_height: float = 188
    second_name: str = "Alcaraz"
    second_hand: str = "R"
    second_id: int = 106688
    second_rank: float = 2
    second_rank_points: float = 8855
    second_age: float = 20
    second_height: float = 183
    winner: str = "Djokovic"


class MatchDelSchema(BaseModel):
    """Defines the structure of the requisition that deletes a Match."""
    message: str = "Information regarding deletion success/failure"
    id: int = 5


#  --------------------------------------------------------------------------------------
#  Auxiliary functions
#  --------------------------------------------------------------------------------------
def show_matches(matches: List[Match]):
    """Returns the representation of a group of Matches."""
    result = []
    for match in matches:
        result.append({
            "id": match.id,
            "surface": match.surface,
            "year": match.year,
            "tourney_level":match.tourney_level,
            "best_of_x_sets": match.best_of_x_sets,
            "tourney_round": match.tourney_round,
            "first_name": match.first_name,
            "first_hand": match.first_hand,
            "first_id": match.first_id,
            "first_rank": match.first_rank,
            "first_rank_points":match.first_rank_points,
            "first_age": match.first_age,
            "first_height": match.first_height,
            "second_name": match.second_name,
            "second_hand": match.second_hand,
            "second_id": match.second_id,
            "second_rank": match.second_rank,
            "second_rank_points": match.second_rank_points,
            "second_age": match.second_age,
            "second_height": match.second_height,
            "winner": match.winner,
            })

    return {"matches": result}

def show_match(match: Match):
    """Returns the representation of a Match as per the MatchViewSchema."""
    return {
        "id": match.id,
        "surface": match.surface,
        "year": match.year,
        "tourney_level":match.tourney_level,
        "best_of_x_sets": match.best_of_x_sets,
        "tourney_round": match.tourney_round,
        "first_name": match.first_name,
        "first_hand": match.first_hand,
        "first_id": match.first_id,
        "first_rank": match.first_rank,
        "first_rank_points":match.first_rank_points,
        "first_age": match.first_age,
        "first_height": match.first_height,
        "second_name": match.second_name,
        "second_hand": match.second_hand,
        "second_id": match.second_id,
        "second_rank": match.second_rank,
        "second_rank_points": match.second_rank_points,
        "second_age": match.second_age,
        "second_height": match.second_height,
        "winner": match.winner,
    }
