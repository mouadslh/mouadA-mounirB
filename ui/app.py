"""
Interface Streamlit pour l'analyse de sentiment d'avis clients.
Trois onglets : analyse d'un avis, analyse de fichier CSV, explications.
"""
import streamlit as st
import pandas as pd
from io import StringIO

from helpers import charger_predicteur, classer, predire_lot, resumer


# Configuration de la page
st.set_page_config(
    page_title="Analyse de sentiment",
    page_icon="💬",
    layout="wide"
)


@st.cache_resource
def init_predicteur():
    """Charge le prédicteur (avec cache)."""
    try:
        return charger_predicteur()
    except FileNotFoundError as e:
        st.error("⚠️ Modèle non trouvé")
        st.info("Lancez d'abord : **python src/train.py --allocine**")
        st.stop()


# Charger le prédicteur
predicteur = init_predicteur()


# Titre principal
st.title("💬 Analyse de sentiment - Avis clients")
st.markdown("Application de priorisation des avis négatifs pour équipes relation client")

# Trois onglets
tab1, tab2, tab3 = st.tabs(["📝 Un avis", "📁 Un fichier CSV", "❓ Comment ça marche"])


# ==================== ONGLET 1 : UN AVIS ====================
with tab1:
    st.header("Analyser un avis")
    
    texte_avis = st.text_area(
        "Saisissez l'avis à analyser :",
        height=150,
        placeholder="Exemple : Produit conforme, livraison rapide, je recommande"
    )
    
    if st.button("Analyser", type="primary"):
        if texte_avis.strip():
            with st.spinner("Analyse en cours..."):
                try:
                    resultat = classer(texte_avis, predicteur)
                    
                    label = resultat["label"]
                    score = resultat["score"]
                    incertain = resultat["incertain"]
                    
                    # Affichage selon le verdict
                    if incertain:
                        st.warning(
                            f"⚠️ **À vérifier par un agent** (penche vers « {label} »)"
                        )
                    elif label == "negative":
                        st.error("🚨 **Avis négatif** : à traiter en priorité")
                    else:
                        st.success("✅ **Avis positif**")
                    
                    # Barre de confiance
                    st.progress(score)
                    st.caption(f"Confiance : {score:.2%}")
                    
                except Exception as e:
                    st.error(f"Erreur : {e}")
        else:
            st.warning("Veuillez saisir un avis")


# ==================== ONGLET 2 : FICHIER CSV ====================
with tab2:
    st.header("Analyser un fichier CSV")
    
    st.markdown(
        "**Format attendu** : fichier CSV avec au moins une colonne nommée `review` "
        "contenant les avis."
    )
    
    fichier = st.file_uploader(
        "Téléversez votre fichier CSV :",
        type=["csv"],
        help="Le fichier doit contenir une colonne 'review'"
    )
    
    if fichier is not None:
        try:
            # Lire le CSV
            df_original = pd.read_csv(fichier, encoding="utf-8")
            
            st.success(f"✓ Fichier chargé : {len(df_original)} lignes")
            
            # Vérifier que la colonne review existe
            if "review" not in df_original.columns:
                st.error("❌ La colonne 'review' est manquante dans le fichier")
                st.stop()
            
            # Prédictions
            with st.spinner("Analyse en cours..."):
                df_resultat = predire_lot(df_original, predicteur)
                stats = resumer(df_resultat)
            
            # Affichage des métriques
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(
                    "Avis analysés",
                    stats["total"]
                )
            
            with col2:
                st.metric(
                    "Négatifs détectés",
                    stats["negatifs"],
                    delta=f"{stats['part_negatifs']}%"
                )
            
            with col3:
                st.metric(
                    "Cas à vérifier",
                    stats["a_verifier"]
                )
            
            # Graphique de répartition
            st.subheader("Répartition des avis")
            
            repartition = df_resultat[df_resultat["prediction"] != ""]["verdict"].value_counts()
            st.bar_chart(repartition)
            
            # Tableau des résultats (triés : négatifs en tête puis confiance décroissante)
            st.subheader("Résultats détaillés")
            
            df_affichage = df_resultat[df_resultat["prediction"] != ""].copy()
            
            # Trier : négatifs d'abord, puis par confiance décroissante
            df_affichage["ordre_priorite"] = df_affichage["prediction"].apply(
                lambda x: 0 if x == "negative" else 1
            )
            df_affichage = df_affichage.sort_values(
                by=["ordre_priorite", "confiance"],
                ascending=[True, False]
            ).drop(columns=["ordre_priorite"])
            
            st.dataframe(df_affichage, use_container_width=True)
            
            # Téléchargement des résultats
            csv_sortie = df_resultat.to_csv(index=False, encoding="utf-8")
            
            st.download_button(
                label="📥 Télécharger les résultats (CSV)",
                data=csv_sortie,
                file_name="resultats_sentiment.csv",
                mime="text/csv"
            )
            
        except Exception as e:
            st.error(f"Erreur lors du traitement du fichier : {e}")


# ==================== ONGLET 3 : COMMENT ÇA MARCHE ====================
with tab3:
    st.header("Comment ça marche ?")
    
    st.markdown("""
    ### 🎯 Objectif
    
    Cette application aide les équipes relation client à **prioriser le traitement des avis négatifs** 
    parmi un grand volume d'avis reçus quotidiennement.
    
    ### 🤖 Le modèle
    
    Le modèle utilise l'apprentissage automatique (régression logistique avec TF-IDF) pour classer 
    automatiquement les avis en **positifs** ou **négatifs**.
    
    Le modèle analyse le vocabulaire et les tournures de phrases pour déterminer le sentiment général.
    
    ### ⚠️ Avis "à vérifier"
    
    Lorsque le modèle est **peu confiant** dans sa prédiction (score < 60%), l'avis est marqué 
    comme **"à vérifier"**. Ces cas correspondent souvent à des avis mitigés ou ambigus qui méritent 
    une lecture humaine.
    
    ### 🚧 Limites
    
    - **Avis mitigés** : Les avis qui commencent positivement mais finissent négativement 
      (ou inversement) peuvent être mal classés.
    
    - **Ironie et sarcasme** : Le modèle ne détecte pas l'ironie ("Super, encore un produit cassé !").
    
    - **Contexte** : Le modèle analyse le vocabulaire mais pas le contexte métier spécifique.
    
    ### ✅ Recommandations
    
    - Toujours **vérifier les avis marqués "à vérifier"** avant de les écarter
    - Les avis négatifs détectés doivent être traités en priorité
    - Les faux positifs (avis positifs classés négatifs) sont acceptables car ils seront lus
    """)
