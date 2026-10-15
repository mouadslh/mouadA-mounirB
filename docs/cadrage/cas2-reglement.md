# Fiche de cadrage : Questions sur le règlement intérieur

> Remplir chaque rubrique en une à trois phrases. Les rubriques marquées (obligatoire) sont vérifiées par `pytest`.

## Besoin en une phrase (obligatoire)

Permettre aux étudiants et au personnel d'obtenir des réponses instantanées, fiables et sourcées à leurs questions sur le règlement intérieur de l'école.

## Utilisateur final (obligatoire)

Les étudiants, enseignants et membres du personnel administratif de l'établissement cherchant à clarifier une règle ou une procédure scolaire.

## Approche retenue (obligatoire)

Cocher une seule case :

- [ ] Règles métier
- [ ] Machine learning
- [x] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)

(a) Il n'existe pas d'historique volumineux de questions étiquetées pour entraîner un modèle supervisé, mais les documents de référence existent déjà sous forme textuelle. (b) Chaque réponse doit être parfaitement vérifiable en citant obligatoirement le numéro de l'article et la section exacte du règlement officiel. (d) Une réponse erronée ou hallucinée sur une sanction ou un délai d'absence peut pénaliser l'étudiant ; l'ancrage documentaire du RAG garantit la conformité de l'information.

## Données nécessaires et leur origine (obligatoire)

Corpus des règlements officiels de l'établissement (règlement intérieur, charte informatique, modalités de contrôle des connaissances) segmenté en passages textuels indexés avec leurs métadonnées.

## Métrique de succès et seuil d'acceptation (obligatoire)

Taux de citation exacte de la source documentaire supérieur à 95 % et score de fidélité factuelle (faithfulness) supérieur à 0,90 sur un banc d'essai de 100 questions d'évaluation.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)

L'extrait officiel cité est affiché directement sous la réponse pour permettre à l'usager de vérifier la règle originale, et un lien permet d'escalader la question au secrétariat pédagogique en cas de doute.

## Risques éthiques ou de confidentialité (obligatoire)

Les questions posées par les étudiants peuvent contenir des données personnelles ou médicales : filtrage des informations identifiantes avant traitement et politique stricte de non-conservation des requêtes.

## Approche écartée et pourquoi (facultatif)

Modèle génératif seul : rejeté car il présente un risque élevé d'hallucination et ne permet pas d'attester de la source exacte des règles en vigueur.
