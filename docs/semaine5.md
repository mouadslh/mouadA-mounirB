# Semaine 5 : l'interface, notes du binôme

> Trois questions, quelques phrases chacune. Répondez avec ce que vous avez observé.

## 1. Pourquoi l'interface n'importe-t-elle jamais `predict()` ni le fichier `.joblib` ?

L'interface envoie les avis au client HTTP, qui appelle l'API. Elle reste ainsi indépendante du fichier `.joblib` et du code d'entraînement ; le modèle peut être remplacé côté serveur sans changer la page.

## 2. Que montre l'interface quand le modèle hésite, et pourquoi est-ce mieux qu'un verdict forcé ?

Quand la confiance est sous le seuil de 0,60, l'API renvoie `INDETERMINE`. La page l'indique comme un cas à vérifier par un humain au lieu de forcer une réponse positive ou négative.

## 3. Que voit l'utilisateur quand l'API tombe ? Et le fichier `data/avis_exemple.csv` : combien d'avis partent vers un humain ?

Si l'API ne répond pas, la page affiche un message qui indique de démarrer `uvicorn api.main:app`. Le fichier `data/avis_exemple.csv` contient six avis ; sur le modèle de démonstration entraîné pour ce contrôle, un seul est envoyé à un humain.
