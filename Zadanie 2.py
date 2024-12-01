import pandas as pd

file_path = "demografia.csv"
df = pd.read_csv(
    file_path,
    decimal=',',
    na_values=['NA', 'n/a', 'NaN']
)

indeks_max = df['2022'].idxmax(skipna = True)

kraj = df.loc[indeks_max, 'KRAJE']

print(f"Największy przyrost ludności w 2022 roku odnotowano w kraju: {kraj}.")