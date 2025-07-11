import streamlit as st
import pandas as pd
import random

st.title("📈 Bank Risk Scoring Dashboard")

# 🔹 Génération auto des données
def generate_clients(n=100):
    clients = []
    for i in range(n):
        client_id = i + 1
        age = random.randint(18, 70)
        income = random.randint(1000, 5000)
        charges = random.randint(200, 2000)
        clients.append([client_id, age, income, charges])
    return pd.DataFrame(clients, columns=["client_id", "age", "income", "charges"])

def generate_loans(n=100):
    loans = []
    for i in range(n):
        client_id = random.randint(1, 100)
        amount = random.randint(1000, 20000)
        duration_months = random.choice([12, 24, 36, 48, 60])
        loans.append([client_id, amount, duration_months])
    return pd.DataFrame(loans, columns=["client_id", "amount", "duration_months"])

df_clients = generate_clients()
df_loans = generate_loans()

# 🔹 Pipeline direct
df = pd.merge(df_clients, df_loans, on="client_id", how="left")
df["debt_ratio"] = df["amount"] / (df["income"] * 12)
df["debt_to_income"] = df["charges"] / df["income"]

# 🔹 Dashboard
st.subheader("📂 Données clients et ratios")
st.dataframe(df)

st.subheader("📊 Distribution du Debt Ratio")
import plotly.express as px
fig = px.histogram(df, x="debt_ratio", nbins=30, title="Répartition du Debt Ratio")
st.plotly_chart(fig)

threshold = st.slider("Seuil de Debt Ratio", 0.0, 1.0, 0.3)
filtered = df[df["debt_ratio"] > threshold]
st.write(f"Clients avec Debt Ratio > {threshold}:")
st.dataframe(filtered)
