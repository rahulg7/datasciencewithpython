import pandas as pd

health_data = pd.read_csv("data1.csv",header=0,sep=",")

health_data.dropna(axis=0,inplace=True) #axis=0 means that we want to remove all rows that have a NaN value:

print(health_data)