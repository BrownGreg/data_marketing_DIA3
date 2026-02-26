import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\HETIC\2025-2026\Data_Marketing\data_marketing_DIA3\touchpoints.csv")

print(f"Nombre de lignes avant nettoyage : {len(df)}\n")

print("Premières lignes :")
print(df.head(6))

print("Statistiques descriptives :")
print(df.describe(include='all'))

print("\nInfo du DataFrame :")
print(df.info())

df = df.drop_duplicates()
print(f"Nombre de lignes après suppression des doublons : {len(df)}")


valeurs_manquantes = df.isnull().sum()
print("\nValeurs manquantes par colonne :")
print(valeurs_manquantes)


lignes_vides = df.isnull().all(axis=1).sum()
print(f"\nNombre de lignes complètement vides : {lignes_vides}")

df = df.dropna(how='all')

print(f"Nombre de lignes après suppression des lignes vides : {len(df)}")


print("\n----- Statistiques après nettoyage -----")
print("Premières lignes :")
print(df.head(6))

print("\nStatistiques descriptives :")
print(df.describe(include='all'))

print("\nInfo du DataFrame :")
print(df.info())

valeurs_manquantes = df.isnull().sum()
print("\nValeurs manquantes par colonne après nettoyage :")
print(valeurs_manquantes)

print(f"\nNombre de lignes final après tout le nettoyage : {len(df)}")

output_path = r"C:\HETIC\2025-2026\Data_Marketing\data_marketing_DIA3\touchpoints_clean.csv"
df.to_csv(output_path, index=False)

print(f"\nDataset nettoyé sauvegardé dans : {output_path}")