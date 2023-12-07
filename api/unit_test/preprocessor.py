from sklearn.model_selection import train_test_split

class PreProcessor:

    def pre_process(self, dataset, test_split_ratio, seed=7):
        """ Handles dataset pre-processing. """
        # For future implementation
        # - data cleaning and outlier elimination
        # - feature selection
        # - normalization/standardization
        # - trains/test holdout definition
        X_train, X_test, Y_train, Y_test = self.__prepare_holdout(dataset,
                                                                  test_split_ratio,
                                                                  seed)
        
        return (X_train, X_test, Y_train, Y_test)
    
    def __prepare_holdout(self, dataset, test_split_ratio, seed):
        """ Divides full dataset into train/test groups.
        Assumes that the target ouput variable is in the last column of the dataset.
        O parâmetro test_size é o percentual de dados de teste.
        
        Arguments:
        dataset = dataset
        test_split_ratio = % of test data
        seed = seed for random operations
        """
        data = dataset.values
        X = data[:, 0:-1]
        Y = data[:, -1]
        return train_test_split(X, Y, test_size=test_split_ratio, random_state=seed)
