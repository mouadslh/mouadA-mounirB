"""Script temporaire pour tester le modèle"""
from pathlib import Path

import joblib

MODELE = Path("models/sentiment.joblib")

if MODELE.exists():
    print("Chargement du modèle...")
    pipeline = joblib.load(MODELE)

    print(f"Type du pipeline: {type(pipeline)}")
    print(f"Classes: {pipeline.classes_}")
    print(f"Steps: {list(pipeline.named_steps.keys())}")

    # Test avec quelques phrases
    test_phrases = [
        "Excellent produit, très satisfait",
        "Produit cassé à l'arrivée, service client absent",
        "Conforme à la description"
    ]

    print("\n=== Tests de prédiction ===")
    for phrase in test_phrases:
        label = pipeline.predict([phrase])[0]
        probas = pipeline.predict_proba([phrase])[0]
        print(f"\nPhrase: {phrase}")
        print(f"Label prédit: {label}")
        print(f"Probabilités: {dict(zip(pipeline.classes_, probas, strict=True))}")
else:
    print(f"Modèle non trouvé: {MODELE}")
