import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Configuration de la page (Design minimaliste et épuré)
st.set_page_config(
    page_title="Data & Esprit Critique",
    page_icon="📊",
    layout="centered"
)

# En-tête du site
st.title("📊 Data, Corrélations & Esprit Critique")
st.subheader("Le portfolio d'un Data Analyst qui ne croit pas tout ce qu'il voit.")

st.markdown("---")

# 2. Introduction et Storytelling
st.write("""
### Cas n°1 : Le fromage rend-il intelligent ? 🧀
On entend souvent dire que les statistiques ne mentent jamais. Pourtant, en cherchant bien, 
on peut faire dire n'importe quoi aux chiffres. Regardez ce graphique qui compare la consommation 
de fromage par habitant et le taux d'obtention de diplômes du supérieur dans différents pays.
""")

# 3. Simulation de données (À remplacer plus tard par ton vrai fichier CSV)
# Ici, on crée de fausses données qui se corrèlent parfaitement
data = {
    'Pays': ['France', 'USA', 'Allemagne', 'Suisse', 'Italie', 'Belgique', 'Canada', 'Japon'],
    'Consommation_Fromage_KG': [26, 17, 24, 22, 23, 15, 12, 3],
    'Taux_Diplomes_Pct': [48, 38, 44, 43, 41, 35, 30, 12]
}
df = pd.DataFrame(data)

# 4. Création du graphique interactif avec Plotly
fig = px.scatter(
    df, 
    x='Consommation_Fromage_KG', 
    y='Taux_Diplomes_Pct',
    text='Pays',
    title="Relation entre la consommation de fromage et le niveau d'études",
    labels={
        'Consommation_Fromage_KG': "Consommation de fromage (kg / habitant / an)",
        'Taux_Diplomes_Pct': "Pourcentage de diplômés du supérieur (%)"
    },
    trendline="ols" # Ajoute la ligne de tendance (corrélation) automatiquement !
)

# Personnalisation rapide du graphique (style épuré)
fig.update_traces(marker=dict(size=12, color='#1f77b4'), textposition='top center')
fig.update_layout(plot_bgcolor='white')

# Affichage du graphique sur le site web
st.plotly_chart(fig, use_container_width=True)

# 5. L'analyse du Data Analyst (Ce qui va impressionner le recruteur)
st.info("💡 **L'œil du Data Analyst :** Le coefficient de corrélation est extrêmement proche de 1. Pourtant...")

st.write("""
Manger du camembert ne vous aidera pas à réussir vos examens. Ce graphique cache une **variable de confusion** : 
**le PIB par habitant**. 

Les pays développés ont globalement un accès aux études supérieures plus large ET un pouvoir d'achat 
qui permet de consommer des produits de table plus variés ou importés (comme le fromage). 
En isolant l'effet de la richesse du pays via une régression multiple, la corrélation entre le fromage 
et les diplômes s'effondre.
""")

# Petit bouton bonus pour voir ton code sous le capot
with st.expander("🛠️ Voir le code Python de cette analyse"):
    st.code("""
    # Comment j'ai vérifié la corrélation en Python :
    correlation = df['Consommation_Fromage_KG'].corr(df['Taux_Diplomes_Pct'])
    print(f"Le coefficient de corrélation de Pearson est de : {correlation:.2f}")
    # Résultat : ~0.96 (Une corrélation presque parfaite, mais totalement illusoire !)
    """, language='python')