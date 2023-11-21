import numpy as np
import pickle
import joblib

from sklearn.preprocessing import LabelEncoder

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
        X_input = np.array([  #FIXME: verify order of data in model, must be the same here
            form["surface"], 
            form["year"], 
            form["tourney_level"], 
            form["best_of_x_sets"], 
            form["tourney_round"], 
            form["first_hand"], 
            form["first_id"],
            form["first_rank"],
            form["first_rank_points"],
            form["first_age"],
            form["first_height"],
            form["second_hand"], 
            form["second_id"],
            form["second_rank"],
            form["second_rank_points"],
            form["second_age"],
            form["second_height"]])

        # Faremos o reshape para que o modelo entenda que estamos passando
        winner = model.predict(X_input.reshape(1, -1))
        return int(winner[0])
    
    @staticmethod
    def encodeMatchFormData (form):
        form_encoded = {
            "surface" : form.surface,
            "year" : form.year,
            "tourney_level" : form.tourney_level,
            "best_of_x_sets" : form.best_of_x_sets,
            "tourney_round" : form.tourney_round,
            "first_hand" : form.first_hand,
            "first_id" : form.first_id,
            "first_rank" : form.first_rank,
            "first_rank_points" : form.first_rank_points,
            "first_age" : form.first_age,
            "first_height" : form.first_height,
            "second_hand" : form.second_hand,
            "second_id" : form.second_id,
            "second_rank" : form.second_rank,
            "second_rank_points" : form.second_rank_points,
            "second_age" : form.second_age,
            "second_height" : form.second_height
        }
        
        hands = ["L", "R"]
        hand_encoder = LabelEncoder()
        hand_encoder.fit(hands)
        form_encoded["first_hand"] = hand_encoder.transform([form.first_hand])[0]
        form_encoded["second_hand"] = hand_encoder.transform([form.second_hand])[0]
        
        surfaces = ["Carpet", "Clay", "Grass", "Hard"]
        surface_encoder = LabelEncoder()
        surface_encoder.fit(surfaces)
        form_encoded["surface"] = surface_encoder.transform([form.surface])[0]
        
        tourney_levels = ["A", "D", "F", "G", "M"]
        tourney_level_encoder = LabelEncoder()
        tourney_level_encoder.fit(tourney_levels)
        form_encoded["tourney_level"] = tourney_level_encoder.transform([form.tourney_level])[0]

        tourney_rounds = ["BR", "ER", "F", "QF", "R128", "R16", "R32", "R64", "RR", "SF"]
        tourney_round_encoder = LabelEncoder()
        tourney_round_encoder.fit(tourney_rounds)
        form_encoded["tourney_round"] = tourney_round_encoder.transform([form.tourney_round])[0]
        
        print(form_encoded)
        
        return form_encoded