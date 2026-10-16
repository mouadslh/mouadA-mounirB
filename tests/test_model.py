"""
Tests du modèle de classification.
4 tests : 2 sur les métriques (en CI), 2 sur les prédictions (skip si modèle absent).
"""
import json
from pathlib import Path
import pytest

# Chemins
RACINE = Path(__file__).resolve().parent.parent
METRIQUES = RACINE / "models" / "metrics.json"
MODELE = RACINE / "models" / "sentiment.joblib"


class TestMetriques:
    """Tests sur les métriques sauvegardées."""
    
    def test_fichier_metriques_existe(self):
        """Le fichier metrics.json doit exister."""
        assert METRIQUES.exists(), f"{METRIQUES} n'existe pas"
    
    def test_structure_metriques(self):
        """Le fichier metrics.json doit contenir toutes les clés requises."""
        with open(METRIQUES, "r", encoding="utf-8") as f:
            metriques = json.load(f)
        
        # Clés obligatoires
        cles_requises = {
            "source",
            "date",
            "n_train",
            "n_test",
            "f1_macro",
            "accuracy",
            "recall_negative",
            "seuil_f1"
        }
        
        cles_presentes = set(metriques.keys())
        assert cles_requises.issubset(cles_presentes), \
            f"Clés manquantes : {cles_requises - cles_presentes}"
    
    def test_seuil_f1_atteint(self):
        """Le F1-score doit être supérieur ou égal au seuil."""
        with open(METRIQUES, "r", encoding="utf-8") as f:
            metriques = json.load(f)
        
        f1 = metriques["f1_macro"]
        seuil = metriques["seuil_f1"]
        
        assert f1 >= seuil, \
            f"F1-score {f1} inférieur au seuil {seuil}"


class TestPredictions:
    """Tests sur le module de prédiction."""
    
    @pytest.mark.skipif(
        not MODELE.exists(),
        reason="Modèle non entraîné (lancez python src/train.py)"
    )
    def test_predictions_evidentes(self):
        """Le modèle doit correctement classer des avis évidents."""
        from src.predict import predict
        
        # Avis clairement positif
        resultat_pos = predict("Excellent produit, très satisfait, je recommande")
        assert resultat_pos["label"] == "positive", \
            "Avis positif mal classé"
        
        # Avis clairement négatif
        resultat_neg = predict("Produit cassé, service horrible, très déçu")
        assert resultat_neg["label"] == "negative", \
            "Avis négatif mal classé"
    
    @pytest.mark.skipif(
        not MODELE.exists(),
        reason="Modèle non entraîné (lancez python src/train.py)"
    )
    def test_format_sortie_predict(self):
        """La fonction predict doit retourner le bon format."""
        from src.predict import predict
        
        resultat = predict("Un texte quelconque pour tester")
        
        # Vérifier les clés
        assert set(resultat.keys()) == {"label", "score"}, \
            "Format de sortie incorrect"
        
        # Vérifier les types et valeurs
        assert resultat["label"] in ["positive", "negative"], \
            "Label invalide"
        
        assert isinstance(resultat["score"], float), \
            "Le score doit être un float"
        
        assert 0 <= resultat["score"] <= 1, \
            "Le score doit être entre 0 et 1"
    
    @pytest.mark.skipif(
        not MODELE.exists(),
        reason="Modèle non entraîné (lancez python src/train.py)"
    )
    def test_erreur_texte_vide(self):
        """predict doit lever ValueError sur texte vide."""
        from src.predict import predict
        
        with pytest.raises(ValueError, match="vide"):
            predict("   ")
