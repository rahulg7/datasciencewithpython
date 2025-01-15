import pandas as pd

data1 = pd.read_csv("tips.csv", header=0, sep=",") #header = 0 means takes column name from row =0 i.e first row, sep = , because we are using csv file
# print(data1)
print(data1.head()) #show top 5 rows only 