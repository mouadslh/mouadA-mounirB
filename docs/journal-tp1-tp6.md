# Journal de bord du binôme : TP1 à TP6

**Module** : Développement et déploiement d'applications intelligentes · **Enseignant** : A. Larhlimi

| | Membre A | Membre B |
| --- | --- | --- |
| Nom | Mouad Salah | Elhamss Med Mounir |
| Compte GitHub | @mouadslh | @mounir-med |

**Dépôt** : https://github.com/mouadslh/mouadA-mounirB

**Version livrée** : `0.6.0` · **Étiquette Git** : `v0.6.0`


> Version de remise mise à jour le 28 octobre 2026 à partir du dépôt. Les commandes et résultats historiques non archivés sont signalés comme tels ; ils ne sont pas reconstitués depuis les résultats attendus. Les captures de séance n'ont pas été conservées dans le dépôt. Les résultats de reprise et la CI sont rapportés lorsqu'ils sont vérifiables. Le défaut Unicode Hypothesis a été corrigé dans `37f18a7`; l'isolation du client de lot a été corrigée dans `26ae0ee`. La CI de la version `0.6.0` est verte. Les détails TP4 et TP5 figurent aussi dans `docs/semaine4.md` et `docs/semaine5.md`.

## Repères de lecture

Ce document synthétise les travaux TP1 à TP6 du dépôt indiqué ci-dessus. Les sorties historiques qui n'ont pas été archivées sont identifiées explicitement et ne sont pas reconstituées à partir des résultats attendus. Les preuves disponibles sont les fichiers du dépôt, les rapports TP4/TP5 et la CI de la version livrée. Les captures d'écran de séance n'ont pas été conservées.

---

## 0. La préparation des postes

### Poste du membre A

```powershell
py -0
py -3.11 --version
git --version
git config --global user.name
```

**Attendu** : une version 3.11 dans la liste, `Python 3.11.x`, une version de Git, le nom du membre A.

**Obtenu** :

```text
Trace de séance non conservée dans le dépôt.
```

- Preuve historique (sortie/capture) : non archivée.

**Commentaire** :

> La sortie de ce contrôle doit être prise sur le poste de Mouad : version de Python, version de Git et nom Git configuré. Aucune capture de ce poste n'est conservée.


### Poste du membre B

```powershell
py -0
py -3.11 --version
git --version
git config --global user.name
```

**Attendu** : une version 3.11, `Python 3.11.x`, une version de Git, le nom du membre B, différent de celui du membre A.

**Obtenu** :

```text
Trace de séance non conservée dans le dépôt.
```

- Preuve historique (sortie/capture) : non archivée.

**Commentaire** :

> La sortie historique et la capture de ce contrôle ne sont pas archivées ; le binôme doit les relever sur le poste concerné.


---

## TP1 : cadrer l'application et préparer l'environnement

### T0 · La structure du kit (membre A)

```powershell
Get-ChildItem -Force
```

**Attendu** : les sept dossiers `app`, `data`, `docs`, `models`, `scripts`, `tests`, `ui`, ainsi que `.github` et `.gitignore`.

**Obtenu** :

```text
Reprise locale du 21/10/2026 : `scripts/check_setup.py` indique `0 erreur(s), 0 avertissement(s)`. Les dossiers contrôlés incluent `data/`, `models/`, `app/`, `ui/`, `tests/`, `scripts/` et `docs/cadrage/`. Le dépôt actuel contient également `api/`.
```

- Preuve historique (sortie/capture) : non archivée.

**Commentaire** :

> Le diagnostic confirme la structure de reprise et l'environnement courant. Ce relevé ne prouve pas la sortie historique de T0 ; la capture de séance n'est pas disponible.


### T1 · L'environnement et le point de départ (membre A)

```powershell
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
python --version
pip install -r requirements.txt
python -m pip freeze | Out-File -Encoding utf8 requirements.lock
python scripts/check_setup.py
python -m pytest -q
```

**Attendu** : `Python 3.11.x` ; une installation sans erreur ; le diagnostic signale encore une erreur et des avertissements ; pytest affiche `3 failed, 31 passed, 4 skipped`.

**Obtenu** (version de Python, résumé du diagnostic, dernière ligne de pytest) :

```text
Reprise du 21/10/2026 : Python 3.11.17 et diagnostic final `0 erreur(s), 0 avertissement(s)`. Cette exécution avait donné `1 failed, 96 passed, 6 xfailed` à cause du surrogate Unicode isolé `\ud800`. Le défaut a ensuite été corrigé (`37f18a7`) et la CI de la version livrée passe.
```

- Preuve historique (sortie/capture) : non archivée.

**Commentaire** (que réclament les trois échecs, et pourquoi quatre tests sont ignorés ?) :

> Ces résultats de reprise ne reconstituent pas le point de départ historique du TP1. L'échec Unicode observé pendant la reprise a été corrigé et validé par la CI de la version livrée.


