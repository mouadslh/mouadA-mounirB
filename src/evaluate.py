"""
Script d'évaluation détaillée du modèle.
Affiche le rapport de classification, la matrice de confusion et des exemples d'erreurs.
"""
import argparse
import sys
from pathlib import Path
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# Ajouter le dossier src au path pour importer train
sys.path.insert(0, str(Path(__file__).resolve().parent))
from train import GRAINE, MODELE, charger_donnees


def evaluer_modele(utiliser_allocine=False):
    """
    Évalue le modèle de manière détaillée.
    
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
    
    # Charger les données (même découpage que pour l'entraînement)
    df, source = charger_donnees(utiliser_allocine)
    print(f"\nSource : {source}")
    
    X_train, X_test, y_train, y_test = train_test_split(
        df["review"],
        df["label"],
        test_size=0.2,
        random_state=GRAINE,
        stratify=df["label"]
    )
    
    # Prédictions
    print("\nÉvaluation sur l'ensemble de test...")
    y_pred = pipeline.predict(X_test)
    
    # Rapport de classification
    print("\n" + "=" * 60)
    print("RAPPORT DE CLASSIFICATION")
    print("=" * 60)
    print(classification_report(
        y_test, 
        y_pred, 
        target_names=["negative", "positive"],
        digits=3
    ))
    
    # Matrice de confusion
    print("=" * 60)
    print("MATRICE DE CONFUSION")
    print("=" * 60)
    cm = confusion_matrix(y_test, y_pred, labels=["negative", "positive"])
    print("\n              Prédit")
    print("              negative  positive")
    print(f"Vérité negative    {cm[0][0]:4d}      {cm[0][1]:4d}")
    print(f"       positive    {cm[1][0]:4d}      {cm[1][1]:4d}")
    
    # Analyse des erreurs
    print("\n" + "=" * 60)
    print("ANALYSE DES ERREURS")
    print("=" * 60)
    
    # Négatifs classés positifs (faux négatifs - erreur grave)
    negatifs_manques = cm[0][1]
    print(f"\nNégatifs classés positifs (erreur grave) : {negatifs_manques}")
    
    # Positifs classés négatifs (faux positifs - fausse alerte)
    fausses_alertes = cm[1][0]
    print(f"Positifs classés négatifs (fausse alerte) : {fausses_alertes}")
    
    total_erreurs = negatifs_manques + fausses_alertes
    print(f"\nTotal d'erreurs : {total_erreurs} sur {len(y_test)}")
    
    # Afficher des exemples d'erreurs
    print("\n" + "=" * 60)
    print("EXEMPLES D'ERREURS")
    print("=" * 60)
    
    erreurs = []
    for i, (vrai, predit, texte) in enumerate(zip(y_test, y_pred, X_test)):
        if vrai != predit:
            erreurs.append((vrai, predit, texte))
    
    # Afficher les 3 premiers exemples
    for i, (vrai, predit, texte) in enumerate(erreurs[:3], 1):
        texte_court = texte[:90] + "..." if len(texte) > 90 else texte
        print(f"\n{i}. Vérité : {vrai}")
        print(f"   Prédit : {predit}")
        print(f"   Texte : {texte_court}")


def main():
    """Fonction principale."""
    parser = argparse.ArgumentParser(
        description="Évalue le modèle de classification de sentiment"
    )
    parser.add_argument(
        "--allocine",
        action="store_true",
        help="Utilise le dataset Allociné au lieu des données de démo"
    )
    args = parser.parse_args()
    
    evaluer_modele(utiliser_allocine=args.allocine)


if __name__ == "__main__":
    main()
