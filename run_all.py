import subprocess

print("Génération des données...")
subprocess.run(["python", "scripts/generate_data.py"])

print("Exécution du pipeline ETL...")
subprocess.run(["python", "scripts/etl_pipeline.py"])

print("Pipeline complet terminé ✅")
