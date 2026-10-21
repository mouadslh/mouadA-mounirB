"""Tests d'intégration : l'API telle qu'elle tourne vraiment (TP4, étape D). À COMPLÉTER.

Les tests du TP3 vérifient des réponses ; ceux-ci vérifient le démarrage de l'API
et son comportement quand le modèle manque ou tombe en panne.
"""
from importlib import reload
from pathlib import Path

import pytest

MODELE = Path(__file__).resolve().parents[1] / "models" / "sentiment.joblib"
pytestmark = pytest.mark.skipif(not MODELE.exists(), reason="modèle non produit : python src/train.py")


def test_demarrage_reel_charge_le_modele():
    """D.1 (donné en exemple) : un client ouvert par « with » exécute le lifespan."""
    from fastapi.testclient import TestClient

    from api.main import app

    with TestClient(app) as client:
        reponse = client.get("/health")
    assert reponse.status_code == 200
    assert "TP2" in reponse.json()["model"]


def test_modele_absent_refuse_le_demarrage(monkeypatch, tmp_path):
    from fastapi.testclient import TestClient

    from api.main import app
    from src import predict

    monkeypatch.setattr(predict, "MODELE", tmp_path / "absent.joblib")
    predict.charger_modele.cache_clear()
    with pytest.raises(FileNotFoundError):
        with TestClient(app):
            pass
    predict.charger_modele.cache_clear()


def test_modele_non_charge_repond_503(monkeypatch):
    from fastapi.testclient import TestClient

    from api.main import app

    with TestClient(app) as client:
        monkeypatch.setattr(app.state, "classifier", None)
        assert client.get("/health").status_code == 503
        assert client.post("/predict", json={"text": "Très bien"}).status_code == 503


@pytest.mark.parametrize("exception", [RuntimeError("panne"), ValueError("bug interne")])
def test_panne_modele_repond_500_sans_detail_interne(monkeypatch, exception):
    from fastapi.testclient import TestClient

    from api.main import app

    class ModeleEnPanne:
        model_name = "modele de test"

        def predict(self, text):
            raise exception

    with TestClient(app) as client:
        monkeypatch.setattr(app.state, "classifier", ModeleEnPanne())
        reponse = client.post("/predict", json={"text": "Très bien"})
    assert reponse.status_code == 500
    assert "bug interne" not in reponse.text
    assert "panne" not in reponse.text


def test_classes_inattendues_refusent_le_demarrage(monkeypatch):
    from fastapi.testclient import TestClient

    import api.model as module
    from api.main import app

    class PipelineInattendu:
        classes_ = ["negative", "neutral", "positive"]

    monkeypatch.setattr(module, "charger_modele", lambda: PipelineInattendu())
    with pytest.raises(ValueError, match="Classes inattendues"):
        with TestClient(app):
            pass


def test_adaptateur_retourne_label_et_abstention():
    import api.model as module

    module = reload(module)
    classifier = module.SentimentClassifier()
    assert classifier.predict("Très satisfait, excellent produit")['label'] in {
        "POSITIVE", "NEGATIVE", "INDETERMINE"
    }
    assert classifier.predict("xqzvb wlkptr grombu")['label'] == "INDETERMINE"


# À écrire (étape D) :
# D.2 modèle absent : chemin du modèle redirigé (monkeypatch), cache vidé
#     (charger_modele.cache_clear()), l'API refuse de démarrer (FileNotFoundError) ;
# D.3 modèle non chargé : l'API démarrée, modèle retiré de app.state, 503 sur /health et /predict ;
# D.4 modèle en panne : predict lève RuntimeError, puis ValueError("bug interne") :
#     500 dans les deux cas, sans le message interne dans la réponse.
# Utilisez monkeypatch.setattr pour toute modification : il restaure l'état à la fin du test.
