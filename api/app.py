from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from flask_caching import Cache
from datetime import date

from sqlalchemy.exc import IntegrityError
from sqlalchemy import func

from model import Session, Match, Model
from logger import logger
from schemas import *
from flask_cors import CORS


# Creating OpenAPI object
info = Info(title="Matches Control", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Defining tags
home_tag = Tag(name="Documentation", description="Documentation selection: Swagger, Redoc or RapiDoc")
match_tag = Tag(name="Match", description="Addition, visualization, edition and deletion of matches from the database")
analysis_tag = Tag(name="Analysis", description="Statistics and analysis regarding the matches in the database")

# Sets cache
app.config['CACHE_TYPE'] = 'simple'
app.config["DEBUG"] = True
cache = Cache(app)

#  --------------------------------------------------------------------------------------
#  Routes
#  --------------------------------------------------------------------------------------
@app.get('/', tags=[home_tag])
def home():
    """Redirects to /openapi, allowing us to chose the type of documentation."""
    return redirect('/openapi')


@app.post('/match', tags=[match_tag],
          responses={"200": MatchViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_match(form: MatchSchema):
    """Adds a new Match to the database.

    Returns the representation of the added Match (as per MatchViewSchema).
    """
    
    # Loading the prediction model
    model_obj_path = 'ml_model/atp_model.pkl'
    model = Model.load_external_python_object(model_obj_path)
    form_encoded = Model.encode_match_form_data(form)
    
    match = Match(
        surface = form.surface,
        year = form.year,
        tourney_level = form.tourney_level,
        best_of_x_sets = form.best_of_x_sets,
        tourney_round = form.tourney_round,
        first_name = form.first_name,
        first_hand = form.first_hand,
        first_id = form.first_id,
        first_rank = form.first_rank,
        first_rank_points = form.first_rank_points,
        first_age = form.first_age,
        first_height = form.first_height,
        second_name = form.second_name,
        second_hand = form.second_hand,
        second_id = form.second_id,
        second_rank = form.second_rank,
        second_rank_points = form.second_rank_points,
        second_age = form.second_age,
        second_height = form.second_height,
        winner_code = Model.predictor(model, form_encoded)
    )
    
    logger.debug(f"Added Match between '{match.first_name}' and '{match.second_name}'.")
    try:
        # Creates database connection
        session = Session()

        # Adds new item to the database table and commits it
        session.add(match)
        session.commit()
        logger.debug(f"Added Match between '{match.first_name}' and '{match.second_name}'.")
        return show_match(match), 200

    except IntegrityError as e:
        error_msg = "Integrity error on new Match addition :/"
        logger.warning(f"Error while adding Match #{match.id} between '{match.first_name}' and '{match.second_name}': {error_msg}")
        return {"message": error_msg}, 409

    except Exception as e:
        # in case of a non-expected error
        error_msg = "It was not possible to save the new Match :/"
        logger.warning(f"Error while adding Match #{match.id} between '{match.first_name}' and '{match.second_name}': {error_msg}")
        return {"message": error_msg}, 400


@app.put('/matchedition', tags=[match_tag],
          responses={"200": MatchViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def edit_match(query: MatchSearchSchema, form: MatchSchema,):
    """Edits an existing Match in the database.

    Returns the representation of the edited Match (as per MatchViewSchema).
    """
    edited_match_id = query.id
    logger.debug(f"Editing Match #{edited_match_id} between '{form.first_name}' and '{form.second_name}'.")
    
    # Loading the prediction model
    model_obj_path = 'ml_model/atp_model.pkl'
    model = Model.load_external_python_object(model_obj_path)
    form_encoded = Model.encode_match_form_data(form)
    
    try:
        # Creates database connection
        session = Session()
        
        # Selects item to edit it in the database table and then commits it
        to_edit = session.query(Match).filter(Match.id == edited_match_id).first()
        to_edit.surface = form.surface
        to_edit.year = form.year
        to_edit.tourney_level = form.tourney_level
        to_edit.best_of_x_sets = form.best_of_x_sets
        to_edit.tourney_round = form.tourney_round
        to_edit.first_name = form.first_name
        to_edit.first_hand = form.first_hand
        to_edit.first_id = form.first_id
        to_edit.first_rank = form.first_rank
        to_edit.first_rank_points = form.first_rank_points
        to_edit.first_age = form.first_age
        to_edit.first_height = form.first_height
        to_edit.second_name = form.second_name
        to_edit.second_hand = form.second_hand
        to_edit.second_id = form.second_id
        to_edit.second_rank = form.second_rank
        to_edit.second_rank_points = form.second_rank_points
        to_edit.second_age = form.second_age
        to_edit.second_height = form.second_height

        winner_code = Model.predictor(model, form_encoded)
        to_edit.winner = Match.get_uncoded_winner(winner_code, form)

        session.commit()
        
        return show_match(to_edit), 200

    except IntegrityError as e:
        error_msg = "Integrity error on new Match addition :/"
        logger.warning(f"Error while editing Match #{to_edit.id} between '{to_edit.first_name}' and '{to_edit.second_name}': {error_msg}")
        return {"message": error_msg}, 409

    except Exception as e:
        # in case of a non-expected error
        error_msg = "It was not possible to save the new Match :/"
        logger.warning(f"Error while editing Match #{to_edit.id} between '{to_edit.first_name}' and '{to_edit.second_name}': {error_msg}")
        return {"message": error_msg}, 400


@app.get('/matches', tags=[match_tag],
         responses={"200": MatchesListSchema, "404": ErrorSchema})
def get_matches():
    """Searches for all registered Matches.

    Returns the representation of a list of all registred Matches (if any exists).
    """
    logger.debug(f"Getting Matches")
    
    # Creates database connectio to perform the search
    session = Session()
    matches = session.query(Match).all()

    if matches:
        logger.debug(f"%d Matches found" % len(matches))
        print(matches)
        # retuns the representation of the list of all matches found
        return show_matches(matches), 200
    else:
        # retorno empty if nothing is found
        return {"matches": []}, 200


@app.get('/match', tags=[match_tag],
         responses={"200": MatchViewSchema, "404": ErrorSchema})
def get_match(query: MatchSearchSchema):
    """Searches a Match based on it's Id.

    Returns the representation of a Match (if found).
    """
    match_id = query.id
    logger.debug(f"Getting Match data #{match_id}")

    # Creates database connectio to perform the search
    session = Session()

    # Searchs using match Id
    match = session.query(Match).filter(Match.id == match_id).first()

    if match:
        logger.debug(f"Match found: #{match_id}")
        return show_match(match), 200
    else:
        error_msg = "Match not found in database :/"
        logger.warning(f"Error while searching for Match #{match.id} between '{match.first_name}' and '{match.second_name}': {error_msg}")
        return {"message": error_msg}, 404


@app.delete('/match', tags=[match_tag],
            responses={"200": MatchDelSchema, "404": ErrorSchema})
def del_match(query: MatchSearchSchema):
    """Deletes a Match based on it's Id.

    Returns a message confirming target Match deletion.
    """
    match_id = query.id
    logger.debug(f"Deleting Match #{match_id}")

    # Creates database connection to perform the search
    session = Session()
    
    # Searching and deleting target Match
    match_to_delete: Match = session.query(Match).filter(Match.id == match_id).first()
    match_first_name = match_to_delete.first_name
    match_second_name = match_to_delete.second_name
    match_deletion_success = session.query(Match).filter(Match.id == match_id).delete()
    session.commit()

    if match_deletion_success:
        logger.debug(f"Match deleted #{match_id}, between '{match_first_name}' and '{match_second_name}'")
        # retuns the representation of the confirmation message
        return {"message": "Match deleted", "id": match_id, "player one": match_first_name, "player two": match_second_name}
    else:
        error_msg = "Match not found in database :/"
        logger.warning(f"Error while deleting Match #{match_id} between '{match_first_name}' and '{match_second_name}': {error_msg}")
        return {"message": error_msg}, 404


#  --------------------------------------------------------------------------------------
#  Auxiliary functions
#  --------------------------------------------------------------------------------------
