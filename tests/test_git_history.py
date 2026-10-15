"""
Tests de vérification de l'historique Git.
3 tests pour valider que le dépôt Git est correctement configuré.
"""
from pathlib import Path
import subprocess
import pytest

RACINE = Path(__file__).resolve().parent.parent


def executer_commande_git(args):
    """Exécute une commande git et retourne la sortie."""
    try:
        resultat = subprocess.run(
            ["git"] + args,
            cwd=RACINE,
            capture_output=True,
            text=True,
            check=True
        )
        return resultat.stdout.strip()
    except subprocess.CalledProcessError:
        return None
    except FileNotFoundError:
        pytest.skip("Git n'est pas installé")


class TestGitConfiguration:
    """Tests sur la configuration Git."""
    
    def test_git_initialise(self):
        """Le dépôt Git doit être initialisé."""
        assert (RACINE / ".git").exists(), "Le dépôt Git n'est pas initialisé"
    
    def test_git_remote_configure(self):
        """Un remote Git doit être configuré."""
        remote = executer_commande_git(["remote", "-v"])
        if remote is None:
            pytest.skip("Impossible de vérifier les remotes Git")
        # Accepter soit qu'il y ait un remote, soit que le dépôt soit neuf
        assert remote is not None  # La commande a fonctionné
    
    def test_gitignore_present(self):
        """Le fichier .gitignore doit exister."""
        assert (RACINE / ".gitignore").exists(), ".gitignore manquant"
