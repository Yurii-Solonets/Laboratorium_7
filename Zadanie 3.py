import pandas as pd

file_path = "demografia.csv"
df = pd.read_csv(
    file_path,
    decimal=',',
    na_values=['NA', 'n/a', 'NaN'],
    sep = ','
)

dane_przyrost = df.drop(columns=["KRAJE"], errors = 'ignore')
kolumna_max = dane_przyrost.max().idxmax()
indeks_max = dane_przyrost[kolumna_max].idxmax()

kraj = df.loc[indeks_max, "KRAJE"]
wartość = dane_przyrost.loc[indeks_max, kolumna_max]

print(f"Największy przyrost ludności odnotowano w kraju: {kraj}")
print(f"Rok: {kolumna_max}, wartość przyrostu: {wartość}")