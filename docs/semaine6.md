# Semaine 6 : packager l'application

## 1. Pourquoi déplacer `predict()` dans `sentiment_app` ?

Le prédicteur devient importable comme un module normal après installation de la roue.
L'API utilise `sentiment_app.predict` directement, sans modifier `sys.path`. Le fichier
`src/predict.py` est conservé comme adaptateur afin que les scripts et tests des TP
précédents continuent d'utiliser le même module et le même cache du modèle.

## 2. Que contient la roue et comment fonctionne-t-elle sans le dépôt ?

La roue installe les paquets `sentiment_app`, `api` et `ui`, avec la commande
`sentiment`. Elle déclare les dépendances Python nécessaires; Streamlit, pandas et
httpx sont regroupés dans l'extra `ui`. Les tests, données, scripts d'entraînement et
fichier du modèle ne sont pas distribués. `SENTIMENT_MODELE` permet d'indiquer le
chemin du modèle lorsqu'il n'est pas présent sous `models/sentiment.joblib` dans
l'installation.

## 3. Pourquoi scikit-learn est-il limité à la version 1.5 ?

Le fichier joblib sérialise des objets scikit-learn qui doivent être relus avec une
version compatible. Le projet déclare `scikit-learn>=1.5,<1.6`, et la CI installe le
projet avant d'entraîner le modèle puis de construire et d'essayer la roue. Ainsi,
l'entraînement et la lecture utilisent la même version mineure. Une version différente
peut échouer au chargement, par exemple si un attribut attendu par l'une des versions
n'existe plus dans l'autre.

## Vérification

Les six tests de packaging et la vérification d'installation de la roue sont présents
dans le dépôt et dans la CI. Les sorties locales, l'état GitHub Actions, la validation
sur un environnement hors dépôt et la capture T41 sont à consigner après leur exécution.
