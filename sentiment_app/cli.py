"""Interface en ligne de commande du paquet sentiment-app."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Sequence

from sentiment_app import __version__


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="sentiment", description="Analyse de sentiment des avis.")
    parser.add_argument("--version", action="version", version=f"sentiment-app {__version__}")
    commands = parser.add_subparsers(dest="command", required=True)

    prediction = commands.add_parser("predict", help="classer un avis")
    prediction.add_argument("text", nargs="+", help="texte de l'avis")

    commands.add_parser("serve", help="démarrer l'API FastAPI")
    commands.add_parser("ui", help="démarrer l'interface Streamlit")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.command == "predict":
        try:
            from api.model import load_model

            result = load_model().predict(" ".join(args.text))
        except FileNotFoundError as error:
            print(str(error), file=sys.stderr)
            return 1
        print(json.dumps(result, ensure_ascii=False))
        return 0

    if args.command == "serve":
        import uvicorn

        uvicorn.run("api.main:app", host="0.0.0.0", port=8000, log_level="info")
        return 0

    import streamlit.web.cli

    app_path = Path(__file__).resolve().parents[1] / "ui" / "app.py"
    sys.argv = ["streamlit", "run", str(app_path)]
    return int(streamlit.web.cli.main() or 0)

