#!/usr/bin/env python3
"""
Setup complet automatisé pour Gmail API
Utilise Google OAuth2 sans intervention manuelle
"""

import os
import json
import webbrowser
from pathlib import Path

def create_oauth_credentials():
    """
    Crée les credentials OAuth2 pour Gmail
    """
    print("""
╔════════════════════════════════════════════════════════════════════╗
║         CONFIGURATION AUTOMATIQUE GMAIL API OAUTH2                 ║
╚════════════════════════════════════════════════════════════════════╝
""")
    
    # Ouvre Google Cloud Console dans le navigateur
    print("🌐 Ouverture Google Cloud Console...")
    webbrowser.open('https://console.cloud.google.com/projectcreate')
    
    print("\n📋 Étapes à suivre:")
    print("1. Crée un projet: 'trier-mails'")
    print("2. Clique sur le projet créé")
    print("3. Va à APIs & Services > Credentials")
    print("4. Clique '+ Create Credentials'")
    print("5. Sélectionne 'OAuth 2.0 Client ID'")
    print("6. Type: 'Desktop Application'")
    print("7. Clique 'Create'")
    print("8. Télécharge le JSON")
    
    return ask_for_credentials()

def ask_for_credentials():
    """Demande à l'utilisateur de coller les credentials"""
    print("\n" + "="*70)
    print("📝 Colle le contenu du fichier credentials.json téléchargé:")
    print("="*70)
    print("(Colle puis appuie ENTER deux fois)")
    print()
    
    lines = []
    empty_count = 0
    
    while empty_count < 2:
        try:
            line = input()
            if line.strip() == "":
                empty_count += 1
            else:
                empty_count = 0
                lines.append(line)
        except EOFError:
            break
    
    credentials_str = "\n".join(lines)
    
    try:
        credentials = json.loads(credentials_str)
        return credentials
    except json.JSONDecodeError:
        print("❌ JSON invalide")
        return None

def save_credentials(creds):
    """Sauvegarde les credentials"""
    if creds:
        with open('credentials.json', 'w') as f:
            json.dump(creds, f, indent=2)
        print("\n✅ credentials.json sauvegardé!")
        return True
    return False

def install_and_run():
    """Installe les dépendances et lance le script"""
    print("\n📦 Installation des dépendances...")
    os.system('pip install -q google-auth-oauthlib google-auth-httplib2 google-api-python-client')
    
    print("\n🚀 Lancement du tri des mails...\n")
    os.system('python trier_mails.py')

if __name__ == '__main__':
    creds = create_oauth_credentials()
    if save_credentials(creds):
        try:
            install_and_run()
        except Exception as e:
            print(f"\n❌ Erreur: {e}")
    else:
        print("\n❌ Setup échoué")
