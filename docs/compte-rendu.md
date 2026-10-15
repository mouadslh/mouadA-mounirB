# Compte-rendu du projet sentiment-app

**Équipe** : Med Mounir Elhamss et Mouad Salah

**Dépôt GitHub** : https://github.com/mouadslh/mouadA-mounirB.git

---

## 1. Besoin métier et cadrage

Une équipe relation client reçoit plusieurs milliers d'avis par jour. L'objectif est de **prioriser automatiquement les avis négatifs** pour les traiter en urgence et limiter l'impact sur la réputation de l'entreprise. Actuellement, les agents doivent parcourir manuellement tous les avis, ce qui est chronophage et fait passer certains avis négatifs inaperçus.

Nous avons étudié trois cas d'usage IA et appliqué les critères de décision :

- **(a) Disponibilité des données étiquetées** : Les avis clients sont déjà étiquetés implicitement via les notes (1-2 étoiles = négatif, 4-5 étoiles = positif). On dispose donc gratuitement d'un grand volume de données d'entraînement.

- **(b) Explicabilité** : Bien que souhaitable, l'explicabilité n'est pas critique ici. Il suffit que le modèle classe correctement, sans nécessairement expliquer pourquoi.

- **(c) Volume de données** : Le volume est élevé (milliers d'avis par jour), ce qui fournit suffisamment de données pour entraîner et maintenir un modèle ML.

- **(d) Conséquence d'une erreur** : Une erreur de classification est **peu grave**. Un négatif manqué sera traité avec retard, et un positif classé négatif sera lu sans conséquence négative.

**Conclusion** : Le **machine learning supervisé** est l'approche la plus adaptée, car nous avons des étiquettes gratuites (critère a), un gros volume de données (critère c) et une faible gravité des erreurs (critère d).

---

## 2. Architecture du dépôt

Le dépôt suit une structure classique avec séparation des responsabilités :

```
sentiment-app/
├── src/            # Code source (entraînement, évaluation, prédiction)
├── ui/             # Interface Streamlit
├── tests/          # Tests unitaires
├── data/           # Données (non versionnées)
├── models/         # Modèles et métriques
├── docs/           # Documentation et fiches de cadrage
└── .github/        # CI/CD
```

### Fichiers versionnés et non versionnés

- **`models/metrics.json`** : **versionné**. Ce fichier JSON contient les métriques d'évaluation (F1-score, accuracy, recall). Il est léger et permet de suivre l'évolution des performances du modèle au fil des commits.

- **`models/sentiment.joblib`** : **non versionné** (dans `.gitignore`). Le modèle entraîné est un fichier binaire volumineux (~2 Mo) qui change fréquemment. Le versionner polluerait l'historique Git. On peut toujours le régénérer avec `python src/train.py`.

- **`data/demo_reviews.csv`** : **non versionné**. Ce fichier est généré par `src/make_demo.py` et peut être recréé à tout moment.

Cette approche garantit un dépôt léger tout en conservant la traçabilité des performances.

---

## 3. Modèle de classification

### Données

Nous avons utilisé deux sources de données :

1. **Démonstration locale** (`data/demo_reviews.csv`) : 290 avis synthétiques générés de manière déterministe (graine 42), avec 145 positifs et 145 négatifs. Les avis incluent des cas nets, mitigés et neutres.

2. **Dataset Allociné** : 20 000 critiques de films en français, téléchargées depuis Hugging Face. Nous utilisons le split de validation (20 000 avis).

### Pipeline

Le modèle repose sur un **pipeline scikit-learn** :

1. **TF-IDF Vectorizer** : Transforme le texte en vecteurs numériques. Paramètres :
   - `ngram_range=(1, 2)` : capture les mots seuls et les bigrammes ("très satisfait", "jamais reçue")
   - `min_df=2` : ignore les termes trop rares
   - `sublinear_tf=True` : lisse les fréquences pour réduire le poids des mots très fréquents

2. **Régression Logistique** : Classifieur linéaire simple et rapide. Paramètres :
   - `max_iter=1000` : assure la convergence
   - `class_weight="balanced"` : compense les déséquilibres de classes
   - `random_state=42` : reproductibilité

### Découpage

**Crucial** : Le découpage train/test (80/20) est effectué **avant toute vectorisation** pour éviter le data leakage. Le TF-IDF est ajusté uniquement sur l'ensemble d'entraînement.

### Résultats

#### Sur les données de démonstration :
- **Entraînement** : 232 avis
- **Test** : 58 avis
- **Vocabulaire** : ~316 termes
- **F1-score macro** : **0,8793** (seuil requis : 0,85) ✅
- **Accuracy** : 0,8793
- **Recall négatifs** : 0,9310

#### Sur le dataset Allociné :
- **Entraînement** : 16 000 avis
- **Test** : 4 000 avis
- **Vocabulaire** : ~149 529 termes
- **F1-score macro** : **0,9205**
- **Accuracy** : 0,9205
- **Recall négatifs** : 0,9235

Le modèle dépasse le seuil de 0,85 sur les deux datasets.

### Lecture de la matrice de confusion (démo)

```
              Prédit
              negative  positive
Vérité negative    27         2
       positive     5        24
```

- **Vrais négatifs** (27) : avis négatifs correctement détectés ✅
- **Faux positifs** (5) : avis positifs classés négatifs (fausse alerte, peu grave)
- **Faux négatifs** (2) : avis négatifs manqués (erreur grave ⚠️)
- **Vrais positifs** (24) : avis positifs correctement détectés ✅

Le modèle a un **recall négatif de 93%**, ce qui signifie qu'il détecte correctement 93% des avis négatifs.

Voir l'image : `docs/images/matrice-confusion.png`

---

## 4. Analyse des erreurs

Sur 58 avis de test (démo), le modèle commet **7 erreurs** :

- **2 négatifs classés positifs** (faux négatifs) : erreurs graves car ces avis ne seront pas traités en priorité.
- **5 positifs classés négatifs** (faux positifs) : fausses alertes sans grande conséquence.

### Exemple d'erreur réelle (tiré de `evaluate.py`)

```
Vérité : negative
Prédit : positive
Texte : "Excellent rapport qualité prix au début, sauf que ensuite se casse au bout de deux u..."
```

**Explication** : Le modèle utilise un **sac de mots** qui ne comprend pas l'ordre des phrases. Il voit "excellent", "qualité", "prix" (positifs) et "casse" (négatif), mais ne saisit pas que la conclusion ("se casse") l'emporte sur le début. Les n-grammes (1,2) capturent "qualité prix" mais pas le retournement "sauf que ensuite se casse".

Les avis mitigés avec retournement de sentiment sont la principale source d'erreurs.

---

## 5. Interface et seuil d'incertitude

L'interface Streamlit (`ui/app.py`) propose trois onglets :

1. **Un avis** : Analyse un avis saisi par l'utilisateur. Affiche le sentiment (négatif/positif/à vérifier) et le score de confiance.

2. **Un fichier CSV** : Analyse un fichier d'avis en lot. Affiche des métriques (avis analysés, négatifs détectés, cas à vérifier), un graphique de répartition et un tableau trié (négatifs en tête).

3. **Comment ça marche** : Explications pour un non-spécialiste sur le fonctionnement du modèle, le seuil d'incertitude et les limites.

### Seuil d'incertitude

Nous avons retenu un **seuil de 0,60** : les avis avec un score < 60% sont marqués **"à vérifier"** et nécessitent une validation humaine.

Tests sur `data/demo_reviews.csv` :

| Seuil | Avis à vérifier | % du total |
|-------|-----------------|------------|
| 0,50  | ~15             | ~5%        |
| **0,60**  | **~35**             | **~12%**       |
| 0,75  | ~80             | ~28%       |

Le seuil de 0,60 offre le meilleur compromis :
- **12% des avis** partent vers un agent (charge raisonnable)
- Les cas mitigés, source d'erreurs, sont interceptés
- Les cas clairs sont traités automatiquement

---

## 6. Ce qui a échoué

**À COMPLÉTER par nous** :

- [Liste des incidents techniques rencontrés]
- [Problèmes de dépendances, de configuration, etc.]
- [Difficultés avec les tests ou le déploiement]
- [Erreurs de compréhension des consignes]

---

## 7. Ce que nous ferions autrement

Si nous devions refaire le projet :

1. **Tester un modèle séquentiel** : Un LSTM ou un transformer (CamemBERT) pourrait mieux capturer les retournements de sentiment dans les avis mitigés.

2. **Enrichir le dataset de démo** : Ajouter plus d'avis mitigés avec des patterns variés (ironie, sarcasme, double négation) pour mieux tester les limites du modèle.

3. **Ajouter une API REST** : Exposer le modèle via FastAPI pour permettre une intégration dans d'autres systèmes (CRM, plateforme e-commerce).

4. **Mettre en place un monitoring** : Logger les prédictions et leurs scores pour détecter une dérive du modèle en production.

5. **Tester différents seuils par métrique métier** : Plutôt qu'un seuil fixe de 0,60, calibrer le seuil en fonction du coût réel d'un faux négatif vs. faux positif.

---

## 8. Répartition du travail

**À COMPLÉTER par nous** :

- [Qui a fait quoi : code, tests, documentation, rédaction]
- [Répartition des tâches entre les deux membres]
- [Commits et contributions de chacun]

---

**Rédaction assistée par un assistant d'IA (Kiro) pour la génération du code et un premier jet des documents ; les chiffres ont été relus et vérifiés par nous dans models/metrics.json.**
