"""
Fonctions utilitaires pour l'interface Streamlit.
Aucun import de streamlit dans ce fichier.
"""
import sys
from pathlib import Path
import pandas as pd

# Constantes
RACINE = Path(__file__).resolve().parents[1]
MODELE = RACINE / "models" / "sentiment.joblib"
SEUIL_INCERTITUDE = 0.60


def charger_predicteur():
    """
    Charge le prédicteur depuis src/predict.py.
    
    Returns:
        module: Le module predict avec la fonction predict()
    
    Raises:
        FileNotFoundError: Si le modèle n'existe pas
    """
    if not MODELE.exists():
        raise FileNotFoundError(
            f"Le modèle {MODELE} n'existe pas.\n"
            f"Lancez d'abord : python src/train.py --allocine"
        )
    
    # Import tardif de predict
    sys.path.insert(0, str(RACINE / "src"))
    from predict import predict
    
    # Retourner le module pour accès à la fonction
    import predict as predict_module
    return predict_module


def classer(texte, predicteur):
    """
    Classe un avis et ajoute les champs verdict et incertain.
    
    Args:
        texte: Le texte de l'avis
        predicteur: Le module predict
    
    Returns:
        dict: Résultat avec label, score, incertain et verdict
    
    Raises:
        ValueError: Si le texte est vide
    """
    if not texte or not isinstance(texte, str) or texte.strip() == "":
        raise ValueError("Le texte ne peut pas être vide")
    
    # Prédiction de base
    resultat = predicteur.predict(texte)
    
    # Ajouter le champ incertain
    resultat["incertain"] = resultat["score"] < SEUIL_INCERTITUDE
    
    # Ajouter le verdict
    if resultat["incertain"]:
        resultat["verdict"] = "à vérifier"
    else:
        resultat["verdict"] = resultat["label"]
    
    return resultat


def predire_lot(df, predicteur, colonne="review"):
    """
    Prédit le sentiment pour un DataFrame d'avis.
    
    Args:
        df: DataFrame avec au moins une colonne d'avis
        predicteur: Le module predict
        colonne: Nom de la colonne contenant les avis
    
    Returns:
        DataFrame: DataFrame enrichi avec prediction, confiance, verdict
    
    Raises:
        KeyError: Si la colonne n'existe pas
        ValueError: Si aucun avis exploitable
    """
    if colonne not in df.columns:
        raise KeyError(f"La colonne '{colonne}' n'existe pas dans le DataFrame")
    
    # Copier le DataFrame
    resultat = df.copy()
    
    # Initialiser les colonnes de résultat
    resultat["prediction"] = ""
    resultat["confiance"] = 0.0
    resultat["verdict"] = ""
    
    # Compter les avis exploitables
    nb_exploitables = 0
    
    # Prédire pour chaque ligne
    for idx, row in resultat.iterrows():
        texte = row[colonne]
        
        # Ignorer les lignes vides
        if pd.isna(texte) or not isinstance(texte, str) or texte.strip() == "":
            continue
        
        nb_exploitables += 1
        
        # Faire la prédiction
        pred = classer(texte, predicteur)
        
        resultat.at[idx, "prediction"] = pred["label"]
        resultat.at[idx, "confiance"] = round(pred["score"], 3)
        resultat.at[idx, "verdict"] = pred["verdict"]
    
    # Vérifier qu'il y a au moins un avis exploitable
    if nb_exploitables == 0:
        raise ValueError("Aucun avis exploitable dans le fichier")
    
    return resultat


def resumer(df):
    """
    Calcule un résumé statistique des prédictions.
    
    Args:
        df: DataFrame avec colonnes prediction, confiance, verdict
    
    Returns:
        dict: Statistiques (total, negatifs, part_negatifs, a_verifier, confiance_moyenne)
    """
    # Filtrer les lignes avec prédiction
    df_valide = df[df["prediction"] != ""].copy()
    
    total = len(df_valide)
    
    # Protéger contre division par zéro
    if total == 0:
        return {
            "total": 0,
            "negatifs": 0,
            "part_negatifs": 0.0,
            "a_verifier": 0,
            "confiance_moyenne": 0.0
        }
    
    negatifs = (df_valide["prediction"] == "negative").sum()
    a_verifier = (df_valide["verdict"] == "à vérifier").sum()
    confiance_moyenne = df_valide["confiance"].mean()
    part_negatifs = (negatifs / total) * 100
    
    return {
        "total": total,
        "negatifs": int(negatifs),
        "part_negatifs": round(part_negatifs, 1),
        "a_verifier": int(a_verifier),
        "confiance_moyenne": round(confiance_moyenne, 3)
    }
