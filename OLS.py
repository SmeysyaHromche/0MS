import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
#import matplotlib as mplt
#mplt.use('TkAgg')
from sympy.printing.pretty import pprint
class OLS():

    def __init__(self):
        '''
        Class constructor
        '''
        self.PATH_TO_DATASET = 'dataset/flats_moscow.csv'  # path to dataset
        self._dataset= pd.DataFrame()  # data frame of dataset
        self._solv = pd.DataFrame(columns=['Sum of real Y', 'Sum of predict Y', 'Regression residual'])

        self._x = np.array([])
        self._y = np.array([])

        self._y_predict = np.array([])
        self._b1 = 0  # slope factor
        self._b2 = 0  # free member 
        self._e = np.array([])  # regression residual

        self._sum_e = 0
        self._sum_of_y = 0
        self._sum_of_y_predict = 0


    def _StoringDataSet(self):
        '''
        
        Private method for storing dataset from csv to DataFrame and choosing only important data(price and area)

        '''

        path = Path(self.PATH_TO_DATASET)
        if not path.is_file():  # check is file with dataset exist
            raise Exception(f'Error! File with dataset on path {self.PATH_TO_DATASET} is not exist')
        
        self._dataset= pd.read_csv(self.PATH_TO_DATASET)  # store dataset to dataframe
        if self._dataset.empty:  # check is dataframe not empty
            raise Exception(f'Waring! Data set on path {self.PATH_TO_DATASET} is empty. Counting is aborted.')
        
        
    def _Sorting(self):
        sample = self._dataset.loc[:, ['price', 'totsp']].sample(n=50)  # search 'area' and 'cost'
        self._x = sample['totsp'].values
        self._y = sample['price'].values
        
    def _Vizualization(self):
        
        plt.scatter(self._x, self._y, marker='o', color='blue')
        plt.axis([self._x.min()-10, self._x.max()+10, self._y.min()-10, self._y.max()+10])  # xmin, xmax, ymin, ymax
        
        plt.plot(self._x, self._y_predict, color='red')
        plt.xlabel('area ( m^2)')
        plt.ylabel('cost (1000 $)')
        
        plt.gca().ticklabel_format(useOffset=False)
        plt.title('Area to cost')
        plt.show()


    def _Alg(self):
        x_mul_y_mean = np.mean(np.multiply(self._x, self._y))
        x_mean_mul_y_mean = np.mean(self._x)*np.mean(self._y)
        x_in_2_mean = np.mean(np.multiply(self._x, self._x))
        x_mean_in_2 = np.mean(self._x)**2
        
        self._b2 =  (x_mul_y_mean-x_mean_mul_y_mean)/(x_in_2_mean-x_mean_in_2)
        self._b1 = np.mean(self._y) - self._b2*np.mean(self._x)
        
        self._y_predict = self._b1 + self._b2*self._x

        self._e = self._y - self._y_predict  # positive (up), negative (down)

        self._e = np.sum(self._e)
        self._sum_of_y = np.sum(self._y)
        self._sum_of_y_predict = np.sum(self._y_predict)
        

    def OLS(self):
        '''
        
        Main method for counting OLS algorithms

        '''

        self._StoringDataSet()  # store data set

        # calc b2
        
        for i in range(30):
            self._Sorting()
            self._Alg()
            self._solv.loc[len(self._solv)] = {'Sum of real Y':self._sum_of_y, 'Sum of predict Y':self._sum_of_y_predict, 'Regression residual':self._e}
        
        print(self._solv)
        #self._Vizualization()
        

