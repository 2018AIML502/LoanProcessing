#!/usr/bin/env python
# coding: utf-8

# In[79]:


# pip install plotnine

import pandas as pd
import seaborn as sns
#import statsmodels.formula.api as smf

import matplotlib.pyplot as plt
#from plotnine import *

from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
import numpy as np
import sys, os, gc, traceback
from sklearn.preprocessing import LabelEncoder
#import missingno as msno
#from impyute.imputation.cs import mice
from scipy import stats


class ErrorHandler(object):
    def handleErr(self, err):
        tb = sys.exc_info()[-1]
        stk = traceback.extract_tb(tb, 1)
        functionName = stk[0][2]
        return functionName + ":" + err
    
class ReadData():
    def __init__(self, parent=None):
        try:
            
            self.errObj = ErrorHandler()

        except Exception as exp:
            err = self.errObj.handleErr(str(exp))
            print(str(err))
    def getData():
        dataFolder='Dataset'
        dataFilePath=os.path.join(dataFolder,'LoanApplyData-bank.csv')
        loanData=pd.read_csv(dataFilePath)
        #print(loanData.head())            
        return loanData
        


class PreProcessor():
    def __init__(self, parent=None):
        try:
            self.errObj = ErrorHandler()

        except Exception as exp:
            err = self.errObj.handleErr(str(exp))
            print(str(err))
    def get_categorical_columns(data):
        numeric_columns=data._get_numeric_data().columns
        allColumns=data.columns
        cat_columns=list(set(allColumns)-set(numeric_columns))
        return cat_columns
    def encode_categorical_variables(data):
        le=LabelEncoder()
        cat_cols=PreProcessor.get_categorical_columns(data)
        for col in cat_cols:
            data[col]=le.fit_transform(data[col])
        return data
        
    def show_stats(data):
        data['target'].value_counts().plot.bar()
        print('Size of the data: ', data.shape)
        
        


class visualizeCorrelation():
    def __init__(self, parent=None):
        try:
            self.errObj = ErrorHandler()

        except Exception as exp:
            err = self.errObj.handleErr(str(exp))
            print(str(err))

class MissingValue:
    def __init__(self, parent=None):
        try:
            self.errObj = ErrorHandler()
        except Exception as exp:
            err = self.errObj.handleErr(str(exp))
            print(str(err))
    def find_missing_value(data):
        print('Missing value per column', data.isnull().sum())


class Outlier:
    def __init__(self, parent=None):
        try:
            self.errObj = ErrorHandler()
        except Exception as exp:
            err = self.errObj.handleErr(str(exp))
            print(str(err))

def main():


    if __name__ == '__main__':
        main()


# In[81]:


data=ReadData.getData()
PreProcessor.encode_categorical_variables(data)
PreProcessor.show_stats(data)
MissingValue.find_missing_value(data)


# In[ ]:




