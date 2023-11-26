from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from flask_caching import Cache
from datetime import date

from sqlalchemy.exc import IntegrityError
from sqlalchemy import func

from model import Session, Payment, Model
from logger import logger
from schemas import *
from flask_cors import CORS


# Creating OpenAPI object
info = Info(title="Payments Control", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Defining tags
home_tag = Tag(name="Documentation", description="Documentation selection: Swagger, Redoc or RapiDoc")
payment_tag = Tag(name="Payment", description="Addition, visualization, edition and deletion of payments from the database")
analysis_tag = Tag(name="Analysis", description="Statistics and analysis regarding the payments in the database")

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


@app.post('/payment', tags=[payment_tag],
          responses={"200": PaymentViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_payment(form: PaymentSchema):
    """Adds a new Payment to the database.

    Returns the representation of the added Payment (as per PaymentViewSchema).
    """
    
    # Loading the prediction model
    ml_path = 'ml_model/atp_model.pkl'
    model = Model.loadModel(ml_path)
    form_encoded = Model.encodeMatchFormData(form)
    
    payment = Payment(
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
    
    logger.debug(f"Added Match between '{payment.first_name}' and '{payment.second_name}'.")
    try:
        # Creates database connection
        session = Session()

        # Adds new item to the database table and commits it
        session.add(payment)
        session.commit()
        logger.debug(f"Added Match between '{payment.first_name}' and '{payment.second_name}'.")
        return show_payment(payment), 200

    except IntegrityError as e:
        error_msg = "Integrity error on new Match addition :/"
        logger.warning(f"Error while adding Match #{payment.id} between '{payment.first_name}' and '{payment.second_name}': {error_msg}")
        return {"message": error_msg}, 409

    except Exception as e:
        # in case of a non-expected error
        error_msg = "It was not possible to save the new Match :/"
        logger.warning(f"Error while adding Match #{payment.id} between '{payment.first_name}' and '{payment.second_name}': {error_msg}")
        return {"message": error_msg}, 400


@app.put('/paymentedition', tags=[payment_tag],
          responses={"200": PaymentViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def edit_payment(query: PaymentSearchSchema, form: PaymentSchema,):
    """Edits an existing Payment in the database.

    Returns the representation of the edited Payment (as per PaymentViewSchema).
    """
    edited_match_id = query.id
    logger.debug(f"Editing Match #{edited_match_id} between '{form.first_name}' and '{form.second_name}'.")
    
    # Loading the prediction model
    ml_path = 'ml_model/atp_model.pkl'
    model = Model.loadModel(ml_path)
    form_encoded = Model.encodeMatchFormData(form)
    
    try:
        # Creates database connection
        session = Session()
        
        # Selects item to edit it in the database table and then commits it
        to_edit = session.query(Payment).filter(Payment.id == edited_match_id).first()
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
        to_edit.winner = Payment.getUncodedWinner(winner_code, form)

        session.commit()
        
        return show_payment(to_edit), 200

    except IntegrityError as e:
        error_msg = "Integrity error on new Match addition :/"
        logger.warning(f"Error while editing Match #{to_edit.id} between '{to_edit.first_name}' and '{to_edit.second_name}': {error_msg}")
        return {"message": error_msg}, 409

    except Exception as e:
        # in case of a non-expected error
        error_msg = "It was not possible to save the new Match :/"
        logger.warning(f"Error while editing Match #{to_edit.id} between '{to_edit.first_name}' and '{to_edit.second_name}': {error_msg}")
        return {"message": error_msg}, 400


@app.get('/payments', tags=[payment_tag],
         responses={"200": PaymentsListSchema, "404": ErrorSchema})
def get_payments():
    """Searches for all registered Payments.

    Returns the representation of a list of all registred Payments (if any exists).
    """
    logger.debug(f"Getting Payments")
    
    # Creates database connectio to perform the search
    session = Session()
    payments = session.query(Payment).all()

    if payments:
        logger.debug(f"%d Payments found" % len(payments))
        print(payments)
        # retuns the representation of the list of all payments found
        return show_payments(payments), 200
    else:
        # retorno empty if nothing is found
        return {"payments": []}, 200


@app.get('/payment', tags=[payment_tag],
         responses={"200": PaymentViewSchema, "404": ErrorSchema})
def get_payment(query: PaymentSearchSchema):
    """Searches a Payment based on it's Id.

    Returns the representation of a Payment (if found).
    """
    payment_id = query.id
    logger.debug(f"Getting Payment data #{payment_id}")

    # Creates database connectio to perform the search
    session = Session()

    # Searchs using payment Id
    payment = session.query(Payment).filter(Payment.id == payment_id).first()

    if payment:
        logger.debug(f"Payment found: #{payment_id}")
        return show_payment(payment), 200
    else:
        error_msg = "Payment not found in database :/"
        logger.warning(f"Error while searching for Match #{payment.id} between '{payment.first_name}' and '{payment.second_name}': {error_msg}")
        return {"message": error_msg}, 404


@app.delete('/payment', tags=[payment_tag],
            responses={"200": PaymentDelSchema, "404": ErrorSchema})
def del_payment(query: PaymentSearchSchema):
    """Deletes a Payment based on it's Id.

    Returns a message confirming target Payment deletion.
    """
    payment_id = query.id
    logger.debug(f"Deleting Payment #{payment_id}")

    # Creates database connection to perform the search
    session = Session()
    
    # Searching and deleting target Payment
    payment_to_delete: Payment = session.query(Payment).filter(Payment.id == payment_id).first()
    payment_first_name = payment_to_delete.first_name
    payment_second_name = payment_to_delete.second_name
    payment_deletion_success = session.query(Payment).filter(Payment.id == payment_id).delete()
    session.commit()

    if payment_deletion_success:
        logger.debug(f"Match deleted #{payment_id}, between '{payment_first_name}' and '{payment_second_name}'")
        # retuns the representation of the confirmation message
        return {"message": "Match deleted", "id": payment_id, "player one": payment_first_name, "player two": payment_second_name}
    else:
        error_msg = "Match not found in database :/"
        logger.warning(f"Error while deleting Match #{payment_id} between '{payment_first_name}' and '{payment_second_name}': {error_msg}")
        return {"message": error_msg}, 404


#  --------------------------------------------------------------------------------------
#  Auxiliary functions
#  --------------------------------------------------------------------------------------
