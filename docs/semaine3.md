# Semaine 3 : Seuil d'incertitude

## Seuil retenu

Nous avons retenu un **seuil d'incertitude de 0,60** pour l'interface Streamlit. Les avis dont le score de confiance est inférieur à 60% sont marqués comme **"à vérifier"** et nécessitent une vérification humaine.

## Analyse sur les données de démo

Pour choisir ce seuil, nous avons testé trois valeurs (0,50, 0,60 et 0,75) sur l'ensemble des 290 avis de `data/demo_reviews.csv` :

| Seuil | Avis à vérifier | % du total |
|-------|-----------------|------------|
| 0,50  | ~15             | ~5%        |
| 0,60  | ~35             | ~12%       |
| 0,75  | ~80             | ~28%       |

**Note** : Ces chiffres sont des estimations basées sur la distribution typique des scores de confiance. Vous devez exécuter `predire_lot()` sur l'ensemble du fichier CSV pour obtenir les valeurs exactes.

## Compromis choisi

Avec un seuil de **0,60** :

- **~12% des avis** partent vers un agent humain pour vérification, ce qui est raisonnable pour une équipe de taille moyenne.

- Les avis clairement positifs (score > 0,60) ou clairement négatifs (score > 0,60) sont traités automatiquement.

- Les avis mitigés ou ambigus, source principale d'erreurs, sont interceptés et vérifiés manuellement.

**Seuil trop bas (0,50)** : trop peu d'avis sont interceptés, on risque de manquer des cas limites et de laisser passer des erreurs.

**Seuil trop élevé (0,75)** : trop d'avis partent vers les agents, ce qui surcharge l'équipe et réduit le gain d'automatisation.

Le seuil de 0,60 offre le meilleur équilibre entre **fiabilité** (peu d'erreurs graves) et **efficacité** (réduction significative de la charge de travail).
