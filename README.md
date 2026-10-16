# sentiment-app : dépôt du binôme

Application fil rouge du cours *Développement et déploiement d'applications intelligentes*.
Ce dépôt grandit chaque semaine ; la semaine 1 met en place le cadrage et l'environnement. Rien n'est jeté.

## Démarrage rapide

```bash
python -m venv .venv
source .venv/bin/activate        # Windows PowerShell : .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Puis vérifiez :

```bash
python scripts/check_setup.py    # diagnostic lisible : versions, dossiers, Git, fiches
pytest -q                        # les mêmes vérifications, sous forme de tests
```

**Au premier lancement, `pytest` affiche `3 failed, 31 passed, 4 skipped` : c'est normal.** Les trois échecs sont les fiches de cadrage encore vides, les quatre tests ignorés attendent que le dépôt Git existe. En fin de TP, la même commande affiche `38 passed`.

Les scripts `scripts/setup.sh` (Linux, macOS, Git Bash) et `scripts/setup.ps1` (Windows) font l'installation et le diagnostic en une commande.

## Par où commencer

| Fichier | Quand le lire |
| --- | --- |
| `MARCHE-A-SUIVRE.md` | Pendant la séance : huit étapes, huit contrôles, les résultats attendus |
| `TP1-ENONCE.md` | L'énoncé du TP : objectifs, livrables, grille de notation |
| `TESTS.md` | La démarche de test en détail, et les trois états de référence |
| `AIDE-GIT.md` | Les commandes Git du TP et la résolution d'un conflit |
| `DEPANNAGE.md` | Quand quelque chose échoue |
| `docs/cadrage/GRILLE-DE-DECISION.md` | Pendant la partie A, pour remplir les fiches |
| `exemples/README.md` | Après le TP, pour voir à quoi ressembleront les semaines 2 et 5 |

## Raccourcis

Sous Linux, macOS et Git Bash, un `Makefile` évite de retaper les commandes :

```bash
make setup          # venv, dépendances, diagnostic
make check          # diagnostic seul
make test           # les 38 tests
make test-cadrage   # les 12 tests des fiches
make verif URL=https://github.com/<organisation>/sentiment-app.git
make exemple-ml     # entraîne le modèle d'exemple (facultatif)
make help           # la liste complète
```

## Structure

```text
sentiment-app/
├── README.md, MARCHE-A-SUIVRE.md, TP1-ENONCE.md, TESTS.md, AIDE-GIT.md, DEPANNAGE.md
├── Makefile              # raccourcis (optionnel)
├── requirements.txt      # dépendances du semestre, versions figées
├── .gitignore, .env.example, .editorconfig, pytest.ini
├── .vscode/              # interpréteur et tests préconfigurés
├── data/                 # jeux de données (DVC à partir de la semaine 7)
├── models/               # modèles entraînés (jamais dans Git)
├── app/                  # API FastAPI (semaine 3)
├── ui/                   # interface Streamlit (semaine 5)
├── tests/                # pytest : 23 + 12 + 3 = 38 tests en semaine 1
├── scripts/              # setup, diagnostic, création de fiche, init du dépôt, clone de vérification
├── notebooks/            # variante Colab du TP1
└── docs/cadrage/         # fiches de cadrage, exemple corrigé, grille, banque de cas
```

## Membres du binôme

| Rôle | Nom | Identifiant GitHub | Travail de la semaine 1 | Travail de la semaine 2 |
| --- | --- | --- | --- | --- |
| Membre A | mouad salah | @mouadslh | Création du dépôt, fiches de cadrage, requirements.lock | • Module de prédiction (`src/predict.py`) et tests (`tests/test_model.py`)<br>• Résolution des conflits de fusion Git et réconciliation des branches<br>• Configuration de la CI (`.github/workflows/ci.yml`)<br>• Suivi et versionnement des métriques (`models/metrics.json`) |
| Membre B | med mounir elhamss | @mounir-med | Clone du dépôt, installation de l'environnement, relecture des fiches, vérification du clone frais | • Pipeline d'entraînement TF-IDF + LogisticRegression (`src/train.py`)<br>• Données synthétiques et démo autonome (`src/make_demo.py`)<br>• Évaluation et matrice de confusion (`src/plot_confusion.py`)<br>• Rédaction de l'analyse des erreurs (`docs/semaine2.md`) |

### Traçabilité du travail - Semaine 2

* **Mouad Salah (Membre A)** :
  * Intégration et validation du module d'inférence/prédiction (`src/predict.py`) avec gestion des seuils de confiance.
  * Rédaction et validation des tests unitaires (`tests/test_model.py`).
  * Réconciliation Git des historiques sans relation, résolution des conflits et merge.
  * Maintien du workflow CI GitHub Actions (`.github/workflows/ci.yml`) et configuration des exclusions `.gitignore` pour `models/metrics.json`.

* **Med Mounir Elhamss (Membre B)** :
  * Implémentation du pipeline d'entraînement scikit-learn (`src/train.py`) sur le corpus Allociné et fallback local.
  * Développement du script de génération de données de démonstration (`src/make_demo.py`).
  * Calcul des scores ($F_1$, Rappel négatif, Accuracy) et tracé de la matrice de confusion (`src/plot_confusion.py`).
  * Rédaction de l'analyse des erreurs de classification sur avis mitigés (`docs/semaine2.md`).


