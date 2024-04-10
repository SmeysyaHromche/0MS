import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib as mplt
#mplt.use('TkAgg')
import tkinter as tk
import sympy as sp
from sympy.printing.pretty import pprint
class OLS():

    def __init__(self):
        '''
        Class constructor
        '''
        self.PATH_TO_DATASET = 'dataset/Housing.csv'  # path to dataset
        self._df = pd.DataFrame()  # data frame of dataset
        self._outputDf = pd.DataFrame()  # dataFrame with calc data
        
        self._x, self._y = sp.symbols('x y')
        self._x_assume = self._x.conjugate()
        self._y_assume = self._y.conjugate()


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


    def _Vizualization(self):
        #print(self._df['price'])
        
        price = self._df['price']
        area = self._df['area']
        print(self._df['area'].min(), self._df['area'].max(), self._df['price'].min(), self._df['price'].max())
        plt.scatter(area, price, marker='o', color='orange')
        plt.axis([self._df['area'].min()-1000, self._df['area'].max()+1000, self._df['price'].min()-100000, self._df['price'].max()+100000])  # xmin, xmax, ymin, ymax
        plt.xlabel('area(m^2)')
        plt.ylabel('cost($)')
        plt.locator_params(axis='y', nbins=5)
        plt.gca().ticklabel_format(useOffset=False)
        plt.title('Relathionship between area and finally cost for flat')
        plt.show()

    def _Func(self):
        pprint(self._x_assume)

    def OLS(self):
        '''
        
        Main method for counting OLS algorithms

        '''

        self._StoringDataSet()  # store data set
        self._Func()
        self._Vizualization()

