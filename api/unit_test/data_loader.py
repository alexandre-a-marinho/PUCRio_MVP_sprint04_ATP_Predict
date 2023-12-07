import pandas as pd

class DataLoader:

    def load_data(self, url: str, attributes: list):
        """ Loads data from .csv file as a pandas DataFrame.
        
        Arguments:
        url = url of the targer .csv file
        attributes = list of attributes names to be read from the .csv file
        """
        
        return pd.read_csv(url, names=attributes, skiprows=1, delimiter=',') # FIXME: check if these parameters are really necessary
    