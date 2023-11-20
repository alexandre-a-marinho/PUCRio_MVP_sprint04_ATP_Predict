import numpy as np
import pickle
import joblib

class Model:
    
    def loadModel(path):
        """Dependendo se o final for .pkl ou .joblib, carregamos de uma forma ou de outra
        """
        
        if path.endswith('.pkl'):
            model = pickle.load(open(path, 'rb'))
        elif path.endswith('.joblib'):
            model = joblib.load(path)
        else:
            raise Exception('Formato de arquivo não suportado')
        return model
    
    def predictor(model, form):
        """Realiza a predição de um paciente com base no modelo treinado
        """
        X_input = np.array([
            form.surface, 
            form.year, 
            form.tourney_level, 
            form.best_of_x_sets, 
            form.tourney_round, 
            #form.first_name, 
            form.first_hand, 
            form.first_id,
            form.first_rank,
            form.first_rank_points,
            form.first_age,
            form.first_height,
            #form.second_name, 
            form.second_hand, 
            form.second_id,
            form.second_rank,
            form.second_rank_points,
            form.second_age,
            form.second_height])

        # FIXME:encode input before prediction

        # Faremos o reshape para que o modelo entenda que estamos passando
        winner = model.predict(X_input.reshape(1, -1))
        return int(winner[0])