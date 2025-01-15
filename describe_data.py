import pandas as pd

health_data = pd.read_csv("data1.csv",header=0,sep=",")

print(health_data.describe())