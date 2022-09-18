import numpy as np 
import pandas as pd
 

import plotly.express as px 
import plotly.graph_objects as go 
import plotly.io as pio
pio.templates

import seaborn as sns
import matplotlib.pyplot as plt 
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.datasets import load_wine

class MachineLearning():
    def __init__(self, data : pd.DataFrame or str):
        self.train_raw_data = None
        self.test_raw_data = None
        if isinstance(data, str): #URL
            self.raw_data = pd.read_csv(data)
        elif isinstance(data, pd.DataFrame):
            self.raw_data = data

class PreparedData(MachineLearning): 
     def __init__(self,data):
        super().__init__(data = data)
        pass    

        p_data = load_wine()

        print ("----------------------------------------- Its here \n" , type(p_data))

        self.target = 'alcohol'

        X = p_data.data

        self.p_df = pd.DataFrame(X , columns = p_data.feature_names)

        self.y = p_data.target

        self.p_df.head()

        print ("this is the dataset " ,  self.p_df)

class Linear(PreparedData):
    def __init__(self, data) :
        super().__init__(data = data)
        pass

        self.PreparedData = PreparedData(self)

        target= 'alcohol'

        self.X =self.PreparedData.p_df.drop(target, axis = 1)

        self.y= self.PreparedData.p_df[target]

        self.X_train,self.X_test,self.y_train,self.y_test = train_test_split(self.X,self.y,test_size=0.2, random_state=42)

        print ("this is the x trainning prep" , self.X , self.y)

        print("this is x train data" ,self.X_train.shape)

        print("this is x test data" ,self.X_test.shape) 

        print("this is y train data" ,self.y_train.shape)
        
        print("this is y test data" ,self.y_test.shape)
    
        lr = LinearRegression()

        lr.fit(self.X_train, self.y_train)

        predictions =lr.predict(self.X_test)

        print("Actual value Alchool:- ", self.y_test[:1])

        print("Model Predicted Value:- ", predictions[:1])

        mse = mean_squared_error(self.y_test, predictions )

        rmse = np.sqrt(mse)

        print("Accuracy of the model:-" , rmse) # print the accuracy of the model

class DataUtilities(PreparedData): 

    def __init__(self, p_data):
        super.__init__(p_data)
        pass
        return
        d_desc = PreparedData.p_data.describe()
        j_column_names =  PreparedData.p_data.isnull().sum()

class every_chart(PreparedData , height:= int ,):

    def __init__(self, p_data):
        super.__init__(p_data)
        pass
        return
        p_plt = sns.pairplot(PreparedData.p_data , height )
        plt.tight_layout(p_plt)
                