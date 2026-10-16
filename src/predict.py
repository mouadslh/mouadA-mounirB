"""
Module de prédiction pour le modèle de sentiment.
Permet de prédire le sentiment d'un texte avec un score de confiance.
"""
from functools import lru_cache
from pathlib import Path
import joblib
import numpy as np

# Constantes
RACINE = Path(__file__).resolve().parent.parent
MODELE = RACINE / "models" / "sentiment.joblib"
# Seuil de décision : si P(positive) > SEUIL, alors positive, sinon negative
SEUIL_DECISION = 0.5  # Valeur standard, ajustable entre 0.4 et 0.6


@lru_cache(maxsize=1)
def charger_modele():
    """
    Charge le modèle entraîné (avec cache).

    Returns:
        Pipeline: Le modèle de classification

    Raises:
        FileNotFoundError: Si le modèle n'existe pas
    """
    if not MODELE.exists():
        raise FileNotFoundError(
            f"Le modèle {MODELE} n'existe pas.\n"
            f"Lancez d'abord : python src/train.py"
        )

    return joblib.load(MODELE)


def predict(texte, seuil=None):
    """
    Prédit le sentiment d'un texte.

    Args:
        texte: Le texte à analyser
        seuil: Seuil de décision personnalisé (optionnel, défaut: SEUIL_DECISION)
               Si P(positive) > seuil, alors positive, sinon negative

    Returns:
        dict: Dictionnaire avec les clés :
              - "label" : "positive" ou "negative"
              - "score" : score de confiance entre 0 et 1

    Raises:
        ValueError: Si le texte est vide ou n'est pas une chaîne
    """
    # Validation du texte
    if not isinstance(texte, str):
        raise ValueError("Le texte doit être une chaîne de caractères")

    if not texte or texte.strip() == "":
        raise ValueError("Le texte ne peut pas être vide")

    # Utiliser le seuil par défaut si non spécifié
    if seuil is None:
        seuil = SEUIL_DECISION

    # Charger le modèle
    pipeline = charger_modele()

    # Obtenir les probabilités
    probas = pipeline.predict_proba([texte])[0]

    # Identifier les indices des classes
    classes = pipeline.classes_
    idx_positive = np.where(classes == 'positive')[0][0]
    idx_negative = np.where(classes == 'negative')[0][0]

    proba_positive = probas[idx_positive]
    proba_negative = probas[idx_negative]

    # Décision basée sur le seuil
    if proba_positive > seuil:
        label = "positive"
        score = float(proba_positive)
    else:
        label = "negative"
        score = float(proba_negative)

    return {
        "label": label,
        "score": round(score, 4)
    }


def main():
    """Interface en ligne de commande."""
    import sys

    if len(sys.argv) < 2:
        print("Usage : python src/predict.py \"Votre texte à analyser\"")
        sys.exit(1)

    texte = " ".join(sys.argv[1:])

    try:
        resultat = predict(texte)
        print(f"\nTexte : {texte}")
        print(f"Sentiment : {resultat['label']}")
        print(f"Confiance : {resultat['score']:.4f}")
    except Exception as e:
        print(f"Erreur : {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
