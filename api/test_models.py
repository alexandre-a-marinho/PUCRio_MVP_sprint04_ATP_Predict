from unit_test import Evaluator, DataLoader
from model import Model

# To run: pytest -v test_models.py

# Instanciação das Classes
loader = DataLoader()
model = Model()
evaluator = Evaluator()

# Parâmetros    
url_data = "ml_model/archive/matches_golden.csv"
colunas = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

# Carga dos dados
dataset = loader.load_data(url_data, colunas)

# Separando em dados de entrada e saída
X = dataset.iloc[:, 0:-1]
Y = dataset.iloc[:, -1]
    
# Método para testar o model de Regressão Logística a partir do arquivo correspondente
# O nome do método a ser testado necessita começar com "test_"
def test_model_lr():  
    # Importando o model de regressão logística
    lr_path = 'ml_model/diabetes_lr.pkl'
    model_lr = model.carrega_model(lr_path)

    # Obtendo as métricas da Regressão Logística
    acuracia_lr, recall_lr, precisao_lr, f1_lr = evaluator.evaluate(model_lr, X, Y)
    
    # Testando as métricas da Regressão Logística 
    # Modifique as métricas de acordo com seus requisitos
    assert acuracia_lr >= 0.75 
    assert recall_lr >= 0.5 
    assert precisao_lr >= 0.5 
    assert f1_lr >= 0.5 
 
# Método para testar model KNN a partir do arquivo correspondente
def test_model_knn():
    # Importando model de KNN
    knn_path = 'ml_model/diabetes_knn.pkl'
    model_knn = model.carrega_model(knn_path)

    # Obtendo as métricas do KNN
    acuracia_knn, recall_knn, precisao_knn, f1_knn = evaluator.evaluate(model_knn, X, Y)
    
    # Testando as métricas do KNN
    # Modifique as métricas de acordo com seus requisitos
    assert acuracia_knn >= 0.75
    assert recall_knn >= 0.5 
    assert precisao_knn >= 0.5 
    assert f1_knn >= 0.5 
    

