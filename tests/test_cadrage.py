"""
Tests de validation des fiches de cadrage.
12 tests pour vérifier la structure et le contenu des fiches.
"""
from pathlib import Path
import re
import pytest

RACINE = Path(__file__).resolve().parent.parent
DOSSIER_CADRAGE = RACINE / "docs" / "cadrage"

# Rubriques obligatoires dans chaque fiche
RUBRIQUES_OBLIGATOIRES = [
    "Besoin métier",
    "Approche IA proposée",
    "Critères de décision",
    "Limites et risques"
]


def lire_fiche(nom_fichier):
    """Lit le contenu d'une fiche de cadrage."""
    chemin = DOSSIER_CADRAGE / nom_fichier
    if not chemin.exists():
        pytest.skip(f"Fiche {nom_fichier} non trouvée")
    with open(chemin, "r", encoding="utf-8") as f:
        return f.read()


class TestFicheCas1:
    """Tests pour cas1-pharmacie.md."""
    
    def test_cas1_existe(self):
        """La fiche cas1-pharmacie.md doit exister."""
        assert (DOSSIER_CADRAGE / "cas1-pharmacie.md").exists()
    
    def test_cas1_rubriques_obligatoires(self):
        """La fiche cas1 doit contenir toutes les rubriques."""
        contenu = lire_fiche("cas1-pharmacie.md")
        for rubrique in RUBRIQUES_OBLIGATOIRES:
            assert rubrique in contenu, f"Rubrique '{rubrique}' manquante"
    
    def test_cas1_une_seule_case_cochee(self):
        """La fiche cas1 doit avoir exactement une case cochée."""
        contenu = lire_fiche("cas1-pharmacie.md")
        cases_cochees = re.findall(r"- \[x\]", contenu, re.IGNORECASE)
        assert len(cases_cochees) == 1, f"Trouvé {len(cases_cochees)} cases cochées au lieu de 1"
    
    def test_cas1_criteres_cites(self):
        """La fiche cas1 doit citer au moins deux critères (a) à (d)."""
        contenu = lire_fiche("cas1-pharmacie.md")
        criteres = re.findall(r"\([a-d]\)", contenu)
        assert len(criteres) >= 2, f"Seulement {len(criteres)} critères cités, au moins 2 requis"


class TestFicheCas2:
    """Tests pour cas2-reglement.md."""
    
    def test_cas2_existe(self):
        """La fiche cas2-reglement.md doit exister."""
        assert (DOSSIER_CADRAGE / "cas2-reglement.md").exists()
    
    def test_cas2_rubriques_obligatoires(self):
        """La fiche cas2 doit contenir toutes les rubriques."""
        contenu = lire_fiche("cas2-reglement.md")
        for rubrique in RUBRIQUES_OBLIGATOIRES:
            assert rubrique in contenu, f"Rubrique '{rubrique}' manquante"
    
    def test_cas2_une_seule_case_cochee(self):
        """La fiche cas2 doit avoir exactement une case cochée."""
        contenu = lire_fiche("cas2-reglement.md")
        cases_cochees = re.findall(r"- \[x\]", contenu, re.IGNORECASE)
        assert len(cases_cochees) == 1, f"Trouvé {len(cases_cochees)} cases cochées au lieu de 1"
    
    def test_cas2_criteres_cites(self):
        """La fiche cas2 doit citer au moins deux critères (a) à (d)."""
        contenu = lire_fiche("cas2-reglement.md")
        criteres = re.findall(r"\([a-d]\)", contenu)
        assert len(criteres) >= 2, f"Seulement {len(criteres)} critères cités, au moins 2 requis"


class TestFicheCas3:
    """Tests pour cas3-avis-negatifs.md."""
    
    def test_cas3_existe(self):
        """La fiche cas3-avis-negatifs.md doit exister."""
        assert (DOSSIER_CADRAGE / "cas3-avis-negatifs.md").exists()
    
    def test_cas3_rubriques_obligatoires(self):
        """La fiche cas3 doit contenir toutes les rubriques."""
        contenu = lire_fiche("cas3-avis-negatifs.md")
        for rubrique in RUBRIQUES_OBLIGATOIRES:
            assert rubrique in contenu, f"Rubrique '{rubrique}' manquante"
    
    def test_cas3_une_seule_case_cochee(self):
        """La fiche cas3 doit avoir exactement une case cochée."""
        contenu = lire_fiche("cas3-avis-negatifs.md")
        cases_cochees = re.findall(r"- \[x\]", contenu, re.IGNORECASE)
        assert len(cases_cochees) == 1, f"Trouvé {len(cases_cochees)} cases cochées au lieu de 1"
    
    def test_cas3_criteres_cites(self):
        """La fiche cas3 doit citer au moins deux critères (a) à (d)."""
        contenu = lire_fiche("cas3-avis-negatifs.md")
        criteres = re.findall(r"\([a-d]\)", contenu)
        assert len(criteres) >= 2, f"Seulement {len(criteres)} critères cités, au moins 2 requis"
