from unit_test import Evaluator, DataLoader
from model import Model

# To run:
# cd to /api directory
# pytest -v test_models.py

# Instantiations
loader = DataLoader()
model = Model()
evaluator = Evaluator()

# Dataset parameters    
filepath_data = "ml_model/archive/matches_golden.csv"
attributes = ["surface",
              "tourney_level",
              "second_id",
              "second_hand",
              "second_ht",
              "second_age",
              "first_id",
              "first_hand",
              "first_ht",
              "first_age",
              "best_of",
              "round",
              "second_rank",
              "second_rank_points",
              "first_rank",
              "first_rank_points",
              "tourney_year",
              "label"]

# Load data
dataset = loader.load_data(filepath_data, attributes)

# Data separation into input/output arrays
X_data = dataset.iloc[:, 0:-1]
Y_data = dataset.iloc[:, -1]

# Scale input according to training dataset
has_scaling = True
if has_scaling:
    scaler_path = 'ml_model/atp_scaler.pkl'
    scaler = Model.load_external_python_object(scaler_path)
    X_data = scaler.transform(X_data)

# Test methods (obs: name of the method to be tested must begin with "test_")
# Method to test any general model based on a given model file
def test_model():
    # Importing the model
    model_obj_path = 'ml_model/atp_model.pkl'
    model_test = model.load_external_python_object(model_obj_path)

    # Obtaining metrics
    accuracy, recall, precisao, f1 = evaluator.evaluate(model_test, X_data, Y_data)

    # Testing metrics
    assert accuracy >= 0.65
    assert recall >= 0.5
    assert precisao >= 0.5
    assert f1 >= 0.5
