import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
import pickle
dataset=pd.read_csv("diabetes.csv")
pd.set_option("display.max_columns",10)
#print("Rows in dataset = {}\nFeatures in dataset = {}".format(dataset.shape[0],dataset.shape[1]))
#print(dataset.head())
#print(dataset.info())
#print(dataset.isnull().sum())
#print(dataset.describe())

