# Corrélations Illusoires

Application Streamlit démontrant une corrélation trompeuse entre consommation de fromage et taux de diplômes.

## Installation locale

1. Crée un environnement Python :
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
2. Installe les dépendances :
   ```powershell
   pip install -r requirements.txt
   ```
3. Lance l'application :
   ```powershell
   streamlit run app.py
   ```

## Publication sur GitHub

1. Crée un dépôt public sur GitHub.
2. Ajoute le dépôt distant dans ton dossier :
   ```powershell
   git remote add origin https://github.com/TON_UTILISATEUR/NOM_DU_DEPOT.git
   git branch -M main
   git push -u origin main
   ```

## Déploiement de l'application Streamlit

Pour rendre l'application accessible à tout le monde avec un lien :

1. Va sur https://streamlit.io/cloud
2. Connecte-toi avec GitHub.
3. Crée une nouvelle application en sélectionnant ton dépôt GitHub.
4. Streamlit génèrera un lien public que tu pourras partager.

> GitHub héberge le code. Streamlit Community Cloud héberge l'application web accessible via un URL public.
