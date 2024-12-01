import pandas as pd

dane = {
    "Numer ID": [1, 2, 3, 4, 5],
    "Imię": ["Anna", "Jan", "Katarzyna", "Tomasz", "Michał"],
    "Nazwisko": ["Kowalska", "Nowak", "Wiśniewska", "Kaczmarek", "Zieliński"],
    "Stanowisko": ["Manager", "Programista", "Konsultant", "Programista", "Manager"],
    "Wiek": [35, 28, 40, 30, 45],
    "Pensja": [8000, 4500, 6000, 5500, 7000]
}

df_pracownicy = pd.DataFrame(dane)

#Element 1
wysoka_pensja = df_pracownicy[df_pracownicy["Pensja"] > 5000]
print("Pracownicy z pensją > 5000 PLN:\n", wysoka_pensja)

#Element 2
sortowani_wiek = df_pracownicy.sort_values(by = "Wiek")
print("\nPracownicy posortowani według wieku:\n", sortowani_wiek)

#Element3
średnia_pensja = df_pracownicy.groupby("Stanowisko")["Pensja"].mean()
print("\nŚrednia pensja w każdej grupie stanowisk:\n", średnia_pensja)

#Element 4
dane_awans = {
    "Numer ID": [2, 4],
    "Nowe Stanowisko": ["Senior Programista", "Manager"]
}
df_awans = pd.DataFrame(dane_awans)

#Element 5
df_połączone = pd.merge(df_pracownicy, df_awans, on = "Numer ID", how = "left")
print("\nPołączona ramka danych z awansami:\n", df_połączone)

plik_csv = "pracownicy.csv"
df_połączone.to_csv(plik_csv, index = False)
print(f"\nDane zostały zapisane do pliku: {plik_csv}")

df_wczytane = pd.read_csv(plik_csv)
print("\nWczytane dane z pliku:\n", df_wczytane)