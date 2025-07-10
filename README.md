# 📈 Bank Risk Scoring Pipeline

Ce projet est un pipeline d'agrégation de données bancaires pour calculer des ratios de risque et un scoring de crédit simplifié.

## 📂 Structure

- `data/` — Données simulées
- `scripts/` — Génération de données, pipeline ETL
- `dashboard/` — Application Streamlit
- `database/` — Base SQLite

## ⚙️ Pour exécuter

1️⃣ Génère les données :
```
python scripts/generate_data.py
```

2️⃣ Lance le pipeline ETL :
```
python scripts/etl_pipeline.py
```

3️⃣ Ou exécute tout d’un coup :
```
python run_all.py
```

4️⃣ Lance le dashboard :
```
streamlit run dashboard/app.py
```

## ✅ Objectif

- Générer des données bancaires simulées
- Calculer des indicateurs financiers
- Stocker les résultats
- Visualiser via un dashboard Streamlit
