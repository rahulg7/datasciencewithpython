import pandas as pd

health_data = pd.read_csv("data1.csv",header=0,sep=",")

print(health_data.info())

# astype(float) converts object to float datatype

health_data["Average_Pulse"] = health_data["Average_Pulse"].astype(float)
health_data["Max_Pulse"] = health_data["Max_Pulse"].astype(float)
health_data["Hours_sleep"] = health_data["Hours_sleep"].astype(float)

print(health_data.info())
