"""Vérifie le contenu essentiel d'une roue construite pour le TP6."""
from __future__ import annotations

import sys
from pathlib import Path
from zipfile import ZipFile


def main() -> int:
    wheels = sorted((Path(__file__).resolve().parents[1] / "dist").glob("*.whl"))
    if len(wheels) != 1:
        print(f"Attendu : une roue dans dist/, trouvé {len(wheels)}.", file=sys.stderr)
        return 1

    with ZipFile(wheels[0]) as wheel:
        files = wheel.namelist()
    packages = {name.split("/", maxsplit=1)[0] for name in files if "/" in name}
    required = {"sentiment_app", "api", "ui"}
    forbidden = {"tests", "data", "models", "src"}
    missing = required - packages
    included = forbidden & packages
    if missing or included:
        print(f"Paquets absents : {sorted(missing)}; contenus interdits : {sorted(included)}.")
        return 1
    print(f"Roue valide : {wheels[0].name}; paquets {', '.join(sorted(required))}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
