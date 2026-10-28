"""Contrats d'entrée et de sortie de l'API (Pydantic v2)."""
from typing import Literal

from pydantic import BaseModel, Field, field_validator

Label = Literal["POSITIVE", "NEGATIVE", "INDETERMINE"]


class PredictRequest(BaseModel):
    """Requête de prédiction."""
    text: str = Field(..., min_length=1, max_length=2000, description="Texte à classifier",
                      examples=["Livraison rapide, produit conforme, très satisfait"])

    @field_validator("text", mode="before")
    @classmethod
    def normaliser_unicode_non_scalar(cls, value: object) -> object:
        """Remplace les surrogates isolés, qui ne peuvent pas être encodés en UTF-8."""
        if isinstance(value, str):
            return value.encode("utf-8", errors="replace").decode("utf-8")
        return value

    @field_validator("text")
    @classmethod
    def texte_non_blanc(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Le texte ne peut pas être vide ou composé uniquement d'espaces")
        return value


class PredictResponse(BaseModel):
    """Réponse de prédiction."""
    label: Label = Field(..., description="POSITIVE, NEGATIVE ou INDETERMINE")
    score: float = Field(..., ge=0, le=1, description="Confiance de la classe prédite")
    text: str = Field(..., description="Aperçu du texte analysé (100 caractères)")


class HealthResponse(BaseModel):
    """Réponse de l'endpoint de santé."""
    status: str = Field(..., description="OK si le modèle est chargé")
    model: str = Field(..., description="Nom du modèle servi")


class ErrorResponse(BaseModel):
    """Format standard des erreurs FastAPI."""
    detail: str
