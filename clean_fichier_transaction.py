import pandas as pd
import numpy as np


df = pd.read_csv(r"C:\HETIC\2025-2026\Data_Marketing\data_marketing_DIA3\transactions.csv")

print(f"Nombre de lignes avant nettoyage : {len(df)}\n")
print("Premières lignes :")
print(df.head(6))
print("\nStatistiques descriptives :")
print(df.describe(include='all'))
print("\nInfo du DataFrame :")
print(df.info())


df = df.drop_duplicates()
print(f"Nombre de lignes après suppression des doublons : {len(df)}")


valeurs_manquantes = df.isnull().sum()
print("Valeurs manquantes par colonne :")
print(valeurs_manquantes)



print("Statistiques après nettoyage: ")
print("Premières lignes :")
print(df.head(6))
print("\nStatistiques descriptives :")
print(df.describe(include='all'))
print("\nInfo du DataFrame :")
print(df.info())

valeurs_manquantes = df.isnull().sum()
print("\nValeurs manquantes par colonne après nettoyage :")
print(valeurs_manquantes)

df['from_store'] = np.where(df['customer_id'].notna(), 'no', 'yep')
print(df[['customer_id', 'from_store']].head(10))

df['retour_commande'] = ['oui' if (q < 0 or inv.startswith('C')) else 'non'
                         for q, inv in zip(df['quantity'], df['invoice_id'])]

print(df[['invoice_id', 'quantity', 'retour_commande']].head(10))

retours = df[df['retour_commande'] == 'oui']
print("LES COMMANDES EN RETOURS")
print(retours[['invoice_id', 'retour_commande', 'customer_id']].head(10))

print(f" apres nettoyage : {len(df)}")
output_path = r"C:\HETIC\2025-2026\Data_Marketing\data_marketing_DIA3\transaction_clean.csv"
df.to_csv(output_path, index=False)
print(f"\nDataset nettoyé sauvegardé dans : {output_path}")