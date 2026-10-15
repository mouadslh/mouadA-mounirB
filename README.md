# sentiment-app

Application d'analyse de sentiment pour la priorisation des avis clients négatifs.

## Équipe

- Med Mounir Elhamss
- Mouad Salah

## Description

Cette application permet à une équipe relation client de traiter en priorité les avis négatifs parmi des milliers d'avis reçus quotidiennement.

## Prérequis

- Python 3.11
- Windows avec PowerShell

## Installation

```powershell
# Créer l'environnement virtuel avec Python 3.11
py -3.11 -m venv .venv

# Activer l'environnement
.\.venv\Scripts\Activate.ps1

# Installer les dépendances
python -m pip install -r requirements.txt
```

## Utilisation

### Générer les données de démonstration

```powershell
python src\make_demo.py
```

### Entraîner le modèle

```powershell
# Sur les données de démonstration
python src\train.py

# Sur le dataset Allociné
python src\train.py --allocine
```

### Évaluer le modèle

```powershell
python src\evaluate.py
```

### Générer la matrice de confusion

```powershell
python src\plot_confusion.py
```

### Lancer l'interface Streamlit

```powershell
streamlit run ui\app.py
```

## Tests

```powershell
python -m pytest -q
```

## Structure du projet

```
sentiment-app/
├── data/               # Données (non versionnées)
├── models/             # Modèles entraînés
│   └── metrics.json    # Métriques (versionné)
├── src/                # Code source
├── ui/                 # Interface Streamlit
├── tests/              # Tests unitaires
├── docs/               # Documentation
│   ├── cadrage/        # Fiches de cadrage
│   └── images/         # Images et graphiques
├── scripts/            # Scripts utilitaires
└── notebooks/          # Notebooks (optionnel)
```

## Licence

Projet académique - Module "Développement et déploiement d'applications intelligentes"
