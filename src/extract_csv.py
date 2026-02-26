import pandas as pd

df = pd.read_csv("../data/customers.csv", nrows=1000)
df.to_csv("customers_sample.csv", index=False)