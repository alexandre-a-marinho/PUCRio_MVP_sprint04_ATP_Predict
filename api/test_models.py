from unit_test import Evaluator, DataLoader
from model import Model

# To run: pytest -v test_models.py

# Instantiations
loader = DataLoader()
model = Model()
evaluator = Evaluator()

# Dataset parameters    
url_data = "ml_model/archive/matches_golden.csv"
attributes = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

# Load data
dataset = loader.load_data(url_data, attributes)

# Data separation into input/output arrays
X = dataset.iloc[:, 0:-1]
Y = dataset.iloc[:, -1]
    

# Method to test the SVM model based on a given model file
# obs: The name of the method to be tested must begin with "test_"
def test_model_svm():  
    # Importing the model
    svm_model_obj_path = 'ml_model/atp_model_svm.pkl'
    model_svm = model.load_external_python_object(svm_model_obj_path)

    # Obtaining SVM metrics
    accuracy_svm, recall_svm, precisao_svm, f1_svm = evaluator.evaluate(model_svm, X, Y)
    
    # Testing SVM metrics
    assert accuracy_svm >= 0.75 
    assert recall_svm >= 0.5 
    assert precisao_svm >= 0.5 
    assert f1_svm >= 0.5 
 
# Method to test the RFC model based on a given model file
def test_model_rfc():
    # Importing the model
    rfc_model_obj_path = 'ml_model/atp_model_rfc.pkl'
    model_rfc = model.load_external_python_object(rfc_model_obj_path)

    # Obtaining RFC metrics
    accuracy_rfc, recall_rfc, precisao_rfc, f1_rfc = evaluator.evaluate(model_rfc, X, Y)
    
    # Testing RFC metrics
    assert accuracy_rfc >= 0.75
    assert recall_rfc >= 0.5 
    assert precisao_rfc >= 0.5 
    assert f1_rfc >= 0.5 
    

