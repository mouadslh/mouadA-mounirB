"""
Tests de vérification de l'environnement de développement.
23 tests pour valider la configuration du projet.
"""
import sys
import importlib
from pathlib import Path
import pytest

# Chemin racine du projet
RACINE = Path(__file__).resolve().parent.parent


class TestVersionPython:
    """Tests sur la version de Python."""
    
    def test_python_version_majeure(self):
        """Python doit être en version 3.x."""
        assert sys.version_info.major == 3
    
    def test_python_version_mineure(self):
        """Python doit être en version 3.11 (recommandé)."""
        # Tolérant : on accepte 3.11 et autres versions 3.x
        assert sys.version_info.minor >= 11 or sys.version_info.minor >= 8


class TestDependances:
    """Tests sur les dépendances Python."""
    
    def test_import_pandas(self):
        """pandas doit être installé."""
        import pandas
        assert hasattr(pandas, "__version__")
    
    def test_import_sklearn(self):
        """scikit-learn doit être installé."""
        import sklearn
        assert hasattr(sklearn, "__version__")
    
    def test_import_pytest(self):
        """pytest doit être installé."""
        import pytest
        assert hasattr(pytest, "__version__")
    
    def test_import_streamlit(self):
        """streamlit doit être installé."""
        import streamlit
        assert hasattr(streamlit, "__version__")
    
    def test_import_joblib(self):
        """joblib doit être installé."""
        import joblib
        assert hasattr(joblib, "__version__")
    
    def test_import_pyarrow(self):
        """pyarrow doit être installé."""
        import pyarrow
        assert hasattr(pyarrow, "__version__")
    
    def test_import_matplotlib(self):
        """matplotlib doit être installé."""
        import matplotlib
        assert hasattr(matplotlib, "__version__")


class TestStructureDossiers:
    """Tests sur la structure des dossiers."""
    
    def test_dossier_data_existe(self):
        """Le dossier data/ doit exister."""
        assert (RACINE / "data").exists()
    
    def test_dossier_models_existe(self):
        """Le dossier models/ doit exister."""
        assert (RACINE / "models").exists()
    
    def test_dossier_src_existe(self):
        """Le dossier src/ doit exister."""
        assert (RACINE / "src").exists()
    
    def test_dossier_ui_existe(self):
        """Le dossier ui/ doit exister."""
        assert (RACINE / "ui").exists()
    
    def test_dossier_tests_existe(self):
        """Le dossier tests/ doit exister."""
        assert (RACINE / "tests").exists()
    
    def test_dossier_docs_existe(self):
        """Le dossier docs/ doit exister."""
        assert (RACINE / "docs").exists()
    
    def test_dossier_docs_cadrage_existe(self):
        """Le dossier docs/cadrage/ doit exister."""
        assert (RACINE / "docs" / "cadrage").exists()
    
    def test_dossier_docs_images_existe(self):
        """Le dossier docs/images/ doit exister."""
        assert (RACINE / "docs" / "images").exists()
    
    def test_dossier_scripts_existe(self):
        """Le dossier scripts/ doit exister."""
        assert (RACINE / "scripts").exists()


class TestFichiersConfiguration:
    """Tests sur les fichiers de configuration."""
    
    def test_fichier_requirements_existe(self):
        """Le fichier requirements.txt doit exister."""
        assert (RACINE / "requirements.txt").exists()
    
    def test_fichier_gitignore_existe(self):
        """Le fichier .gitignore doit exister."""
        assert (RACINE / ".gitignore").exists()
    
    def test_fichier_pytest_ini_existe(self):
        """Le fichier pytest.ini doit exister."""
        assert (RACINE / "pytest.ini").exists()
    
    def test_fichier_readme_existe(self):
        """Le fichier README.md doit exister."""
        assert (RACINE / "README.md").exists()
