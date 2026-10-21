# Journal de bord du binôme : TP1 à TP5

**Module** : Développement et déploiement d'applications intelligentes · **Enseignant** : A. Larhlimi

| | Membre A | Membre B |
| --- | --- | --- |
| Nom | mouad salah | med mounir elhamss |
| Compte GitHub | @mouadslh | @mounir-med |

**Dépôt** : https://github.com/mouadslh/mouadA-mounirB.git


> Reprise du journal (21 octobre 2026) : les sorties historiques TP1 à TP3, les postes du membre B et les captures d'écran n'ont pas été archivés dans ce dépôt. Je ne les reconstitue donc pas à partir des résultats attendus. Les résultats datés de cette reprise sont renseignés quand ils ont pu être vérifiés ; ils ne remplacent pas les captures de séance demandées. Le compte-rendu TP4 est dans `docs/semaine4.md`, les réponses TP5 dans `docs/semaine5.md`. La suite complète exécutée pendant cette reprise a révélé un cas Hypothesis avec le caractère Unicode isolé `\ud800` qui fait échouer la sérialisation JSON de l'erreur 422 ; ce défaut reste à corriger.

## Comment remplir ce journal

Ce fichier se place dans votre dépôt, sous `docs/journal-tp1-tp5.md`, et vos captures d'écran dans `docs/captures/`. Créez ce dossier une fois :

```powershell
New-Item -ItemType Directory -Force docs\captures
```

Après chaque contrôle, remplissez les quatre rubriques de son bloc :

1. **Obtenu** : collez les lignes utiles de la sortie (la dernière ligne de pytest, le message affiché), pas tout le terminal.
2. **Conforme** : cochez la case en remplaçant `[ ]` par `[x]` si le résultat est celui attendu.
3. **Commentaire** : deux ou trois phrases. Ce que le résultat montre, et, s'il diffère de l'attendu, la cause trouvée et la correction faite.
4. **Capture** : enregistrez l'image sous le nom exact indiqué dans le bloc. Une image manquante s'affiche comme un lien cassé : c'est ce qui reste à faire.

