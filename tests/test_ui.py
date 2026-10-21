"""
Tests des fonctions utilitaires de l'interface (sans lancer Streamlit).
3 tests avec un faux prédicteur.
"""
import sys
from pathlib import Path

import pandas as pd
import pytest

# Ajouter ui au path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "ui"))
from helpers import classer, predire_lot, resumer


# Faux prédicteur pour les tests
class FakePredicteur:
    """Faux prédicteur pour les tests."""
    
    @staticmethod
    def predict(texte):
        """Retourne un résultat prévisible selon le texte."""
        if "excellent" in texte.lower() or "satisfait" in texte.lower():
            return {"label": "positive", "score": 0.85}
        elif "mauvais" in texte.lower() or "décevant" in texte.lower():
            return {"label": "negative", "score": 0.90}
        else:
            return {"label": "positive", "score": 0.55}


def test_classer_ajoute_verdict():
    """La fonction classer doit ajouter les champs verdict et incertain."""
    fake_pred = FakePredicteur()
    
    # Cas avec bonne confiance
    resultat1 = classer("Excellent produit, très satisfait", fake_pred)
    assert "verdict" in resultat1
    assert "incertain" in resultat1
    assert resultat1["verdict"] == "positive"
    assert resultat1["incertain"] is False
    
    # Cas avec faible confiance (score 0.55 < 0.60)
    resultat2 = classer("Un produit quelconque", fake_pred)
    assert resultat2["verdict"] == "à vérifier"
    assert resultat2["incertain"] is True


def test_predire_lot_colonne_absente():
    """predire_lot doit lever KeyError si la colonne n'existe pas."""
    fake_pred = FakePredicteur()
    
    df = pd.DataFrame({
        "texte": ["Un avis"],
        "autre": ["Autre chose"]
    })
    
    with pytest.raises(KeyError, match="review"):
        predire_lot(df, fake_pred, colonne="review")


def test_predire_lot_ignore_lignes_vides():
    """predire_lot doit ignorer les lignes vides."""
    fake_pred = FakePredicteur()
    
    df = pd.DataFrame({
        "review": [
            "Excellent produit",
            "",
            None,
            "   ",
            "Mauvais produit"
        ]
    })
    
    resultat = predire_lot(df, fake_pred)
    
    # Seules 2 lignes doivent avoir une prédiction
    predictions_valides = resultat[resultat["prediction"] != ""]
    assert len(predictions_valides) == 2


def test_resumer_fichier_vide():
    """resumer doit gérer un DataFrame vide sans division par zéro."""
    df = pd.DataFrame({
        "prediction": ["", ""],
        "confiance": [0.0, 0.0],
        "verdict": ["", ""]
    })
    
    stats = resumer(df)
    
    assert stats["total"] == 0
    assert stats["negatifs"] == 0
    assert stats["part_negatifs"] == 0.0
    assert stats["a_verifier"] == 0
    assert stats["confiance_moyenne"] == 0.0
