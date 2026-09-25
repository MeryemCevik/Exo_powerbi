import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)
date_debut = datetime(2024, 1, 1)

# ACTIFS
actifs = [{
    'Actif_ID': f'ACT-{i:03d}',
    'Nom': f'Actif_{i}',
    'Type': random.choice(['Serveur','Poste','Application','BDD','Réseau']),
    'Environnement': random.choice(['Production','Test','Développement']),
    'Criticite': random.choice(['Basse','Moyenne','Haute','Critique'])
} for i in range(1, 61)]
pd.DataFrame(actifs).to_csv('actifs.csv', index=False)

# INCIDENTS
incidents = []
for i in range(1, 801):
    statut = random.choices(['Ouvert','En cours','Résolu','Fermé'], weights=[10,20,40,30])[0]
    incidents.append({
        'Incident_ID': f'INC-{i:04d}',
        'Date': date_debut + timedelta(days=random.randint(0,730)),
        'Type': random.choice(['Réseau','Applicatif','Sécurité','BDD','Matériel']),
        'Gravite': random.choices(['Basse','Moyenne','Haute','Critique'], weights=[30,40,20,10])[0],
        'Statut': statut,
        'Actif_ID': f'ACT-{random.randint(1,60):03d}',
        'Temps_Resolution_Heures': random.randint(1,72) if statut in ['Résolu','Fermé'] else 0
    })
pd.DataFrame(incidents).to_csv('incidents.csv', index=False)

# VULNERABILITES
vulns = []
for i in range(1, 301):
    cvss = round(random.uniform(1.0, 10.0), 1)
    vulns.append({
        'Vuln_ID': f'VUL-{i:04d}',
        'Date_Detection': date_debut + timedelta(days=random.randint(0,730)),
        'CVE': f'CVE-202{random.randint(3,5)}-{random.randint(1000,9999)}',
        'CVSS_Score': cvss,
        'Criticite': 'Critique' if cvss>=9 else 'Haute' if cvss>=7 else 'Moyenne' if cvss>=4 else 'Basse',
        'Statut': random.choices(['Ouverte','En cours','Corrigée'], weights=[30,30,40])[0],
        'Actif_ID': f'ACT-{random.randint(1,60):03d}'
    })
pd.DataFrame(vulns).to_csv('vulnerabilites.csv', index=False)

print("✅ 3 CSV générés")