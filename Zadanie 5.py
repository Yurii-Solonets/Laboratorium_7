from codecs import ignore_errors
from traceback import print_tb

import pandas as pd
from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray

dane = {
    "Numer albumu": [1, 2, 3, 4, 5],
    "Imię": ["Anna", "Jan", "Katarzyna", "Tomasz", "Michał"],
    "Nazwisko": ["Kowalska","Nowak", "Wiśniewska", "Kaczmarek", "Zieliński"],
    "Ocena": [4.5, 3.0, 5.0, 4.0, 2.5],
    "Wiek": [22, 21, 24, 23, 25]
}

students_df = pd.DataFrame(dane)

#Zadanie A
students_dobra_ocena = students_df[students_df["Ocena"] > 4]
print("\nStudenci z oceną większą niż 4:")
print(students_dobra_ocena)

#Zadanie B
students_sorted = students_df.sort_values(by = "Wiek")
print("\nStudenci posortowani według wieku:")
print(students_sorted)

#Zadanie C
grouped_by_wiek = students_df.groupby("Ocena")["Wiek"].mean()
print("\nŚrednia wieku w grupach ocen:")
print(grouped_by_wiek)

#Zadanie D
improvement_data = {
    "Numer albumu": [1, 2, 3, 4, 5],
    "Ocena_poprawna": [5.0, 3.5, 5.0, 4.5, 3.0]
}
improvement_df = pd.DataFrame(improvement_data)
merged_df = pd.merge(students_df, improvement_df, on = "Numer albumu")
print("\nPołączone dane z poprawy:")
print(merged_df)

#Zadanie E
output_file = "students_data.csv"
merged_df.to_csv(output_file, index = False)
print(f"\nDane zapisano do pliku: {output_file}")

#Zadanie F
wczytane_df = pd.read_csv(output_file)
print("\nWczytane dane:")
print(wczytane_df)

#Zadanie G
dodany_student = {'Numer albumu': 6, "Imię": "Ewa", "Nazwisko": "Kamińska", "Ocena": 4.0, "Wiek": 22, "Ocena_poprawna": 4.5}
merged_df = merged_df._append(dodany_student, ignore_index = True)
print("\nDataFrame po dodaniu nowego studenta:")
print(merged_df)

#Zadanie H
unikalny_oceny = merged_df["Ocena"].unique()
print("\nUnikalne wartości w kolumnie Ocena:")
print(unikalny_oceny)

#Zadanie I
students_z_5 = merged_df[merged_df["Ocena"] == 5.0].shape[0]
print(f"\nLiczba studentów z oceną równą 5: {students_z_5}")




