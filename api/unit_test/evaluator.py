from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

class Evaluator:

    def evaluate(self, model, X_test, Y_test):
        """ Performs a prediction and evaluates the model performance.
        
        Arguments:
        model = model object
        X_test = test input data
        Y_test = test output data
        """
        predictions = model.predict(X_test)
        return (accuracy_score(Y_test, predictions),
                recall_score(Y_test, predictions),
                precision_score(Y_test, predictions),
                f1_score(Y_test, predictions))
    