**Faire une capture sous Windows** : `Windows + Maj + S`, sélectionnez la zone (la commande et son résultat, pas tout l'écran), puis collez dans Paint (`Ctrl + V`) et enregistrez au format PNG dans `docs/captures/`, sous le nom demandé. Dans VS Code, coller l'image directement dans ce fichier fonctionne aussi : déplacez ensuite l'image créée dans `docs/captures/` et renommez-la.

**Ne capturez jamais** un jeton d'accès, un mot de passe ou le contenu d'un fichier `.env`.

À la fin de chaque TP, commitez le journal et les captures :

```powershell
git add docs/journal-tp1-tp5.md docs/captures
git commit -m "Journal : TPn complété"
git push
```

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

- [ ] Conforme

**Commentaire** :

> La sortie de ce contrôle doit être prise sur le poste de Mouad : version de Python, version de Git et nom Git configuré. Aucune capture de ce poste n'est conservée.

![Poste du membre A](captures/tp0-poste-membre-a.png)

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

- [ ] Conforme

**Commentaire** :

> La sortie historique et la capture de ce contrôle ne sont pas archivées ; le binôme doit les relever sur le poste concerné.

![Poste du membre B](captures/tp0-poste-membre-b.png)

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

- [ ] Conforme

**Commentaire** :

> Le diagnostic confirme la structure de reprise et l'environnement courant. Ce relevé ne prouve pas la sortie historique de T0 ; la capture de séance n'est pas disponible.

![T0 : structure du kit](captures/tp1-t0-structure.png)

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
Reprise locale : Python 3.11.17 et diagnostic final `0 erreur(s), 0 avertissement(s)`. Le test complet actuel a donné `1 failed, 96 passed, 6 xfailed` ; l'échec est une propriété Hypothesis sur un surrogate Unicode isolé (`\ud800`).
```

- [ ] Conforme

**Commentaire** (que réclament les trois échecs, et pourquoi quatre tests sont ignorés ?) :

> Ces résultats sont ceux de la reprise, pas le point de départ TP1 attendu. L'échec aléatoire observé vient du domaine de caractères généré, qui inclut un surrogate non encodable en UTF-8.

![T1 : pytest au départ](captures/tp1-t1-pytest.png)

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

- [ ] Conforme

**Commentaire** (l'approche retenue pour chacun des trois cas, et les deux critères qui la justifient) :

> Les douze contrôles de présence et de contenu des trois fiches passent. Les choix cadrage visibles dans le dépôt reposent sur la stabilité des règles, la disponibilité d'exemples étiquetés et la nature de la réponse attendue ; la sortie historique de la seconde commande n'est pas conservée.

![T2 : fiches complètes](captures/tp1-t2-cadrage.png)

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

- [ ] Conforme

**Commentaire** (quel test échoue encore, et pourquoi ?) :

> Le commit courant est bien présent sur GitHub. Le contrôle du push initial et son résultat `37 passed, 1 failed` ne sont pas reconstructibles depuis le journal de commandes.

![T3 : le dépôt sur GitHub](captures/tp1-t3-depot-github.png)

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

- [ ] Conforme

**Commentaire** :

> La sortie historique et la capture de ce contrôle ne sont pas archivées ; le binôme doit les relever sur le poste concerné.

![T4 : diagnostic du membre B](captures/tp1-t4-check-setup-b.png)

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

- [ ] Conforme

**Commentaire** :

> Le test automatisé passe, mais l'historique contient trois chaînes d'auteur au lieu de deux noms canoniques ; les deux membres doivent vérifier la configuration `user.name` sur leurs postes.

![T5 : deux auteurs](captures/tp1-t5-shortlog.png)

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

- [ ] Conforme

**Commentaire** :

> La structure et la configuration passent le diagnostic. La suite n'est pas entièrement verte à cette reprise ; la CI GitHub n'a pas été vérifiée.

![T6 : pytest final](captures/tp1-t6-pytest.png)

![T6 : la CI verte](captures/tp1-t6-actions.png)

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

- [ ] Conforme

**Commentaire** (qu'est-ce que ce contrôle prouve que T6 ne prouvait pas ?) :

> La sortie historique et la capture de ce contrôle ne sont pas archivées ; le binôme doit les relever sur le poste concerné.

![T7 : clone frais](captures/tp1-t7-clone-frais.png)

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

- [ ] Conforme

**Commentaire** (que réclament les deux échecs ?) :

> La sortie historique et la capture de ce contrôle ne sont pas archivées ; le binôme doit les relever sur le poste concerné.

![C1 : point de départ du TP2](captures/tp2-c1-pytest.png)

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

![C2 : jeu de démonstration](captures/tp2-c2-make-demo.png)

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

- [ ] Conforme

**Commentaire** (pourquoi la mesure est-elle versionnée, et pas le modèle ?) :

> Les métriques sont de petits résultats lisibles et comparables, donc versionnés. Le modèle `.joblib` est un artefact binaire régénérable et est ignoré par Git.

![C3 : entraînement](captures/tp2-c3-train.png)

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

![C4 : matrice de confusion](captures/tp2-c4-evaluate.png)

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

- [ ] Conforme

**Commentaire** (pourquoi le F1 est-il meilleur sur Allociné ?) :

> La sortie historique et la capture de ce contrôle ne sont pas archivées ; le binôme doit les relever sur le poste concerné.

![C5 : Allociné et tests](captures/tp2-c5-allocine.png)

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

- [ ] Conforme

![TP2 : poste du membre B](captures/tp2-membre-b.png)

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

- [ ] Conforme

**Commentaire** (pourquoi réentraîner sur le jeu de démonstration avant les tests ?) :

> La sortie historique et la capture de ce contrôle ne sont pas archivées ; le binôme doit les relever sur le poste concerné.

![T14 : 48 tests verts](captures/tp3-t14-pytest.png)

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

![T15 : health dans /docs](captures/tp3-t15-health.png)

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

![T16 : avis positif](captures/tp3-t16-positif.png)

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

![T17 : avis négatif](captures/tp3-t17-negatif.png)

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

![T18 : un refus 422](captures/tp3-t18-refus.png)

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

- [ ] Conforme

**Commentaire** (pourquoi la CI doit-elle entraîner le modèle ?) :

> La sortie historique et la capture de ce contrôle ne sont pas archivées ; le binôme doit les relever sur le poste concerné.

![T19 : la CI du TP3](captures/tp3-t19-actions.png)

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

- [ ] Conforme

**Commentaire** :

> La sortie historique et la capture de ce contrôle ne sont pas archivées ; le binôme doit les relever sur le poste concerné.

![T20 : refus de démarrer](captures/tp3-t20-sans-modele.png)

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

- [ ] Conforme

![TP3 : poste du membre B](captures/tp3-membre-b.png)

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

- [ ] Conforme

**Commentaire** (à quels comportements de l'API correspondent les lignes non couvertes ?) :

> La couverture finale et les sorties statiques après correction sont documentées. Les lignes non couvertes (83–85 de `api/main.py`) correspondent au lancement direct Uvicorn, contourné par TestClient ; le point de départ exact n'est pas archivé.

![T21 : couverture de départ](captures/tp4-t21-couverture.png)

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

![T22 : refus des espaces](captures/tp4-t22-espaces.png)

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

- [ ] Conforme

**Commentaire** :

> Les cas déterministes et les erreurs connues passent ou restent déclarés xfail. Le cas Unicode isolé est une vraie limite à corriger ; je ne coche pas ce contrôle comme totalement conforme.

![T23 : propriétés vertes](captures/tp4-t23-proprietes.png)

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

![T24 : courbe du seuil](captures/tp4-t24-courbe.png)

![T24 : verdict INDETERMINE](captures/tp4-t24-indetermine.png)

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

![T25 : bilan du jeu d'or](captures/tp4-t25-jeu-or.png)

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

- [ ] Conforme

**Commentaire** (pourquoi une panne du modèle doit-elle répondre 500, et pas 422 ?) :

> Une panne du modèle est une erreur interne serveur (500), pas une erreur de saisie utilisateur (422). La couverture est suffisante, mais le défaut Unicode garde la suite complète non verte.

![T26 : couverture finale](captures/tp4-t26-couverture.png)

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

- [ ] Conforme

**Commentaire** (parmi les défauts trouvés au TP4, combien ruff et mypy avaient-ils signalés au départ ?) :

> Les outils statiques ne signalent plus de défauts. Les valeurs initiales connues sont 25 remarques ruff et 2 erreurs mypy ; le statut actuel des Actions reste à vérifier sur GitHub.

![T27 : commit refusé par pre-commit](captures/tp4-t27-pre-commit.png)

![T27 : la CI du TP4](captures/tp4-t27-actions.png)

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

- [ ] Conforme

![TP4 : poste du membre B](captures/tp4-membre-b.png)

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
Reprise : les tests client/UI/API ciblés affichent `17 passed, 1 warning`. Sur l'ensemble, le dernier lancement a donné `1 failed, 96 passed, 6 xfailed` (cas Unicode Hypothesis).
```

- [ ] Conforme

**Commentaire** (que vérifient les tests du client, et ceux de la page ?) :

> Les tests client contrôlent le décodage des réponses API et les erreurs ; ceux de la page contrôlent l'affichage des états positif, négatif, abstention et erreur. La suite complète a encore le cas Unicode à corriger.

![T28 : tests du TP5](captures/tp5-t28-pytest.png)

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

![T29 : la page ouverte](captures/tp5-t29-page.png)

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

![T30 : avis positif](captures/tp5-t30-positif.png)

![T30 : avis négatif](captures/tp5-t30-negatif.png)

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

![T31 : je ne sais pas](captures/tp5-t31-abstention.png)

### T32 · Les erreurs

Analysez trois espaces. Arrêtez ensuite l'API (`Ctrl+C` dans son terminal), rechargez la page, puis relancez l'API.

**Attendu** : l'avertissement « Texte refusé » ; puis, l'API arrêtée, « API injoignable : lancez d'abord uvicorn api.main:app ».

**Obtenu** :

```text
Reprise API : trois espaces renvoient `422` avec un `detail` de validation. L'indisponibilité de l'API n'a pas été rejouée pendant cette reprise.
```

- [ ] Conforme

**Commentaire** (quelle réponse de l'API se cache derrière chaque message ?) :

> Les espaces sont rejetés par la validation d'entrée de FastAPI (422). Quand le serveur est arrêté, le client doit afficher son message d'API injoignable ; ce second cas reste à capturer.

![T32 : texte refusé](captures/tp5-t32-refus.png)

![T32 : API injoignable](captures/tp5-t32-injoignable.png)

### T33 · Un fichier d'avis

Onglet « Un fichier d'avis », fichier `data/avis_exemple.csv`, puis « Télécharger les résultats ».

**Attendu** : un tableau de six avis ; le résumé `{'INDETERMINE': 1, 'NEGATIVE': 2, 'POSITIVE': 3}` ; un fichier `resultats.csv` téléchargé.

**Obtenu** :

```text
`docs/semaine5.md` indique 6 avis dans le CSV et 1 abstention pour le modèle de démonstration. Le téléchargement réel du fichier `resultats.csv` n'a pas de capture archivée.
```

- [ ] Conforme

**Commentaire** (combien d'avis partent vers un humain, et lesquels ?) :

> Un avis part vers un humain selon le compte-rendu TP5. Le texte de l'avis et le téléchargement doivent être confirmés par une capture de la recette originale.

![T33 : le lot d'avis](captures/tp5-t33-lot.png)

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

- [ ] Conforme

**Commentaire** :

> Les réponses de semaine 5 sont rédigées et le push est confirmé. Le journal ne peut pas attester que l'onglet Actions est vert sans consulter l'exécution GitHub.

![T34 : la CI du TP5](captures/tp5-t34-actions.png)

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

- [ ] Conforme

![TP5 : poste du membre B](captures/tp5-membre-b.png)

---

## Les difficultés rencontrées

Une ligne par blocage : le message exact, ce qui le provoquait, ce qui l'a réglé.

| TP | Commande | Message | Cause | Solution |
| --- | --- | --- | --- | --- |
| Reprise 21/10/2026 | `pytest -q` | `UnicodeEncodeError: surrogates not allowed` | Hypothesis a généré le surrogate isolé `\ud800`, qui est renvoyé dans le détail 422 puis ne peut pas être encodé en UTF-8. | À corriger : exclure les non-scalaires Unicode de la stratégie ou normaliser la réponse de validation, puis rejouer la suite. |
| TP1 / reprise | `git shortlog -sn --all` | Trois libellés d'auteur au lieu de deux | `Mouad Salah` et `Mouad salah` diffèrent uniquement par la casse. | Harmoniser les identités Git des deux postes si les auteurs doivent être regroupés. |
| | | | | |

## La répartition du travail

| TP | Ce qu'a fait le membre A | Ce qu'a fait le membre B |
| --- | --- | --- |
| TP1 | Mouad : configuration de l'environnement Python 3.11, diagnostic de build et CI GitHub Actions. | Mounir : création du dépôt GitHub, cadrage multicritère des cas d'usage et structuration initiale de la documentation. |
| TP2 | Mouad : pipeline scikit-learn, entraînement sur le corpus Allociné et analyse qualitative des erreurs d'inférence. | Mounir : cadrage métier, validation des métriques de classification et du seuil F1 macro. |
| TP3 | Mouad : architecture FastAPI, schémas Pydantic et tests d'API (`test_api.py`). | Mounir : validation de `/health` et `/predict`, tests manuels Swagger et vérification du démarrage fail-fast. |
| TP4 | Mouad : tests limites et propriétés Hypothesis (`test_limites.py`), courbe de seuil, abstention à 0,60 et rédaction des rapports TP4. | Mounir : rédaction/annotation du jeu d'or, cas difficiles et erreurs connues, tests d'intégration et pannes 500, configuration de ruff, mypy et pre-commit. |
| TP5 | Mouad : installation du kit TP5, configuration de Streamlit dans la CI et recette des contrôles T29 à T31. | Mounir : recette des contrôles T32 et T33, ingestion par lot et export CSV, réponses dans `docs/semaine5.md`, mise à jour du journal T0-T34 et rapport TP5. |

## Le bilan

**TP1** :

> Le diagnostic de reprise passe, mais le test complet a révélé une erreur Unicode rare dans la propriété Hypothesis. Les sorties historiques de démarrage et les captures de TP1 ne sont pas conservées.

**TP2** :

> Le modèle de démonstration atteint un F1 macro de 0,879 sur 58 avis ; la courbe du seuil 0,60 envoie 16 avis à un humain et conserve 2 erreurs automatiques. Les sorties historiques Allociné du TP2 ne sont pas archivées dans le journal.

**TP3** :

> L'API expose `/health` et `/predict`, valide les entrées et démarre en échouant clairement si le modèle manque. Les requêtes positives et négatives ont renvoyé 200 lors de la reprise ; les sorties Swagger historiques ne sont pas archivées.

**TP4** :

> Les outils ruff et mypy passent, la couverture API atteint 97,67 % et le jeu d'or rend explicites 6 erreurs connues. Un cas Unicode isolé fait cependant échouer la suite complète et reste à corriger.

**TP5** :

> L'interface observée affiche les verdicts positifs/négatifs et l'abstention à 52 % ; les réponses TP5 sont documentées. Les captures de lot CSV et le statut Actions restent à confirmer.
