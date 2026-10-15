# Semaine 2 : Analyse des erreurs

## Erreurs constatées

Le modèle commet environ 7 erreurs sur 58 avis de test (démo). En analysant la sortie de `evaluate.py`, on constate deux types d'erreurs :

1. **2 avis négatifs classés positifs** (erreur grave) : ce sont des avis négatifs manqués par le modèle, qui ne remonteront donc pas en priorité. Ces erreurs sont les plus problématiques pour le métier.

2. **5 avis positifs classés négatifs** (fausse alerte) : ces avis seront lus par un agent, mais sans conséquence négative réelle, juste un peu de temps perdu.

## Pourquoi ces erreurs ?

Le modèle utilise un **sac de mots** (TF-IDF) qui ne tient pas compte de l'ordre des phrases. Les avis mitigés qui commencent positivement mais finissent négativement (ou inversement) sont donc difficiles à classer correctement. Par exemple, un avis comme "Excellent produit au début, sauf que ensuite application qui plante" contient à la fois des mots positifs ("excellent", "produit") et négatifs ("plante"). Le modèle fait une moyenne du sentiment sans comprendre que la conclusion est négative.

Les n-grammes (1,2) capturent certaines expressions comme "très satisfait" ou "jamais reçue", mais ne suffisent pas pour les avis avec retournement de sentiment.

## Comment corriger ?

Plusieurs pistes pour améliorer le modèle :

1. **N-grammes plus longs** : passer à (1,3) pour capturer des expressions comme "mais finalement cassé" ou "sauf que ensuite plante".

2. **Modèle séquentiel** : utiliser un RNN, LSTM ou transformer (BERT, CamemBERT) qui comprend l'ordre des mots et peut détecter les retournements de sentiment.

3. **Plus de données mitigées** : enrichir le dataset avec davantage d'avis mitigés étiquetés selon leur conclusion pour que le modèle apprenne ce pattern.

4. **Seuil d'incertitude** : marquer les avis avec un score < 0,60 comme "à vérifier" pour qu'un agent humain les traite, réduisant ainsi l'impact des erreurs.
