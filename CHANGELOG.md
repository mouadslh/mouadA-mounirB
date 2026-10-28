# Journal des versions

## 0.6.0 - 2026-10-28

- Ajout du paquet installable `sentiment_app` et de la commande `sentiment`.
- Ajout des commandes `predict`, `serve`, `ui` et `--version`.
- Ajout de `SENTIMENT_MODELE` pour choisir le fichier du modèle.
- Déplacement du prédicteur dans le paquet; conservation de `src/predict.py` pour
  les scripts et imports des TP précédents.
- Ajout de la construction de roue et de son installation de contrôle dans la CI.
- Dépendance scikit-learn limitée à la version mineure 1.5 pour la compatibilité
  entre le modèle entraîné et le modèle chargé.

## 0.5.0 - TP5

- Interface Streamlit et client HTTP pour une prédiction ou un fichier d'avis.

## 0.4.0 - TP4

- Contrat d'entrée renforcé, abstention, jeu d'or et contrôles de qualité.

## 0.3.0 - TP3

- API FastAPI pour la santé du service et la prédiction.

## 0.2.0 - TP2

- Pipeline scikit-learn, entraînement, évaluation et prédiction.

## 0.1.0 - TP1

- Cadrage, environnement Python, structure du dépôt et intégration continue.
