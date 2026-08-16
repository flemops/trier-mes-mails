#!/usr/bin/env python3
"""
Setup automatique pour Gmail API
Crée les credentials avec authentification OAuth2
"""

import os
import json
import sys
from pathlib import Path

def setup_google_cloud():
    """Guide l'utilisateur à travers le setup Google Cloud"""
    
    print("""
╔══════════════════════════════════════════════════════════════════╗
║              SETUP AUTOMATIQUE GMAIL API                         ║
╚══════════════════════════════════════════════════════════════════╝

⚠️  ATTENTION: Ce setup nécessite un accès manuel à Google Cloud Console

📱 Procédure rapide (2-3 minutes):

1️⃣  OUVRE GOOGLE CLOUD CONSOLE
   Clique ici: https://console.cloud.google.com/projectcreate

2️⃣  CRÉE UN PROJET
   • Nom: "trier-mails"
   • Clique "CRÉER"

3️⃣  ACTIVE L'API GMAIL
   Clique ici: https://console.cloud.google.com/apis/library/gmail.googleapis.com
   • Clique le bouton "ACTIVER"

4️⃣  CRÉE LES CREDENTIALS
   Clique ici: https://console.cloud.google.com/apis/credentials
   • Clique "+ CRÉER DES IDENTIFIANTS"
   • Type: "Identifiants OAuth 2.0"
   • Type d'application: "Application de bureau"
   • Clique "CRÉER"
   
5️⃣  TÉLÉCHARGE LE JSON
   • Clique sur ton app créée
   • Clique "TÉLÉCHARGER JSON"
   • Tu reçois un fichier credentials.json

6️⃣  PLACE LE FICHIER
   • Renomme: credentials.json
   • Copie dans ce dossier: {current_dir}

7️⃣  LANCE LE SCRIPT
   python trier_mails.py

""".format(current_dir=os.getcwd()))

    # Attendre que l'utilisateur place le fichier
    input("\n➡️  Appuie sur ENTRÉE une fois credentials.json placé dans ce dossier...")
    
    if os.path.exists('credentials.json'):
        print("\n✅ credentials.json détecté!")
        return True
    else:
        print("\n❌ Erreur: credentials.json introuvable")
        print(f"   Cherche dans: {os.getcwd()}")
        return False

def install_dependencies():
    """Installe les dépendances"""
    print("\n📦 Installation des dépendances...")
    os.system('pip install -q -r requirements.txt')
    print("✅ Dépendances installées")

def run_script():
    """Lance le script principal"""
    print("\n🚀 Lancement du tri des mails...\n")
    os.system('python trier_mails.py')

if __name__ == '__main__':
    if setup_google_cloud():
        install_dependencies()
        run_script()
    else:
        print("\n❌ Setup échoué. Réessaye.")
        sys.exit(1)
