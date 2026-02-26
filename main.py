import pandas as pd

df_clients = pd.read_csv('data/customers.csv')
df_trans = pd.read_csv('data/transactions.csv')

# print(df_clients.head())
#    customer_id / country / first_purchase / last_purchase  / total_spent /  avg_basket / recency_days / tenure_days
# print(df_trans.head())
#   invoice_id  / customer_id / product_code  / unit_price / invoice_date / country

# Etape 1 

#Nb customers
nb_customers= len(df_clients['customer_id'].unique()) 
# print(f'Number of customers: {nb_customers}')

nb_transactions = len(df_trans['invoice_id'])
# print(f'Number of transactions: {nb_transactions}')

min_date_transaction = df_trans['invoice_date'].min()
# print(f'Minimum date of transaction: {min_date_transaction}')
max_date_transaction = df_trans['invoice_date'].max()
# print(f'Maximum date of transaction: {max_date_transaction}')

# Quelles colonnes contiennent des valeurs manquantes, et dans quelle proportion ?
missing_values_clients = df_clients.isnull().sum()
missing_values_trans = df_trans.isnull().sum()
# print(f"Valeurs manquantes df_clients {missing_values_clients}")
# print(f"Valeurs manquantes df_trans {missing_values_trans}")

#proportion 
# print("\nProportion valeur manquante :\n")
proportion_missing_trans = missing_values_trans / len(df_trans) * 100
# print(proportion_missing_trans)

#Attendu type Client
# customer_id => ID
# country => string
# first_purchase => date
# last_purchase => date
# total_spent => float
# avg_basket => float
# recency_days => float
# tenure_days => float

# Réalité type
# print("\nTypes de données df_clients :\n")
# print(df_clients.dtypes)

# customer_id         int64
# country               str
# first_purchase        str
# last_purchase         str
# n_orders          float64
# total_spent       float64
# avg_basket        float64
# recency_days      float64
# tenure_days       float64

# Attendu type Transaction
# invoice_id => ID
# customer_id => ID
# product_code => string
# unit_price => float
# invoice_date => date
# country => string

# Réalité type
# print("\nTypes de données df_trans :\n")
# print(df_trans.dtypes)

# invoice_id          str
# customer_id     float64
# product_code        str
# product_name        str
# quantity        float64
# unit_price      float64
# invoice_date        str
# country             str

# doublons oui


#Data quality report 
report_clients = pd.DataFrame({
    'Column': df_clients.columns,
    'Missing Values': df_clients.isnull().sum().values,
    'Proportion Missing (%)': df_clients.isnull().mean().values * 100,
    'Data Type': df_clients.dtypes.values
})

print("\nData Quality Report for df_clients:\n")
print(report_clients)

# Même logique pour les transactions
report_trans = pd.DataFrame({
    'Column': df_trans.columns,
    'Missing Values': df_trans.isnull().sum().values,
    'Proportion Missing (%)': df_trans.isnull().mean().values * 100,
    'Data Type': df_trans.dtypes.values
})

print("\nData Quality Report for df_trans:\n")
print(report_trans)

# Graphique
import matplotlib.pyplot as plt
plt.ion()

plt.figure(figsize=(10, 6))
plt.bar(report_trans['Column'], report_trans['Proportion Missing (%)'], color='purple')
plt.ylabel('Proportion of Missing Values (%)')
plt.title('Proportion of Missing Values in df_trans')
plt.xticks(rotation=45)
# plt.show(block=False)

plt.savefig('data_quality_report.png')