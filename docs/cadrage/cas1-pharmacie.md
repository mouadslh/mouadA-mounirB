# Cas 1 : Chatbot conseil en pharmacie

## Besoin métier

Une pharmacie souhaite déployer un chatbot pour conseiller les clients sur les médicaments en vente libre, les posologies et les interactions médicamenteuses courantes. Le système doit pouvoir répondre à des questions comme "Puis-je prendre ce médicament avec mon traitement actuel ?" ou "Quelle dose pour un enfant de 6 ans ?". L'objectif est de soulager les pharmaciens des questions de base tout en maintenant un niveau de conseil fiable et sécurisé.

## Approche IA proposée

- [ ] Machine learning supervisé
- [x] RAG (Retrieval-Augmented Generation)
- [ ] Génération par LLM sans contexte
- [ ] Système expert avec règles métier

## Critères de décision

**Critère (b) - Explicabilité** : Le système doit pouvoir justifier ses réponses en citant les sources médicales utilisées (notice officielle, base de données médicamenteuse). Le RAG permet de retrouver les passages pertinents dans la documentation et de les citer, ce qui est essentiel pour la confiance des utilisateurs.

**Critère (a) - Disponibilité des données étiquetées** : Il n'existe pas de dataset pré-étiqueté de questions-réponses pharmaceutiques spécifiques à cette pharmacie. Le RAG permet d'exploiter directement la documentation existante (notices, bases médicamenteuses) sans avoir besoin d'étiqueter des milliers d'exemples.

**Critère (d) - Conséquence d'une erreur** : Une erreur grave (mauvais conseil sur une interaction médicamenteuse) peut avoir des conséquences sanitaires sérieuses. Le RAG limite les hallucinations en ancrant les réponses dans des documents vérifiés, et permet à un pharmacien de vérifier rapidement la source citée.

## Limites et risques

Le système doit être configuré avec un seuil de confiance élevé : en cas de doute, il doit rediriger vers un pharmacien humain. Les documents sources (notices, bases de données) doivent être maintenus à jour régulièrement. Le RAG ne remplace pas un diagnostic médical et doit toujours inclure un avertissement invitant à consulter un professionnel en cas de symptômes graves. Risque de retrieval incomplet si la base documentaire est mal indexée.
