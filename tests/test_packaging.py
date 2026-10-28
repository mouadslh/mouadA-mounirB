"""Vérifications du paquet installable et de sa compatibilité historique (TP6)."""
import importlib
import tomllib
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


def test_version_est_unique_et_lue_par_pyproject():
    from sentiment_app import __version__

    config = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    assert __version__ == "0.6.0"
    assert config["project"]["dynamic"] == ["version"]
    assert config["tool"]["setuptools"]["dynamic"]["version"]["attr"] == (
        "sentiment_app.__version__"
    )


def test_commande_expose_version(capsys):
    from sentiment_app.cli import main

    with pytest.raises(SystemExit) as exit_info:
        main(["--version"])
    assert exit_info.value.code == 0
    assert capsys.readouterr().out.strip() == "sentiment-app 0.6.0"


def test_chemin_modele_est_configurable(monkeypatch, tmp_path):
    from sentiment_app import predict

    configured = tmp_path / "custom.joblib"
    monkeypatch.setenv("SENTIMENT_MODELE", str(configured))
    assert predict.chemin_modele() == configured


def test_ancien_import_et_nouveau_paquet_partagent_le_module():
    legacy = importlib.import_module("src.predict")
    packaged = importlib.import_module("sentiment_app.predict")
    assert legacy is packaged


def test_api_najoute_plus_src_au_chemin_python():
    source = (ROOT / "api" / "model.py").read_text(encoding="utf-8")
    assert "sys.path" not in source
    assert "sentiment_app.predict" in source


def test_roue_ne_declare_que_les_paquets_applicatifs():
    config = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    assert config["tool"]["setuptools"]["packages"] == ["sentiment_app", "api", "ui"]
    assert config["project"]["scripts"]["sentiment"] == "sentiment_app.cli:main"
    assert "scikit-learn>=1.5,<1.6" in config["project"]["dependencies"]

