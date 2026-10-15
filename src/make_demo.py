"""
Génère le fichier data/demo_reviews.csv avec des avis de démonstration.
290 avis : 80 positifs nets + 80 négatifs nets + 100 mitigés + 30 neutres.
Graine aléatoire fixée à 42 pour la reproductibilité.
"""
import csv
import random
from pathlib import Path

# Chemin du fichier de sortie
RACINE = Path(__file__).resolve().parent.parent
FICHIER_SORTIE = RACINE / "data" / "demo_reviews.csv"

# Listes de base pour la génération
POSITIFS = [
    "Service impeccable et livraison en avance",
    "Produit conforme à la description, très satisfait",
    "Excellent rapport qualité prix",
    "Emballage soigné et finitions propres",
    "Prise en main immédiate, notice claire",
    "Le vendeur a répondu en moins d'une heure",
    "Je recommande sans hésiter",
    "Solide, léger, exactement ce que je cherchais"
]

NEGATIFS = [
    "Produit cassé à l'arrivée",
    "Aucune réponse du service client",
    "Commande jamais reçue et remboursement en attente",
    "Se casse au bout de deux utilisations",
    "Notice incompréhensible et pièces manquantes",
    "Taille trop petite et retour payant",
    "Application qui plante à chaque ouverture",
    "Facture erronée, aucun geste commercial"
]

ATTENUATIONS = [
    "au début",
    "les premiers jours",
    "sur le papier",
    "à la livraison",
    "au déballage"
]

RETOURNEMENTS = [
    "mais finalement",
    "sauf que ensuite",
    "puis rapidement",
    "avant que",
    "jusqu'à ce que"
]

NEUTRES = [
    "Reçu dans les délais annoncés",
    "Conforme à la fiche produit",
    "Rien de particulier à signaler",
    "Usage standard, sans surprise",
    "Livré, monté, utilisé"
]

SUFFIXES = ["", ", vraiment", ", comme prévu", " pour ce prix", " cette fois"]


def generer_avis():
    """
    Génère 290 avis avec une distribution contrôlée.
    Utilise une graine fixe (42) pour la reproductibilité.
    """
    # Initialiser le générateur aléatoire avec graine 42
    rng = random.Random(42)
    
    avis = []
    
    # 1. Générer 80 avis positifs nets
    for _ in range(80):
        base = rng.choice(POSITIFS)
        suffixe = rng.choice(SUFFIXES)
        texte = f"{base}{suffixe}."
        avis.append({"review": texte, "label": "positive"})
    
    # 2. Générer 80 avis négatifs nets
    for _ in range(80):
        base = rng.choice(NEGATIFS)
        suffixe = rng.choice(SUFFIXES)
        texte = f"{base}{suffixe}."
        avis.append({"review": texte, "label": "negative"})
    
    # 3. Générer 100 avis mitigés
    # L'étiquette finale suit la seconde moitié (la conclusion)
    for i in range(100):
        if i % 2 == 0:
            # Commence positif, finit négatif -> étiquette negative
            debut = rng.choice(POSITIFS)
            fin = rng.choice(NEGATIFS)
            attenuation = rng.choice(ATTENUATIONS)
            retournement = rng.choice(RETOURNEMENTS)
            texte = f"{debut} {attenuation}, {retournement} {fin.lower()}."
            avis.append({"review": texte, "label": "negative"})
        else:
            # Commence négatif, finit positif -> étiquette positive
            debut = rng.choice(NEGATIFS)
            fin = rng.choice(POSITIFS)
            attenuation = rng.choice(ATTENUATIONS)
            retournement = rng.choice(RETOURNEMENTS)
            texte = f"{debut} {attenuation}, {retournement} {fin.lower()}."
            avis.append({"review": texte, "label": "positive"})
    
    # 4. Générer 30 avis neutres (étiquetés en fonction du complément)
    for i in range(30):
        base = rng.choice(NEUTRES)
        if i % 2 == 0:
            # Neutre + positif -> étiquette positive
            complement = rng.choice(POSITIFS)
            texte = f"{base}, {complement.lower()}."
            avis.append({"review": texte, "label": "positive"})
        else:
            # Neutre + négatif -> étiquette negative
            complement = rng.choice(NEGATIFS)
            texte = f"{base}, {complement.lower()}."
            avis.append({"review": texte, "label": "negative"})
    
    # 5. Mélanger tous les avis avec la même graine
    rng.shuffle(avis)
    
    return avis


def sauvegarder_csv(avis, fichier):
    """Sauvegarde les avis dans un fichier CSV."""
    # Créer le dossier data s'il n'existe pas
    fichier.parent.mkdir(parents=True, exist_ok=True)
    
    # Écrire le fichier CSV en UTF-8
    with open(fichier, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["review", "label"])
        writer.writeheader()
        writer.writerows(avis)


def afficher_statistiques(avis):
    """Affiche les statistiques sur les avis générés."""
    total = len(avis)
    nb_positifs = sum(1 for a in avis if a["label"] == "positive")
    nb_negatifs = sum(1 for a in avis if a["label"] == "negative")
    
    print(f"Génération terminée : {total} avis")
    print(f"  - {nb_positifs} positifs")
    print(f"  - {nb_negatifs} négatifs")
    print(f"\nFichier sauvegardé : {FICHIER_SORTIE}")


def main():
    """Fonction principale."""
    print("Génération des avis de démonstration...")
    avis = generer_avis()
    sauvegarder_csv(avis, FICHIER_SORTIE)
    afficher_statistiques(avis)


if __name__ == "__main__":
    main()
