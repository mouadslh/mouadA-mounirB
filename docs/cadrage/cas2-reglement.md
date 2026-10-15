# Cas 2 : Assistant règlement intérieur

## Besoin métier

Une entreprise de 500 employés souhaite développer un assistant IA pour répondre aux questions courantes sur le règlement intérieur : congés, télétravail, horaires, procédures RH. Les employés passent actuellement par les RH pour des questions simples, ce qui surcharge le service. L'assistant doit pouvoir répondre à des questions comme "Combien de jours de télétravail ai-je droit ?" ou "Quelle est la procédure pour poser un congé exceptionnel ?".

## Approche IA proposée

- [ ] Machine learning supervisé
- [x] RAG (Retrieval-Augmented Generation)
- [ ] Génération par LLM sans contexte
- [ ] Système expert avec règles métier

## Critères de décision

**Critère (b) - Explicabilité** : Le système doit pouvoir citer l'article exact du règlement intérieur pour justifier sa réponse. Les employés et les RH ont besoin de connaître la source de l'information pour s'assurer de sa validité. Le RAG permet de retrouver et citer automatiquement l'article pertinent.

**Critère (a) - Disponibilité des données étiquetées** : Il n'existe pas de dataset de questions-réponses déjà étiquetées sur ce règlement intérieur spécifique. Le RAG permet d'exploiter directement le document du règlement sans passer par une phase d'annotation coûteuse.

**Critère (c) - Volume de données** : Le volume de questions est relativement faible (quelques centaines par mois maximum), et le règlement intérieur est un document de taille modeste (quelques dizaines de pages). Le RAG est adapté à ce contexte où l'on a peu de données d'entraînement mais un document de référence bien structuré.

## Limites et risques

Le règlement intérieur doit être à jour dans la base documentaire, sinon l'assistant donnera des informations obsolètes. Certaines questions peuvent nécessiter une interprétation humaine (cas particuliers, exceptions), et le système doit alors rediriger vers les RH. Il faut veiller à ce que le retrieval soit assez fin pour distinguer des articles similaires (par exemple, congés payés vs. congés exceptionnels). Le découpage du document en chunks doit être soigneusement conçu pour ne pas couper les articles en milieu de phrase.
