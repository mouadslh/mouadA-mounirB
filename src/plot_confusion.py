"""
Script de génération de la matrice de confusion visuelle.
Produit une image docs/images/matrice-confusion.png.
"""
import sys
from pathlib import Path
import joblib
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Ajouter le dossier src au path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from train import GRAINE, MODELE, charger_donnees

# Chemin de sortie
RACINE = Path(__file__).resolve().parent.parent
IMAGE_SORTIE = RACINE / "docs" / "images" / "matrice-confusion.png"


def generer_matrice_confusion(utiliser_allocine=False):
    """
    Génère et sauvegarde la matrice de confusion.
    
    Args:
        utiliser_allocine: Si True, utilise le dataset Allociné.
    """
    # Vérifier que le modèle existe
    if not MODELE.exists():
        raise FileNotFoundError(
            f"Le modèle {MODELE} n'existe pas.\n"
            f"Lancez d'abord : python src/train.py"
        )
    
    # Charger le modèle
    print("Chargement du modèle...")
    pipeline = joblib.load(MODELE)
    
    # Charger les données
    df, source = charger_donnees(utiliser_allocine)
    print(f"Source : {source}")
    
    # Même découpage que pour l'entraînement
    X_train, X_test, y_train, y_test = train_test_split(
        df["review"],
        df["label"],
        test_size=0.2,
        random_state=GRAINE,
        stratify=df["label"]
    )
    
    # Prédictions
    print("Génération des prédictions...")
    y_pred = pipeline.predict(X_test)
    
    # Créer la matrice de confusion
    cm = confusion_matrix(y_test, y_pred, labels=["negative", "positive"])
    
    # Visualisation
    print("Création de la visualisation...")
    fig, ax = plt.subplots(figsize=(8, 6))
    disp = ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=["Négatif", "Positif"]
    )
    disp.plot(ax=ax, cmap="Blues", values_format="d")
    
    ax.set_title("Matrice de confusion - Classification de sentiment", fontsize=14, pad=20)
    ax.set_xlabel("Prédiction", fontsize=12)
    ax.set_ylabel("Vérité", fontsize=12)
    
    # Sauvegarder
    IMAGE_SORTIE.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(IMAGE_SORTIE, dpi=150, bbox_inches="tight")
    print(f"\nImage sauvegardée : {IMAGE_SORTIE}")


def main():
    """Fonction principale."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Génère la matrice de confusion du modèle"
    )
    parser.add_argument(
        "--allocine",
        action="store_true",
        help="Utilise le dataset Allociné au lieu des données de démo"
    )
    args = parser.parse_args()
    
    generer_matrice_confusion(utiliser_allocine=args.allocine)


if __name__ == "__main__":
    main()
