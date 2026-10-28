"""Raccord entre l'API et le modèle fourni par le paquet installable."""
from typing import Literal, TypedDict

from sentiment_app.predict import charger_modele
from sentiment_app.predict import predict as _predict

Label = Literal["POSITIVE", "NEGATIVE", "INDETERMINE"]


class Prediction(TypedDict):
    label: Label
    score: float
    text: str


class SentimentClassifier:
    """Enveloppe du modèle TP2 avec l'interface attendue par l'API."""

    model_name = "tfidf-logreg (TP2, models/sentiment.joblib)"

    def __init__(self) -> None:
        pipeline = charger_modele()  # échoue immédiatement si le joblib manque
        classes = set(pipeline.classes_)
        if classes != {"positive", "negative"}:
            raise ValueError(f"Classes inattendues dans le modèle : {sorted(classes)}")

    def predict(self, text: str) -> Prediction:
        """Renvoie {'label': 'POSITIVE'|'NEGATIVE', 'score': float, 'text': aperçu}."""
        r = _predict(text)  # lève ValueError si le texte est vide
        correspondance: dict[str, Label] = {"positive": "POSITIVE", "negative": "NEGATIVE"}
        label = correspondance[r["label"]]
        if r["score"] < SEUIL_ABSTENTION:
            label = "INDETERMINE"
        return {"label": label, "score": r["score"], "text": text[:100]}


SEUIL_ABSTENTION = 0.60


def load_model() -> SentimentClassifier:
    """Construit le classifier (le cache de chargement est dans src/predict.py)."""
    return SentimentClassifier()
