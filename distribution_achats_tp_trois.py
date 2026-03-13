import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BLUE = '#0058A3'
BLACK = '#1a1a1a'

sns.set_theme(style='whitegrid')

df = pd.read_csv(r"C:\HETIC\2025-2026\Data_Marketing\data_marketing_DIA3\transaction_clean.csv")
df['total_price'] = df['total_price'].fillna(0)

print("Valeurs uniques de retour_commande :", df['retour_commande'].unique())
valeurs = df['retour_commande'].dropna().unique()
val_no = [v for v in valeurs if str(v).lower() in ('no', 'non', 'false', '0', 'n')]
print("Valeur détectée pour 'pas de retour' :", val_no)

df_ventes = df[df['retour_commande'].isin(val_no) & (df['total_price'] > 0)]
print(f"Lignes après filtre : {len(df_ventes)} (total : {len(df)})")

limit = df_ventes['total_price'].quantile(0.95)
df_zoom = df_ventes[df_ventes['total_price'] <= limit]

plt.figure(figsize=(12, 6))
sns.histplot(df_zoom['total_price'], bins=40, color=BLUE)
plt.title('Distribution du montant des paniers (hors retours)', fontsize=16)
plt.xlabel('Montant du panier (€)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


freq = df.groupby('customer_id').size()

plt.figure(figsize=(12, 6))
sns.histplot(freq[freq <= 50], bins=30, color=BLACK)
plt.title("Fréquence d'achat par client (zoom ≤ 50 achats)", fontsize=16)
plt.xlabel("Nombre d'achats")
plt.ylabel("Nombre de clients")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ── 3. Courbe de Pareto ──────────────────────────────────────────────────────
ca_client = df_ventes.groupby('customer_id')['total_price'].sum().sort_values(ascending=False)
ca_cumul_pct = ca_client.cumsum() / ca_client.sum() * 100

plt.figure(figsize=(12, 6))
plt.plot(range(len(ca_cumul_pct)), ca_cumul_pct.values, color=BLUE, linewidth=2.5)
plt.axhline(80, color=BLACK, linestyle='--', linewidth=1.5, label='Seuil 80%')
plt.title("Courbe de Pareto – Contribution au CA", fontsize=16)
plt.xlabel("Clients (ordre décroissant de CA)")
plt.ylabel("CA cumulé (%)")
plt.ylim(0, 100)

n = len(ca_cumul_pct)
step = max(1, n // 10)
xticks = list(range(0, n, step))
plt.xticks(xticks, [str(v) for v in xticks], rotation=45)

plt.legend()
plt.tight_layout()
plt.show()