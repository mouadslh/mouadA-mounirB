"""Prédiction de sentiment et chargement du modèle configurable."""
from __future__ import annotations

import os
import sys
from functools import lru_cache
from pathlib import Path
from typing import Literal, TypedDict

import joblib

RACINE = Path(__file__).resolve().parents[1]


def chemin_modele() -> Path:
    """Renvoie SENTIMENT_MODELE ou le modèle associé à l'installation."""
    return Path(os.environ.get("SENTIMENT_MODELE") or RACINE / "models" / "sentiment.joblib")


MODELE = chemin_modele()
Label = Literal["positive", "negative"]


class Prediction(TypedDict):
    label: Label
    score: float


@lru_cache(maxsize=1)
def charger_modele():
    """Charge le modèle une seule fois par processus."""
    if not MODELE.exists():
        raise FileNotFoundError(
            f"modèle introuvable : {MODELE}. "
            "Lancez python src/train.py ou définissez SENTIMENT_MODELE."
        )
    return joblib.load(MODELE)


def predict(texte: str) -> Prediction:
    """Renvoie l'étiquette et la confiance de l'avis."""
    if not isinstance(texte, str) or not texte.strip():
        raise ValueError("texte vide")
    pipeline = charger_modele()
    etiquette: Label = pipeline.predict([texte])[0]
    score = float(pipeline.predict_proba([texte]).max())
    return {"label": etiquette, "score": round(score, 4)}


def main() -> int:
    """Compatibilité avec l'ancienne commande ``python src/predict.py``."""
    if len(sys.argv) < 2:
        print('Usage : python src/predict.py "texte à analyser"')
        return 2
    resultat = predict(" ".join(sys.argv[1:]))
    print(f"{resultat['label']} (confiance {resultat['score']:.0%})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
