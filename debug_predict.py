"""Script de débogage pour identifier le problème de classification"""
from src.predict import predict

# Tests avec différents types d'avis
test_cases = [
    ("Excellent produit, très satisfait, je recommande", "positive"),
    ("Produit cassé, service horrible, très déçu", "negative"),
    ("Emballage soigné et finitions propres", "positive"),
    ("Aucune réponse du service client", "negative"),
    ("Service impeccable et livraison en avance", "positive"),
    ("Produit conforme à la description", "positive"),
    ("Livraison rapide", "positive"),
    ("Très déçu par la qualité", "negative"),
    ("Je suis ravie de mon achat", "positive"),
    ("Ne fonctionne pas du tout", "negative"),
]

print("=" * 70)
print("TESTS DE PRÉDICTION")
print("=" * 70)

erreurs = []
for texte, attendu in test_cases:
    resultat = predict(texte)
    label_predit = resultat["label"]
    score = resultat["score"]

    statut = "✓" if label_predit == attendu else "✗ ERREUR"
    print(f"\n{statut} {texte[:50]:50s}")
    print(f"   Attendu: {attendu:8s} | Prédit: {label_predit:8s} | Score: {score:.4f}")

    if label_predit != attendu:
        erreurs.append((texte, attendu, label_predit, score))

print("\n" + "=" * 70)
print(f"RÉSULTAT: {len(test_cases) - len(erreurs)}/{len(test_cases)} correct")
if erreurs:
    print(f"ERREURS: {len(erreurs)}")
    for texte, attendu, predit, score in erreurs:
        print(f"  - '{texte}' -> attendu={attendu}, prédit={predit}, score={score}")
else:
    print("Tous les tests sont passés !")
print("=" * 70)