### T2 · Les fiches de cadrage (à deux)

```powershell
python -m pytest tests/test_cadrage.py -q
python -m pytest -q
```

**Attendu** : `12 passed`, puis `34 passed, 4 skipped`.

**Obtenu** :

```text
Reprise locale : `tests/test_cadrage.py` affiche `12 passed in 0.12s`.
```

- Preuve historique (sortie/capture) : non archivée.

**Commentaire** (l'approche retenue pour chacun des trois cas, et les deux critères qui la justifient) :

> Les douze contrôles de présence et de contenu des trois fiches passent. Les choix cadrage visibles dans le dépôt reposent sur la stabilité des règles, la disponibilité d'exemples étiquetés et la nature de la réponse attendue ; la sortie historique de la seconde commande n'est pas conservée.


### T3 · Le dépôt GitHub et le premier push (membre A)

```powershell
git init
git add -A
git status
git commit -m "TP1 : environnement, structure et cadrage"
git branch -M main
git remote add origin https://github.com/<compte-A>/sentiment-app.git
git push -u origin main
python -m pytest -q
```

**Attendu** : `git status` ne liste ni `.venv/`, ni `.env`, ni fichier `.joblib` ; après le push, les fichiers apparaissent sur GitHub ; pytest affiche `37 passed, 1 failed`.

**Obtenu** (extrait de `git status`, dernière ligne de pytest) :

```text
Reprise du 21/10/2026 : `main` est synchronisée avec `origin/main` ; le dernier push a abouti. Le dépôt ne suit pas `.venv/` et les règles `.gitignore` couvrent les fichiers sensibles et modèles. Sortie pytest historique de T3 non conservée.
```

- Preuve historique (sortie/capture) : non archivée.

**Commentaire** (quel test échoue encore, et pourquoi ?) :

> Le commit courant est bien présent sur GitHub. Le contrôle du push initial et son résultat `37 passed, 1 failed` ne sont pas reconstructibles depuis le journal de commandes.


### T4 · L'environnement du membre B (membre B)

```powershell
git clone https://github.com/<compte-A>/sentiment-app.git sentiment-app
cd sentiment-app
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python scripts/check_setup.py
```

**Attendu** : `0 erreur(s)` au diagnostic.

**Obtenu** :

```text
Trace de séance non conservée dans le dépôt.
```

- Preuve historique (sortie/capture) : non archivée.

**Commentaire** :

> La sortie historique et la capture de ce contrôle ne sont pas archivées ; le binôme doit les relever sur le poste concerné.


### T5 · Un commit par membre (membres B puis A)

```powershell
git pull
git add README.md
git commit -m "README : ajout de <nom> au tableau du binome"
git push
git shortlog -sn --all
python -m pytest tests/test_git_history.py -q
```

**Attendu** : deux noms distincts dans `git shortlog`, puis `3 passed`.

**Obtenu** :

```text
Reprise : `git shortlog -sn --all` liste `Mouad Salah`, `med mounir` et `Mouad salah` (3 libellés d'auteur, dont deux variantes de casse), et `tests/test_git_history.py` affiche `3 passed`.
```

- Preuve historique (sortie/capture) : non archivée.

**Commentaire** :

> Le test automatisé passe, mais l'historique contient trois chaînes d'auteur au lieu de deux noms canoniques ; les deux membres doivent vérifier la configuration `user.name` sur leurs postes.


### T6 · La vérification finale (à deux)

```powershell
git pull
python scripts/check_setup.py
python -m pytest -q
```

**Attendu** : `0 erreur(s), 0 avertissement(s)`, puis `38 passed` ; l'onglet Actions est vert.

**Obtenu** :

```text
Reprise : le diagnostic affiche `0 erreur(s), 0 avertissement(s)`. La suite complète a affiché `1 failed, 96 passed, 6 xfailed` à cause du cas `\ud800` dans `test_tout_texte_non_blanc_est_traite`.
```

- Preuve historique (sortie/capture) : non archivée.

**Commentaire** :

> La structure et la configuration passent le diagnostic. Le défaut Unicode observé dans cette ancienne exécution a été corrigé ensuite ; la CI de la version livrée `0.6.0` est verte.



### T7 · Le clone frais

```powershell
cd $env:TEMP
git clone https://github.com/<compte-A>/sentiment-app.git verif
cd verif
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python scripts/check_setup.py
python -m pytest -q
```

**Attendu** : `0 erreur(s)` et `38 passed`, sans aucune intervention.

**Obtenu** :

```text
Trace de séance non conservée dans le dépôt.
```

- Preuve historique (sortie/capture) : non archivée.

**Commentaire** (qu'est-ce que ce contrôle prouve que T6 ne prouvait pas ?) :

> La sortie historique et la capture de ce contrôle ne sont pas archivées ; le binôme doit les relever sur le poste concerné.


---

## TP2 : entraîner, évaluer et sauvegarder le modèle

### C1 · Le kit installé (membre A)

```powershell
python C:\IA-DEV\tp2-semaine2\appliquer_tp2.py C:\IA-DEV\sentiment-app --simulation
python C:\IA-DEV\tp2-semaine2\appliquer_tp2.py C:\IA-DEV\sentiment-app
python -m pytest -q
```

**Attendu** : la simulation liste les fichiers du kit et l'ajout de `!models/metrics.json` au `.gitignore` ; pytest affiche `2 failed, 38 passed, 2 skipped`.

**Obtenu** :

```text
Trace de séance non conservée dans le dépôt.
```

- Preuve historique (sortie/capture) : non archivée.

**Commentaire** (que réclament les deux échecs ?) :

> La sortie historique et la capture de ce contrôle ne sont pas archivées ; le binôme doit les relever sur le poste concerné.


### C2 · Le jeu de démonstration

```powershell
python src/make_demo.py
```

**Attendu** : `290 avis écrits`, 145 positifs et 145 négatifs.

**Obtenu** :

```text
Reprise locale : `data/demo_reviews.csv` contient 290 avis : 145 positifs et 145 négatifs (colonnes `review` et `label`). Exemple mitigé : « Commande jamais reçue et remboursement en attente à la livraison, mais finalement produit conforme à la description, très satisfait. »
```

- [x] Conforme

**Commentaire** (recopiez un avis mitigé et expliquez sa structure) :

> L'avis contient d'abord des termes négatifs, puis une conclusion positive après « mais ». Cette structure de retournement explique pourquoi ces phrases sont difficiles à classer avec un modèle TF-IDF.


### C3 · L'entraînement

```powershell
python src/train.py
git status --short
```

**Attendu** : `Vocabulaire : 316 termes`, `F1 macro sur le jeu de test : 0.879 (seuil 0.85)` ; dans `git status`, `models/metrics.json` apparaît, ni `models/sentiment.joblib` ni `data/demo_reviews.csv`.

**Obtenu** :

```text
Reprise depuis les artefacts présents : vocabulaire du modèle sauvegardé, `316 termes` ; `models/metrics.json` indique `source: demo`, `232` avis d'entraînement, `58` de test et F1 macro `0.879`. L'entraînement Allociné historique n'est pas archivé.
```

- Preuve historique (sortie/capture) : non archivée.

**Commentaire** (pourquoi la mesure est-elle versionnée, et pas le modèle ?) :

> Les métriques sont de petits résultats lisibles et comparables, donc versionnés. Le modèle `.joblib` est un artefact binaire régénérable et est ignoré par Git.


### C4 · L'évaluation

```powershell
python src/evaluate.py
```

**Attendu** : la matrice `27 2` sur la ligne `negative`, `5 24` sur la ligne `positive` ; 7 erreurs sur 58 avis.

**Obtenu** (la matrice et les trois erreurs affichées) :

```text
Reprise locale sur 58 avis : matrice (lignes vérité, colonnes prédiction) `negative: 27 2`, `positive: 5 24` ; 7 erreurs. Exemples : avis positif « Taille trop petite et retour payant ... » classé négatif ; avis positif avec « Commande jamais reçue ... sauf que ensuite je recommande » classé négatif ; avis négatif sur produit cassé classé positif à cause des mots positifs initiaux.
```

- [x] Conforme

**Commentaire** (pourquoi le modèle se trompe-t-il sur ces avis ?) :

> Le modèle TF-IDF exploite surtout les mots et bigrammes appris ; il comprend mal les retournements après « sauf que » et le contraste entre termes positifs et négatifs.


### C5 · Le vrai jeu de données, les tests, le push

```powershell
python src/train.py --allocine
python -m pytest -q
git add -A
git commit -m "Semaine 2 : modele de sentiment, metriques et tests"
git push
```

**Attendu** : `Source : allocine, 20000 avis`, `F1 macro sur le jeu de test : 0.920`, puis `42 passed` ; l'onglet Actions est vert.

**Obtenu** :

```text
Trace de séance non conservée dans le dépôt.
```

- Preuve historique (sortie/capture) : non archivée.

**Commentaire** (pourquoi le F1 est-il meilleur sur Allociné ?) :

> La sortie historique et la capture de ce contrôle ne sont pas archivées ; le binôme doit les relever sur le poste concerné.


### Membre B, après le TP2

```powershell
git pull
python src/make_demo.py
python src/train.py
python -m pytest -q
```

**Attendu** : `42 passed`.

**Obtenu** :

```text
Trace de séance non conservée dans le dépôt.
```

- Preuve historique (sortie/capture) : non archivée.


---

## TP3 : exposer le modèle par une API

### T14 · Le kit installé (membre A)

```powershell
python C:\IA-DEV\kit-tp3\appliquer_tp3.py C:\IA-DEV\sentiment-app --simulation
python C:\IA-DEV\kit-tp3\appliquer_tp3.py C:\IA-DEV\sentiment-app
pip install -r requirements.txt
python src/train.py
python -m pytest -q
```

**Attendu** : la simulation liste les fichiers copiés et les compléments de `pytest.ini` et de `ci.yml` ; pytest affiche `48 passed`.

**Obtenu** :

```text
Trace de séance non conservée dans le dépôt.
```

- Preuve historique (sortie/capture) : non archivée.

**Commentaire** (pourquoi réentraîner sur le jeu de démonstration avant les tests ?) :

> La sortie historique et la capture de ce contrôle ne sont pas archivées ; le binôme doit les relever sur le poste concerné.


### T15 · `/health`

```powershell
uvicorn api.main:app --reload
```

Puis, dans `http://localhost:8000/docs` : `GET /health`, « Try it out », « Execute ».

**Attendu** : `200`, `"status": "OK"`, `"model": "tfidf-logreg (TP2, models/sentiment.joblib)"`.

**Obtenu** :

```text
Reprise avec TestClient (cycle de vie activé) : `200`, `{"status":"OK","model":"tfidf-logreg (TP2, models/sentiment.joblib)"}`.
```

- [x] Conforme

**Commentaire** :

> Le endpoint confirme que l'API répond et que le modèle a été chargé au démarrage. La capture Swagger historique n'est pas conservée.


### T16 · Un avis positif

`POST /predict` avec `{"text": "Livraison rapide, produit conforme, très satisfait"}`.

**Attendu** : `200`, `"label": "POSITIVE"`, `"score": 0.777`.

**Obtenu** :

```text
Reprise avec TestClient : `200`, `label=POSITIVE`, `score=0.777`.
```

- [x] Conforme

**Commentaire** :

> L'avis est classé positif avec une confiance de 77,7 %, supérieure au seuil de 0,60.


Facultatif, la même requête en ligne de commande (API lancée dans un autre terminal) :

```powershell
python -c "import httpx; r = httpx.post('http://127.0.0.1:8000/predict', json={'text': 'Livraison rapide, produit conforme, très satisfait'}); print(r.status_code, r.json())"
```

### T17 · Un avis négatif

`POST /predict` avec `{"text": "Produit cassé et service injoignable, à fuir"}`.

**Attendu** : `200`, `"label": "NEGATIVE"`, `"score": 0.7465`.

**Obtenu** :

```text
Reprise avec TestClient : `200`, `label=NEGATIVE`, `score=0.7465`.
```

- [x] Conforme

**Commentaire** :

> L'avis est classé négatif avec une confiance de 74,65 %, supérieure au seuil de 0,60.


### T18 · Les refus

`POST /predict` avec `{"text": ""}`, puis `{}`, puis `{"text": 42}`.

**Attendu** : `422` dans les trois cas.

**Obtenu** (le code et le `detail` de chaque réponse) :

```text
Reprise : texte vide → `422` avec erreur `string_too_short` ; champ absent → `422` avec `missing` ; nombre `42` → `422` avec `string_type`. Chaque détail est renvoyé dans une liste.
```

- [x] Conforme

**Commentaire** (que dit `detail`, et pourquoi 422 plutôt que 500 ?) :

> `422` indique que la requête ne respecte pas le schéma Pydantic ; `500` serait réservé à une panne interne du serveur.


### T19 · La CI

```powershell
git add -A
git commit -m "Semaine 3 : API FastAPI"
git push
```

**Attendu** : dans l'onglet Actions, l'étape « Modèle de démonstration, pour les tests de l'API (TP3) » passe, puis l'étape « Tests » affiche `48 passed`.

**Obtenu** :

```text
Trace de séance non conservée dans le dépôt.
```

- Preuve historique (sortie/capture) : non archivée.

**Commentaire** (pourquoi la CI doit-elle entraîner le modèle ?) :

> La sortie historique et la capture de ce contrôle ne sont pas archivées ; le binôme doit les relever sur le poste concerné.


### T20 · L'API sans modèle

```powershell
Rename-Item models/sentiment.joblib sentiment.bak
uvicorn api.main:app
Rename-Item models/sentiment.bak sentiment.joblib
```

**Attendu** : `FileNotFoundError: models/sentiment.joblib absent : lancez python src/train.py`, puis `Application startup failed`.

**Obtenu** :

```text
Trace de séance non conservée dans le dépôt.
```

- Preuve historique (sortie/capture) : non archivée.

**Commentaire** :

> La sortie historique et la capture de ce contrôle ne sont pas archivées ; le binôme doit les relever sur le poste concerné.


### Membre B, après le TP3

```powershell
git pull
python src/make_demo.py
python src/train.py
python -m pytest -q
```

**Attendu** : `48 passed`.

**Obtenu** :

```text
Trace de séance non conservée dans le dépôt.
```

- Preuve historique (sortie/capture) : non archivée.


---

## TP4 : tests approfondis et qualité

### T21 · Le kit installé et le point de départ (membre A)

```powershell
python C:\IA-DEV\tp4-tests-qualite\appliquer_tp4.py C:\IA-DEV\sentiment-app
pip install -r requirements-dev.txt
python src/train.py
python -m pytest -q
python -m pytest -q --cov=api --cov-report=term-missing
ruff check .
mypy api
```

**Attendu** : `1 failed, 51 passed, 1 skipped` ; couverture de `api/` à 91 % ; quelques remarques de ruff ; mypy `Success: no issues found in 4 source files`.

**Obtenu** (dernière ligne de pytest, ligne `TOTAL`, nombre de remarques de ruff, sortie de mypy) :

```text
Relevé documenté après corrections : couverture API `97,67 %` (86 instructions, 2 manquantes) ; au départ, le relevé de couverture n'a pas été fait. `docs/semaine4.md` rapporte 25 remarques ruff et 2 erreurs mypy avant corrections. En reprise : `ruff check .` affiche `All checks passed!`, `mypy api` affiche `Success: no issues found in 4 source files`.
```

- Preuve historique (sortie/capture) : non archivée.

**Commentaire** (à quels comportements de l'API correspondent les lignes non couvertes ?) :

> La couverture finale et les sorties statiques après correction sont documentées. Les lignes non couvertes (83–85 de `api/main.py`) correspondent au lancement direct Uvicorn, contourné par TestClient ; le point de départ exact n'est pas archivé.


### T22 · Le contrat d'entrée corrigé

Avant la correction du schéma :

```powershell
python -m pytest -q tests/test_limites.py
```

**Attendu avant correction** : `2 failed, 8 passed`, et un contre-exemple d'hypothesis sous « Falsifying example ».

**Obtenu avant correction** (dernière ligne et contre-exemple) :

```text
Sortie historique avant correction non conservée. En reprise, le contre-exemple d'Hypothesis est `\ud800` : ce caractère surrogate n'est pas encodable en UTF-8 dans le détail de validation.
```

Après la correction, dans `/docs` : `POST /predict` avec `{"text": "   "}`.

**Attendu après correction** : `422`, avec un `detail` en liste, comme pour `{"text": ""}`.

**Obtenu après correction** :

```text
Reprise : `POST /predict` avec trois espaces renvoie `422` et un `detail` au format liste, comme le texte vide.
```

- [x] Conforme

**Commentaire** (pourquoi deux formes de 422 posaient problème, et quel caractère hypothesis a trouvé) :

> La validation doit rejeter les espaces comme le texte vide avec une seule forme de réponse. Hypothesis a ensuite découvert un autre cas limite Unicode (`\ud800`), encore à traiter.


### T23 · Les propriétés

```powershell
python -m pytest -q tests/test_limites.py
python -m pytest -q tests/test_limites.py
python -m pytest -q tests/test_limites.py
```

**Attendu** : `10 passed`, trois fois de suite.

**Obtenu** :

```text
Reprise reproductible avec `--hypothesis-seed=20261021` sur les tests jeu d'or, limites et intégration : `33 passed, 6 xfailed`. Lors d'une exécution non seedée, Hypothesis a trouvé `\ud800` et le test des textes non blancs a échoué avec `UnicodeEncodeError`.
```

- Preuve historique (sortie/capture) : non archivée.

**Commentaire** :

> Les cas déterministes et les erreurs connues passent ou restent déclarés xfail. Le cas Unicode découvert pendant la reprise a été corrigé dans `37f18a7` et couvert par un test.


### T24 · L'abstention

```powershell
python src/courbe_seuil.py
```

**Attendu** : la première ligne `0.50  58  100%  0.879  7  0`. Dans `/docs`, un texte fait de mots inventés reçoit ensuite `INDETERMINE`.

**Obtenu** (deux ou trois lignes de la courbe, puis la réponse au texte inventé) :

```text
Reprise réelle : `0.50  58  100%  0.879  7  0`, `0.60  42  72%  0.952  2  16`, `0.75  29  50%  1.000  0  29`. L'avis inventé renvoie `INDETERMINE`, score `0.5162`.
```

- [x] Conforme

**Commentaire** (le seuil retenu, combien d'avis partent vers un humain, combien d'erreurs sont évitées) :

> Le seuil retenu est 0,60 : 16 avis sur 58 sont dirigés vers un humain et 5 erreurs automatiques de moins qu'à 0,50. Le modèle répond automatiquement à 42 avis avec 2 erreurs.



### T25 · Le jeu d'or

```powershell
python src/bilan_jeu_or.py
python -m pytest -q tests/test_jeu_or.py
```

**Attendu** : le bilan du jeu d'or du dépôt (21 avis) ; aucun `failed`, les erreurs déclarées en `xfail`.

**Obtenu** (la ligne de bilan, puis la dernière ligne de pytest) :

```text
Reprise : bilan sur 21 avis : `abstention 8, erreur franche déclarée 6, juste 7`. La suite ciblée affiche `33 passed, 6 xfailed` avec les tests de limites et d'intégration inclus.
```

- [x] Conforme

**Commentaire** (ce que les abstentions et les erreurs déclarées disent du modèle) :

> Les abstentions signalent des cas où la confiance est sous 0,60 ; les six xfails rendent les erreurs connues visibles au lieu de les masquer. Le jeu doit encore être validé par le binôme.


### T26 · L'intégration et la couverture

```powershell
python -m pytest -q tests/test_integration.py
python -m pytest -q --cov=api --cov-report=term-missing --cov-fail-under=95
```

**Attendu** : avant la correction de `main.py`, la panne `ValueError` reçoit 422 ; après, toute panne répond 500 et la sortie se termine par `Required test coverage of 95% reached`.

**Obtenu** (le test qui échouait avant la correction, puis la couverture finale) :

```text
Reprise : les tests d'intégration passent dans l'exécution ciblée ; couverture API totale `97,67 %`, supérieure au seuil de 95 %. La suite complète de reprise reste affectée par l'échec Unicode décrit à T23.
```

- Preuve historique (sortie/capture) : non archivée.

**Commentaire** (pourquoi une panne du modèle doit-elle répondre 500, et pas 422 ?) :

> Une panne du modèle est une erreur interne serveur (500), pas une erreur de saisie utilisateur (422). La couverture est suffisante, mais le défaut Unicode garde la suite complète non verte.


### T27 · Qualité statique, crochet et CI

```powershell
mypy api
ruff check .
python -m pytest -q
pre-commit install
```

**Attendu** : mypy signale `.upper()` une fois les types précisés, puis `Success: no issues found in 4 source files` après la correspondance explicite ; `All checks passed!` ; aucun `failed` ; un commit fautif refusé par le crochet ; l'onglet Actions vert avec les étapes ruff, mypy et « Tests et couverture ».

**Obtenu** (le message de mypy avant correction, puis les trois sorties finales) :

```text
Reprise : `ruff check .` → `All checks passed!` ; `mypy api` → `Success: no issues found in 4 source files` ; `tests/test_git_history.py` → `3 passed`. Le journal TP4 rapporte 25 remarques ruff et 2 erreurs mypy avant correction. La CI GitHub n'a pas été consultée pendant cette reprise.
```

- Preuve historique (sortie/capture) : non archivée.

**Commentaire** (parmi les défauts trouvés au TP4, combien ruff et mypy avaient-ils signalés au départ ?) :

> Les outils statiques ne signalent plus de défauts. Les valeurs initiales consignées sont 25 remarques ruff et 2 erreurs mypy ; la CI de la version livrée est verte.



### Membre B, après le TP4

```powershell
git pull
pip install -r requirements-dev.txt
python src/train.py
pre-commit install
python -m pytest -q
```

**Attendu** : aucun `failed`.

**Obtenu** :

```text
Trace de séance non conservée dans le dépôt.
```

- Preuve historique (sortie/capture) : non archivée.


---

## TP5 : l'interface Streamlit

### T28 · Le kit installé (membre A)

```powershell
python C:\IA-DEV\tp5-interface\appliquer_tp5.py C:\IA-DEV\sentiment-app --simulation
python C:\IA-DEV\tp5-interface\appliquer_tp5.py C:\IA-DEV\sentiment-app
python src/train.py
python -m pytest -q
```

**Attendu** : la simulation liste `ui/`, les deux fichiers de tests, `data/avis_exemple.csv` et `docs/semaine5.md`, puis les compléments du `.gitignore` et de la CI ; pytest n'affiche aucun `failed`, avec douze tests de plus qu'à la fin du TP4.

**Obtenu** :

```text
Reprise : les tests client/UI/API ciblés affichaient `17 passed, 1 warning`. Cette ancienne exécution complète a donné `1 failed, 96 passed, 6 xfailed` (cas Unicode Hypothesis), corrigé depuis dans `37f18a7`; l'isolation du test client a été corrigée dans `26ae0ee`.
```

- Preuve historique (sortie/capture) : non archivée.

**Commentaire** (que vérifient les tests du client, et ceux de la page ?) :

> Les tests client contrôlent le décodage des réponses API et les erreurs ; ceux de la page contrôlent l'affichage des états positif, négatif, abstention et erreur. Les défauts révélés pendant la reprise sont corrigés dans la version livrée.


### T29 · La page ouverte, l'API prête

Deux terminaux, dans le dépôt :

```powershell
uvicorn api.main:app --reload
```

```powershell
streamlit run ui/app.py
```

**Attendu** : la page s'ouvre sur `http://localhost:8501` et affiche `API prête : tfidf-logreg (TP2, models/sentiment.joblib)`.

**Obtenu** :

```text
Déjà observé sur l'interface locale : la page Streamlit s'ouvre et affiche que l'API est prête.
```

- [x] Conforme

**Commentaire** :

> Streamlit appelle l'API FastAPI via le client HTTP ; le message prêt confirme que le point de santé répond. La capture n'a pas été archivée.


### T30 · Les verdicts

Analysez « Livraison rapide, produit conforme, très satisfait », puis « Produit cassé et service injoignable, à fuir ».

**Attendu** : Avis positif, 78 % ; puis Avis négatif, 75 %.

**Obtenu** :

```text
Contrôle observé : le premier avis affiche `Avis positif`, 78 % (API : POSITIVE, score 0.777) ; le second `Avis négatif`, 75 % (API : NEGATIVE, score 0.7465).
```

- [x] Conforme

**Commentaire** (d'où viennent ces pourcentages ?) :

> Les pourcentages sont les scores de confiance renvoyés par le modèle, arrondis à l'affichage. Ces deux scores dépassent le seuil d'abstention de 0,60.



### T31 · L'abstention

Analysez « xqzvb wlkptr grombu ».

**Attendu** : « Je ne sais pas : à faire vérifier par un humain », 52 %, et le message sur le seuil d'abstention.

**Obtenu** :

```text
Contrôle observé : `Je ne sais pas : à faire vérifier par un humain`, 52 % (API : INDETERMINE, score 0.5162), avec le message sur le seuil d'abstention.
```

- [x] Conforme

**Commentaire** (pourquoi cet affichage vaut-il mieux qu'un verdict forcé ?) :

> Le score est sous 0,60 ; l'application signale l'incertitude et demande un jugement humain plutôt que de présenter une classe peu fiable comme certaine.


### T32 · Les erreurs

Analysez trois espaces. Arrêtez ensuite l'API (`Ctrl+C` dans son terminal), rechargez la page, puis relancez l'API.

**Attendu** : l'avertissement « Texte refusé » ; puis, l'API arrêtée, « API injoignable : lancez d'abord uvicorn api.main:app ».

**Obtenu** :

```text
Reprise API : trois espaces renvoient `422` avec un `detail` de validation. L'indisponibilité de l'API n'a pas été rejouée pendant cette reprise.
```

- Preuve historique (sortie/capture) : non archivée.

**Commentaire** (quelle réponse de l'API se cache derrière chaque message ?) :

> Les espaces sont rejetés par la validation d'entrée de FastAPI (422). Quand le serveur est arrêté, le client doit afficher son message d'API injoignable ; ce second cas reste à capturer.



### T33 · Un fichier d'avis

Onglet « Un fichier d'avis », fichier `data/avis_exemple.csv`, puis « Télécharger les résultats ».

**Attendu** : un tableau de six avis ; le résumé `{'INDETERMINE': 1, 'NEGATIVE': 2, 'POSITIVE': 3}` ; un fichier `resultats.csv` téléchargé.

**Obtenu** :

```text
`docs/semaine5.md` indique 6 avis dans le CSV et 1 abstention pour le modèle de démonstration. Le téléchargement réel du fichier `resultats.csv` n'a pas de capture archivée.
```

- Preuve historique (sortie/capture) : non archivée.

**Commentaire** (combien d'avis partent vers un humain, et lesquels ?) :

> Un avis part vers un humain selon le compte-rendu TP5. Le texte de l'avis et le téléchargement doivent être confirmés par une capture de la recette originale.


### T34 · Compte rendu, push, CI

```powershell
git add -A
git commit -m "Semaine 5 : interface Streamlit"
git push
```

**Attendu** : `docs/semaine5.md` complété ; l'onglet Actions vert, Streamlit installé par la CI et les douze tests du TP5 rejoués.

**Obtenu** :

```text
Le compte-rendu TP5 est présent et les commits sont poussés sur `main` (`2b55e3a` visible sur `origin/main`). Le statut GitHub Actions n'a pas été vérifié.
```

- Preuve historique (sortie/capture) : non archivée.

**Commentaire** :

> Les réponses de semaine 5 sont rédigées et le push est confirmé. Le journal ne peut pas attester que l'onglet Actions est vert sans consulter l'exécution GitHub.


### Membre B, après le TP5

```powershell
git pull
python src/train.py
python -m pytest -q
streamlit run ui/app.py
```

**Attendu** : aucun `failed`, puis la page « API prête » une fois l'API lancée.

**Obtenu** :

```text
Trace de séance non conservée dans le dépôt.
```

- Preuve historique (sortie/capture) : non archivée.


---

## Les difficultés rencontrées

Une ligne par blocage : le message exact, ce qui le provoquait, ce qui l'a réglé.

| TP | Commande | Message | Cause | Solution |
| --- | --- | --- | --- | --- |
| Reprise 21/10/2026, corrigée le 26/10/2026 | `pytest -q` | `UnicodeEncodeError: surrogates not allowed` | Hypothesis avait généré le surrogate isolé `\ud800`, ensuite renvoyé dans le détail de validation 422. | `api/schemas.py` normalise les caractères Unicode non scalaires ; la propriété correspondante est couverte par un test (`37f18a7`). La CI de la version livrée passe. |
| TP1 / reprise | `git shortlog -sn --all` | Trois libellés d'auteur au lieu de deux | L'historique conserve plusieurs variantes de nom d'auteur (`Mouad Salah`, `Mouad salah`, `med mounir`). | Les noms affichés dans les documents sont harmonisés ; l'historique des commits est conservé. |

## La répartition du travail

| TP | Ce qu'a fait le membre A | Ce qu'a fait le membre B |
| --- | --- | --- |
| TP1 | Mouad : configuration de l'environnement Python 3.11, diagnostic de build et CI GitHub Actions. | Mounir : création du dépôt GitHub, cadrage multicritère des cas d'usage et structuration initiale de la documentation. |
| TP2 | Mouad : pipeline scikit-learn, entraînement sur le corpus Allociné et analyse qualitative des erreurs d'inférence. | Mounir : cadrage métier, validation des métriques de classification et du seuil F1 macro. |
| TP3 | Mouad : architecture FastAPI, schémas Pydantic et tests d'API (`test_api.py`). | Mounir : validation de `/health` et `/predict`, tests manuels Swagger et vérification du démarrage fail-fast. |
| TP4 | Mouad : tests limites et propriétés Hypothesis (`test_limites.py`), courbe de seuil, abstention à 0,60 et rédaction des rapports TP4. | Mounir : rédaction/annotation du jeu d'or, cas difficiles et erreurs connues, tests d'intégration et pannes 500, configuration de ruff, mypy et pre-commit. |
| TP5 | Mouad : installation du kit TP5, configuration de Streamlit dans la CI et recette des contrôles T29 à T31. | Mounir : recette des contrôles T32 et T33, ingestion par lot et export CSV, réponses dans `docs/semaine5.md`, mise à jour du journal T0-T34 et rapport TP5. |
| TP6 | Mouad : déplacement du prédicteur dans le paquet, compatibilité API, tests de packaging et construction de la roue. | Mounir : commande `sentiment`, vérification de l'installation isolée, compte rendu TP6 et étiquette `v0.6.0`. |

## Le bilan

**TP1** :

> Le diagnostic de reprise passe. Les sorties historiques de démarrage et les captures de TP1 ne sont pas conservées ; elles ne sont donc pas présentées comme preuves de séance.

**TP2** :

> Le modèle de démonstration atteint un F1 macro de 0,879 sur 58 avis ; la courbe du seuil 0,60 envoie 16 avis à un humain et conserve 2 erreurs automatiques. Les sorties historiques Allociné du TP2 ne sont pas archivées dans le journal.

**TP3** :

> L'API expose `/health` et `/predict`, valide les entrées et démarre en échouant clairement si le modèle manque. Les requêtes positives et négatives ont renvoyé 200 lors de la reprise ; les sorties Swagger historiques ne sont pas archivées.

**TP4** :

> Les outils ruff et mypy passent, la couverture API atteint 97,67 % et le jeu d'or conserve ses erreurs connues en les déclarant explicitement. Le défaut Unicode Hypothesis a été corrigé et la CI de la version livrée est verte.

**TP5** :

> L'interface affiche les verdicts positifs/négatifs et l'abstention. Les réponses TP5 sont documentées. Les sorties historiques du lot CSV ne sont pas archivées ; la CI de la version `0.6.0` est verte.

---

## TP6 : paquet installable

Les contrôles TP6 ont été ajoutés au dépôt avec le paquet `sentiment_app`, la commande `sentiment`, la roue et la vérification de son installation dans un environnement isolé de la CI.

### T35-T37 : paquet et compatibilité

```powershell
python -m pytest -q tests/test_packaging.py
python src/predict.py "Livraison rapide, produit conforme, très satisfait"
Select-String -Path api\*.py -Pattern "sys.path"
ruff check .
mypy api
```

Le prédicteur est fourni sous `sentiment_app.predict`; `src/predict.py` reste un adaptateur historique vers le même module. L'API importe le paquet directement. La CI de la version `0.6.0` valide les tests, ruff, mypy et la construction/installation de la roue. Les journaux locaux complets des postes ne sont pas archivés.

### T38-T40 : commande et roue

```powershell
pip install -e ".[ui]"
sentiment --version
sentiment predict "Livraison rapide, produit conforme, très satisfait"
sentiment predict "xqzvb wlkptr grombu"
sentiment serve
python -m build --wheel
```

La version déclarée est `0.6.0`; le modèle et scikit-learn sont bornés à la même version mineure 1.5. Le modèle n'est pas inclus dans la roue ; `SENTIMENT_MODELE` permet de fournir son chemin. La CI vérifie l'installation de la roue dans un environnement isolé et exécute la prédiction avec le modèle préparé par le pipeline.

### T41 : intégration continue et étiquette

La CI construit la roue, l'installe dans un environnement temporaire et lance la prédiction avec le modèle entraîné par la CI. La version livrée porte l'étiquette annotée `v0.6.0`; la CI de cette version est verte. Les captures de la page GitHub Actions ne sont pas archivées dans le dépôt.
