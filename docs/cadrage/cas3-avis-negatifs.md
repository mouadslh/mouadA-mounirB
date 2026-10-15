# Cas 3 : Priorisation des avis négatifs

## Besoin métier

Une équipe relation client reçoit plusieurs milliers d'avis clients par jour. L'équipe souhaite traiter en priorité les avis négatifs pour répondre rapidement aux clients mécontents et limiter l'impact sur la réputation. Actuellement, les agents doivent parcourir manuellement tous les avis pour identifier les urgences, ce qui est chronophage et fait passer certains avis négatifs inaperçus. Le système doit automatiquement classer les avis et faire remonter les négatifs en tête de file.

## Approche IA proposée

- [x] Machine learning supervisé
- [ ] RAG (Retrieval-Augmented Generation)
- [ ] Génération par LLM sans contexte
- [ ] Système expert avec règles métier

## Critères de décision

**Critère (a) - Disponibilité des données étiquetées** : Les avis clients sont déjà étiquetés de manière implicite grâce aux notes attribuées par les clients (1-2 étoiles = négatif, 4-5 étoiles = positif). On dispose donc gratuitement d'un grand volume de données d'entraînement déjà étiquetées, ce qui rend le machine learning supervisé très pertinent.

**Critère (c) - Volume de données** : Le volume est élevé (milliers d'avis par jour), ce qui fournit suffisamment de données pour entraîner un modèle performant et le maintenir à jour avec de nouvelles données. Le ML supervisé excelle dans ce contexte de gros volumes.

**Critère (d) - Conséquence d'une erreur** : Une erreur de classification est peu grave. Si un avis négatif est classé positif (faux négatif), il sera traité avec un peu de retard mais ne sera pas perdu. Si un avis positif est classé négatif (faux positif), il sera lu par un agent mais sans conséquence négative. Le coût d'une erreur est acceptable, contrairement à un contexte médical ou financier.

## Limites et risques

Le modèle peut avoir des difficultés avec les avis mitigés (qui commencent positivement mais finissent négativement ou inversement), car il utilise un sac de mots qui ne capture pas l'ordre des phrases. L'ironie et le sarcasme sont également difficiles à détecter. Le modèle doit être ré-entraîné régulièrement pour s'adapter à l'évolution du vocabulaire des clients et aux nouveaux produits. Un seuil de confiance peut être défini pour marquer certains avis comme "à vérifier" quand le modèle hésite.
