import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.title("📈 Bank Risk Scoring Dashboard")

conn = sqlite3.connect("../database/bank_data.db")
df = pd.read_sql_query("SELECT * FROM clients_loans", conn)
conn.close()

st.subheader("📂 Données clients et ratios")
st.dataframe(df)

st.subheader("📊 Distribution du Debt Ratio")
fig = px.histogram(df, x="debt_ratio", nbins=30, title="Répartition du Debt Ratio")
st.plotly_chart(fig)

threshold = st.slider("Seuil de Debt Ratio", 0.0, 1.0, 0.3)
filtered = df[df["debt_ratio"] > threshold]
st.write(f"Clients avec Debt Ratio > {threshold}:")
st.dataframe(filtered)
