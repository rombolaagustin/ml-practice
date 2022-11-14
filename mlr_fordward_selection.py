# Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn as sk

# Control Variables
folder = 'linear_regression_files'
file_multiple = 'CarPrice_Assignment.csv'
threhold_pvalue = 0.05

# Read Data 
df_multiple = pd.read_csv(f"{folder}/{file_multiple}")
df_multiple = pd.get_dummies(df_multiple, drop_first=True) #Generate dummies variables
Xm = df_multiple.copy()
Ym = Xm['price']
Xm = Xm.drop('price', axis=1)

cant_features = Xm.shape[1]

# Main

print('Se procesa')

