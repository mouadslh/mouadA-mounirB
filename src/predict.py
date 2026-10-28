"""Compatibilité avec les imports du TP2 et la commande historique.

Le module est aliasé vers ``sentiment_app.predict`` afin que son cache et ses
variables (notamment MODELE dans les anciens tests) restent partagés.
"""
import importlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

_module = importlib.import_module("sentiment_app.predict")

if __name__ == "__main__":
    raise SystemExit(_module.main())

sys.modules[__name__] = _module
