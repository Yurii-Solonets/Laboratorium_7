import pandas as pd

file_path = "demografia.csv"
df = pd.read_csv(file_path,
                 decimal=',',
                 na_values=['N/A, NA', '-', ''])

print(df)