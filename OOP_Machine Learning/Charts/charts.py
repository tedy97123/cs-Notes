import numpy as np 
import pandas as pd

import plotly.express as px 
import plotly.graph_objects as go 
import plotly.io as pio
pio.templates

import seaborn as sns
import matplotlib.pyplot as plt 
from sklearn.datasets import load_boston

from data import PreparedData
from scipy import stats
from scipy.stats import norm , skew # from some real stats work
  
from data
class Distplot(MachineLearning):
    sns.distplot(MachineLearning.PreparedData.data)
        
class S_K(PreparedData):
    def __init__(self,data):
        super().__init__(data)
        pass
    def Skewness(self):
        S = print("Skewness: %f" % self.PreparedData.data[self.PreparedData.y].skew())  #Skewness 
    def Kurtosis(self):
        K =  print("Kurtosis: %f" % self.PreparedData.data[self.PreparedData.y].kurt()) #Kurtosis
        

class subplots(PreparedData , xaxis_feature = '', fontsize = int):
    def __init__(self,data):
        super().__init__(data)
        pass
        self.y = self.PreparedData.y
        self.x = self.PreparedData.data[xaxis_feature]
        plt.ylabel( target ,fontsize)
        plt.xlabel(self.PreparedData.data.column[xaxis_feature])
        plt.show()


class BellCurve(PreparedData):
    def __init__(self,data):
        super().__init__(data)
        pass
    def b_curve(self):
        self.PreparedData.y = np.log1p(self.PreparedData.y)
        sns.displot(self.PreparedData.y)
        (mu , sigma) = norm.fit(self.PreparedData.y)
        print ('\n mu={:.2f} and sigma={:.2f}\n'.format(mu, sigma))
        plt.legend(['Normal dist. ($\mu=$ {:.2f} and $\sigma=$ {:.2f})'.format(mu,sigma)],
            loc='best')
        plt.ylabel('Frequency') # y-axis label
        plt.title('SalePrice distribution') # displot label
    

class ProbabilityPlot(PreparedData):
     def __init__(self,data):
        super().__init__(data)
        pass
     def QQ(self):
        fig= plt.figure() # is the actual graph body
        res = stats.probplot(self.PreparedData.y, plot= plt) # Probability plot  QQ graph that measure the relationship between two features in a dataset
        plt.show() # essential a print 

class Heatmap(PreparedData):
    def __init__(self,data):
        super().__init__(data)  
        pass
    def heatmap(self):
        plt.figure(figsize=(10,10))
        cor=self.PreparedData.data.corr()
        sns.heatmap(cor, annot=True, cmap=plt.cm.PuBu)
        plt.show()