import pandas as pd

d = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}

df = pd.DataFrame(data=d)

print(df)

count_col = df.shape[0] # count number or rows and coloums [0] for row and [1] for column
print(count_col)