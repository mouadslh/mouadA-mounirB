"""
Script d'entraînement du modèle de classification de sentiment.
Supporte deux sources de données : démo locale ou dataset Allociné.
"""
import argparse
import json
from datetime import datetime
from pathlib import Path
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import f1_score, accuracy_score, recall_score

# Constantes
RACINE = Path(__file__).resolve().parent.parent
DEMO = RACINE / "data" / "demo_reviews.csv"
MODELE = RACINE / "models" / "sentiment.joblib"
METRIQUES = RACINE / "models" / "metrics.json"
SEUIL_F1 = 0.85
GRAINE = 42
URL_ALLOCINE = "https://huggingface.co/datasets/tblard/allocine/resolve/main/allocine/validation-00000-of-00001.parquet"


def charger_donnees(utiliser_allocine=False):
    """
    Charge les données d'entraînement.

    Args:
        utiliser_allocine: Si True, télécharge et charge le dataset Allociné.
                            Sinon, charge le fichier de démonstration local.

    Returns:
        tuple: (DataFrame avec colonnes 'review' et 'label', nom de la source)
    """
    if utiliser_allocine:
        print("Téléchargement du dataset Allociné...")
        df = pd.read_parquet(URL_ALLOCINE)

        # Identifier la colonne contenant le texte de la critique
        if "text" in df.columns:
            df["review"] = df["text"]
        elif "content" in df.columns:
            df["review"] = df["content"]
        elif "review" not in df.columns:
            # Si aucune des colonnes habituelles n'est trouvée, prendre la première colonne textuelle
            text_cols = [col for col in df.columns if col != "label"]
            if text_cols:
                df["review"] = df[text_cols[0]]

        # Conversion des étiquettes : 0 -> negative, 1 -> positive (si la colonne label est numérique)
        if "label" in df.columns and df["label"].dtype in [int, float, "int64", "float64"]:
            df["label"] = df["label"].map({0: "negative", 1: "positive"})

        df = df[["review", "label"]].dropna()

        source = "allocine"
    else:
        # Charger le fichier de démonstration
        if not DEMO.exists():
            raise FileNotFoundError(
                f"Le fichier {DEMO} n'existe pas.\n"
                f"Lancez d'abord : python src/make_demo.py"
            )

        df = pd.read_csv(DEMO, encoding="utf-8")
        source = "demo"

    return df, source


def construire_pipeline():
    """
    Construit le pipeline de classification.

    Returns:
        Pipeline: Pipeline TF-IDF + Régression Logistique
    """
    return Pipeline([
        ("tfidf", TfidfVectorizer(
            ngram_range=(1, 2),
            min_df=2,
            max_df=0.95,  # Ignorer les mots trop fréquents
            sublinear_tf=True,
            lowercase=True,
            strip_accents='unicode'  # Normaliser les accents
        )),
        ("clf", LogisticRegression(
            max_iter=1000,
            class_weight="balanced",
            random_state=GRAINE,
            C=1.0,  # Régularisation par défaut
            solver='lbfgs'  # Solveur plus stable
        ))
    ])


def entrainer_modele(utiliser_allocine=False):
    """
    Entraîne le modèle et sauvegarde les résultats.

    Args:
        utiliser_allocine: Si True, utilise le dataset Allociné.
    """
    # Chargement des données
    df, source = charger_donnees(utiliser_allocine)
    print(f"\nSource : {source}")
    print(f"Nombre total d'avis : {len(df)}")

    nb_negatifs = (df["label"] == "negative").sum()
    print(f"  dont {nb_negatifs} négatifs")

    # Découpage train/test AVANT toute vectorisation
    X_train, X_test, y_train, y_test = train_test_split(
        df["review"],
        df["label"],
        test_size=0.2,
        random_state=GRAINE,
        stratify=df["label"]
    )

    print(f"\nDécoupage : {len(X_train)} train, {len(X_test)} test")

    # Construction et entraînement du pipeline
    print("\nEntraînement du modèle...")
    pipeline = construire_pipeline()
    pipeline.fit(X_train, y_train)

    # Afficher la taille du vocabulaire
    taille_vocab = len(pipeline.named_steps["tfidf"].vocabulary_)
    print(f"Taille du vocabulaire : {taille_vocab} termes")

    # Évaluation
    y_pred = pipeline.predict(X_test)
    f1_macro = f1_score(y_test, y_pred, average="macro")
    accuracy = accuracy_score(y_test, y_pred)
    recall_neg = recall_score(y_test, y_pred, pos_label="negative")

    print(f"\nRésultats :")
    print(f"  F1-score macro : {f1_macro:.4f}")
    print(f"  Accuracy : {accuracy:.4f}")
    print(f"  Recall négatifs : {recall_neg:.4f}")
    print(f"  Seuil requis : {SEUIL_F1}")

    if f1_macro >= SEUIL_F1:
        print("✓ Seuil F1 atteint")
    else:
        print("⚠ Seuil F1 non atteint")

    # Sauvegarde du modèle
    MODELE.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipeline, MODELE)
    print(f"\nModèle sauvegardé : {MODELE}")

    # Sauvegarde des métriques
    metriques = {
        "source": source,
        "date": datetime.now().isoformat(),
        "n_train": len(X_train),
        "n_test": len(X_test),
        "f1_macro": round(f1_macro, 4),
        "accuracy": round(accuracy, 4),
        "recall_negative": round(recall_neg, 4),
        "seuil_f1": SEUIL_F1
    }

    with open(METRIQUES, "w", encoding="utf-8") as f:
        json.dump(metriques, f, indent=2, ensure_ascii=False)

    print(f"Métriques sauvegardées : {METRIQUES}")


def main():
    """Fonction principale."""
    parser = argparse.ArgumentParser(
        description="Entraîne le modèle de classification de sentiment"
    )
    parser.add_argument(
        "--allocine",
        action="store_true",
        help="Utilise le dataset Allociné au lieu des données de démo"
    )
    args = parser.parse_args()

    entrainer_modele(utiliser_allocine=args.allocine)


if __name__ == "__main__":
    main()
