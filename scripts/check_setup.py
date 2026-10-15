"""
Script de vérification de l'environnement de développement.
Vérifie que Python 3.11, les dépendances et la structure sont corrects.
"""
import sys
import importlib
from pathlib import Path

def verifier_version_python():
    """Vérifie que Python 3.11 est utilisé."""
    version = sys.version_info
    print(f"Version Python : {version.major}.{version.minor}.{version.micro}")
    if version.major != 3 or version.minor != 11:
        print("⚠️  Attention : Python 3.11 est recommandé")
        return False
    print("✓ Python 3.11 détecté")
    return True

def verifier_dependances():
    """Vérifie que les dépendances sont installées."""
    dependances = [
        "pandas",
        "sklearn",
        "pytest",
        "streamlit",
        "joblib",
        "pyarrow",
        "matplotlib"
    ]
    
    manquantes = []
    for dep in dependances:
        try:
            importlib.import_module(dep)
            print(f"✓ {dep} installé")
        except ImportError:
            print(f"✗ {dep} manquant")
            manquantes.append(dep)
    
    return len(manquantes) == 0

def verifier_structure():
    """Vérifie que la structure des dossiers existe."""
    dossiers = [
        "data",
        "models",
        "src",
        "ui",
        "tests",
        "docs",
        "docs/cadrage",
        "docs/images",
        "scripts"
    ]
    
    racine = Path(__file__).parent.parent
    manquants = []
    
    for dossier in dossiers:
        chemin = racine / dossier
        if chemin.exists():
            print(f"✓ {dossier}/ existe")
        else:
            print(f"✗ {dossier}/ manquant")
            manquants.append(dossier)
    
    return len(manquants) == 0

def main():
    """Fonction principale."""
    print("=" * 60)
    print("Vérification de l'environnement sentiment-app")
    print("=" * 60)
    
    print("\n1. Version Python")
    print("-" * 60)
    python_ok = verifier_version_python()
    
    print("\n2. Dépendances")
    print("-" * 60)
    deps_ok = verifier_dependances()
    
    print("\n3. Structure des dossiers")
    print("-" * 60)
    struct_ok = verifier_structure()
    
    print("\n" + "=" * 60)
    if python_ok and deps_ok and struct_ok:
        print("✓ Environnement prêt !")
    else:
        print("⚠️  Certaines vérifications ont échoué")
        sys.exit(1)
    print("=" * 60)

if __name__ == "__main__":
    main()
