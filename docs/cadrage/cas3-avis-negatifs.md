# Fiche de cadrage : Priorisation des avis négatifs

> Remplir chaque rubrique en une à trois phrases. Les rubriques marquées (obligatoire) sont vérifiées par `pytest`.

## Besoin en une phrase (obligatoire)

Classifier automatiquement les avis clients entrants afin d'isoler et de traiter en priorité les insatisfactions critiques sur la plateforme e-commerce.

## Utilisateur final (obligatoire)

Les agents du service après-vente et des relations clients, qui reçoivent une file d'attente priorisée des avis nécessitant une intervention rapide.

## Approche retenue (obligatoire)

Cocher une seule case :

- [ ] Règles métier
- [x] Machine learning
- [ ] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)

(a) Le site dispose d'un volumineux historique d'avis clients déjà étiquetés par la note en étoiles (1 à 5) et par les actions antérieures du service client. (c) Avec des dizaines de milliers d'avis publiés quotidiennement, un modèle de classification de texte léger permet une inférence rapide à un coût de calcul négligeable par rapport à un LLM. (d) La conséquence d'une erreur de tri est faible, un avis mal classé étant simplement replacé dans la file normale sans risque vital ou financier direct.

## Données nécessaires et leur origine (obligatoire)

Base de données interne des avis clients (texte du commentaire, note attribuée, date, catégorie de produit) préalablement expurgée des informations personnelles (noms, adresses, numéros de commande).

## Métrique de succès et seuil d'acceptation (obligatoire)

F1-score macro d'au moins 0,85 avec un rappel d'au moins 0,92 sur la classe des avis très négatifs (1 et 2 étoiles) sur un jeu de test indépendant.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)

Un avis mal orienté peut être réassigné d'un clic par l'agent de support, et cette action alimente le jeu de données pour les futurs réentraînements du modèle.

## Risques éthiques ou de confidentialité (obligatoire)

Les commentaires peuvent contenir involontairement des données à caractère personnel (noms, téléphones) : pseudonymisation automatique à l'ingestion conformément au RGPD et à la loi 09-08.

## Approche écartée et pourquoi (facultatif)

Règles par mots-clés : approche trop rigide face aux fautes d'orthographe, au vocabulaire familier et au sarcasme fréquemment rencontrés dans les retours clients.
