"""Interface en ligne de commande du paquet sentiment-app."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Sequence

from sentiment_app import __version__


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="sentiment", description="Analyse de sentiment des avis.")
    parser.add_argument("--version", action="version", version=f"sentiment-app {__version__}")
    commands = parser.add_subparsers(dest="command", required=True)

    prediction = commands.add_parser("predict", help="classer un avis")
    prediction.add_argument("texte", nargs="+", help="texte de l'avis")

    server = commands.add_parser("serve", help="démarrer l'API FastAPI")
    server.add_argument("--host", default="127.0.0.1", help="adresse d'écoute")
    server.add_argument("--port", type=int, default=8000, help="port d'écoute")
    commands.add_parser("ui", help="démarrer l'interface Streamlit")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.command == "predict":
        try:
            from api.model import load_model

            result = load_model().predict(" ".join(args.texte))
        except FileNotFoundError as error:
            print(str(error), file=sys.stderr)
            return 1
        print(json.dumps(result, ensure_ascii=False))
        return 0

    if args.command == "serve":
        import uvicorn

        uvicorn.run("api.main:app", host=args.host, port=args.port)
        return 0

    try:
        import streamlit  # noqa: F401
    except ImportError:
        print(
            'Streamlit absent. Installez-le avec : pip install -e ".[ui]"',
            file=sys.stderr,
        )
        return 1

    app_path = Path(__file__).resolve().parents[1] / "ui" / "app.py"
    return subprocess.call([sys.executable, "-m", "streamlit", "run", str(app_path)])

