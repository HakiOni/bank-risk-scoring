import pandas as pd
import sqlite3

clients = pd.read_csv("../data/clients.csv")
loans = pd.read_csv("../data/loans.csv")

df = pd.merge(clients, loans, on="client_id", how="left")

df["debt_ratio"] = df["amount"] / (df["income"] * 12)
df["debt_to_income"] = df["charges"] / df["income"]

conn = sqlite3.connect("../database/bank_data.db")
df.to_sql("clients_loans", conn, if_exists="replace", index=False)
conn.close()

print("ETL terminé ✅")
