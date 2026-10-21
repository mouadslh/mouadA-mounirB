# Semaine 4 : tests approfondis et qualité

## 1. Couverture

Le relevé initial T21 n'a pas été fait avant l'ajout des tests. Après corrections, les contrôles exécutés localement donnent **97,67 %** de couverture sur `api/` (86 instructions, 2 manquantes). Les seules lignes non couvertes sont 83–85 de `api/main.py`, le bloc de lancement direct Uvicorn sous `if __name__ == "__main__"`; les tests démarrent l'application avec `TestClient`.

## 2. Défauts trouvés

| Symptôme | Test qui l'a révélé | Correction |
| --- | --- | --- |
| Un avis composé d'espaces passait la contrainte `min_length`, puis recevait un 422 d'une forme différente. | Cas paramétré et propriété Hypothesis dans `tests/test_limites.py`. | Validateur Pydantic fondé sur `str.strip()`, qui renvoie les erreurs standard en liste. |
| Une exception `ValueError` levée par le modèle était interprétée comme une erreur d'entrée 422. | `test_panne_modele_repond_500_sans_detail_interne`. | Toutes les pannes internes du modèle renvoient 500 sans exposer le détail. |
| Le modèle a classé franchement quatre avis du jeu d'or à l'encontre de leur étiquette. | `tests/test_jeu_or.py`. | Avis conservés et erreurs observées déclarées en `xfail(strict=True)` avec leur raison. |
| Un modèle contenant des classes inattendues pouvait être chargé. | `test_classes_inattendues_refusent_le_demarrage`. | Vérification explicite des classes au démarrage. |

## 3. Seuil d'abstention

La courbe a été calculée sur les 58 avis de test du jeu de démonstration :

| Seuil | Réponses automatiques | Exactitude de ces réponses | Erreurs | Vers un humain |
| --- | ---: | ---: | ---: | ---: |
| 0,50 | 58 (100 %) | 0,879 | 7 | 0 |
| 0,60 | 42 (72 %) | 0,952 | 2 | 16 (28 %) |
| 0,75 | 29 (50 %) | 1,000 | 0 | 29 (50 %) |

Le seuil conservé est **0,60** : 16 avis sont redirigés vers un humain et 5 erreurs automatiques sont évitées par rapport au seuil 0,50.

## 4. Jeu d'or

Le jeu de contrôle contient 21 avis, dont au moins cinq cas difficiles. Après réalignement sur le TP2 du cours, le résultat est **7 justes, 8 abstentions et 6 erreurs franches déclarées** (`xfail(strict=True)`). Ces avis sont un jeu de contrôle préparé pour ce dépôt et doivent être relus/validés par le binôme avant remise. Les erreurs connues restent visibles au lieu d'être retirées du jeu.

## 5. Outils statiques

Avant correction, `ruff check .` relevait 25 remarques et `mypy api` relevait 2 erreurs de types. Après correction, `ruff check .` affiche `All checks passed!` et `mypy api` affiche `Success: no issues found in 4 source files`. Les outils statiques ont notamment relevé les imports désordonnés, quelques constructions risquées et les types trop larges sur les étiquettes.

## Contrôle automatisé final

`python -m pytest -q --cov=api --cov-report=term-missing --cov-fail-under=95` : **97 passed, 6 xfailed**, couverture totale de l'API **97,67 %**. L'avertissement restant vient de Starlette/AnyIO et n'affecte pas les résultats.
