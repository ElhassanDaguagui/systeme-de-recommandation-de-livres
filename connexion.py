import sqlite3
import streamlit as st
import subprocess

# Fonctions pour gérer les utilisateurs
def authenticate(username, password):
    # Votre logique d'authentification
    # Ici, je vais simplement comparer les informations avec des valeurs en dur
    return username == "admin" and password == "hassan"

# Fonction pour exécuter l'application d'administration
def run_admin_app():
    subprocess.run(["streamlit", "run", "administrateur.py"])

# Page de connexion
def login():
    st.title("Connexion")
    username = st.text_input("Nom d'utilisateur")
    password = st.text_input("Mot de passe", type="password")
    if st.button("Se connecter"):
        if authenticate(username, password):
            st.session_state.user = username  # Stocke le nom d'utilisateur dans st.session_state
            run_admin_app()  # Exécute l'application des livres
            return True
        else:
            st.error("Nom d'utilisateur ou mot de passe incorrect.")
    return False

def main():
    login()

if __name__ == "__main__":
    main()
