import numpy as np
import pandas as pd
from pathlib import Path
class OLS():

    def __init__(self):
        self.PATH_TO_DATASET = 'dataset/Housing.csv'
        self._test = 1
        self._df = pd.DataFrame()

    def _StoringDataSet(self):
        '''
        
        Private method for storing dataset from csv to DataFrame and choosing only important data(price and area)

        '''

        path = Path(self.PATH_TO_DATASET)
        if not path.is_file():  # check is file with dataset exist
            raise Exception(f'Error! File with dataset on path {self.PATH_TO_DATASET} is not exist')
        
        self._df = pd.read_csv('dataset/Housing.csv')  # store dataset to dataframe
        self._df = self._df.loc[:, ['price', 'area']]  # search 'area' and 'cost'

        if self._df.empty:  # check is dataframe not empty
            raise Exception(f'Waring! Data set on path {self.PATH_TO_DATASET} is empty. Counting is aborted.')
    
    def OLS(self):
        '''
        
        Main method for counting OLS algorithms

        '''

        self._StoringDataSet()  # store data set
        print(self._df)
