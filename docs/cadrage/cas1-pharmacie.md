# Fiche de cadrage : Ordonnances incomplètes en pharmacie

> Remplir chaque rubrique en une à trois phrases. Les rubriques marquées (obligatoire) sont vérifiées par `pytest`.

## Besoin en une phrase (obligatoire)

Détecter automatiquement les ordonnances médicales incomplètes ou non conformes avant la délivrance des médicaments au comptoir de la pharmacie.

## Utilisateur final (obligatoire)

Les pharmaciens et préparateurs en pharmacie, qui reçoivent une alerte de validation lors de la saisie de l'ordonnance dans leur logiciel d'officine.

## Approche retenue (obligatoire)

Cocher une seule case :

- [x] Règles métier
- [ ] Machine learning
- [ ] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)

(b) Les critères de validité d'une ordonnance sont strictement codifiés par la loi et les autorités sanitaires (présence du prescripteur, identifiant RPPS, date, signature, posologie) : la règle doit être déterministe et totalement vérifiable. (d) Une erreur de validation médicale engage directement la santé du patient et la responsabilité pénale du pharmacien, ce qui exclut les incertitudes d'un modèle statistique. (c) Le coût par requête est nul et le temps de réponse instantané au comptoir.

## Données nécessaires et leur origine (obligatoire)

Champs textuels et métadonnées de l'ordonnance issus de la saisie au logiciel de gestion d'officine (RPPS, date de prescription, identité du patient, lignes de médicaments) ; aucune donnée transmise à l'extérieur.

## Métrique de succès et seuil d'acceptation (obligatoire)

Taux de conformité des règles de 100 % et rappel de 1,00 sur la détection des champs manquants sur un jeu de test de 500 ordonnances synthétiques types.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)

En cas d'ordonnance signalée incomplète, le système bloque la délivrance et le pharmacien effectue une vérification manuelle auprès du médecin prescripteur avant validation définitive.

## Risques éthiques ou de confidentialité (obligatoire)

Traitement de données de santé hautement sensibles (soumises à la loi 09-08 / RGPD) : exécution strictement locale au sein du système d'information de l'officine sans transfert vers des serveurs tiers.

## Approche écartée et pourquoi (facultatif)

Modèle de machine learning ou LLM : écarté en raison du risque d'hallucination, du manque d'explicabilité juridique et de l'inutilité d'un modèle statistique pour des règles déterministes.
