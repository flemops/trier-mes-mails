#!/usr/bin/env python3
"""
Génère les credentials Google Cloud automatiquement
Via gcloud CLI si disponible
"""

import subprocess
import json
import os
import sys

def check_gcloud():
    """Vérifie si gcloud CLI est installé"""
    try:
        result = subprocess.run(['gcloud', '--version'], capture_output=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False

def setup_with_gcloud():
    """Setup automatique avec gcloud CLI"""
    print("🔧 Utilisation de Google Cloud CLI...")
    
    commands = [
        # Créer un projet
        ['gcloud', 'projects', 'create', 'trier-mails', '--name', 'Mail Sorter'],
        
        # Activer l'API Gmail
        ['gcloud', 'services', 'enable', 'gmail.googleapis.com', '--project=trier-mails'],
        
        # Créer un service account
        ['gcloud', 'iam', 'service-accounts', 'create', 'mail-sorter',
         '--project=trier-mails', '--display-name=Mail Sorter Service'],
        
        # Créer et télécharger les credentials
        ['gcloud', 'iam', 'service-accounts', 'keys', 'create', 'credentials.json',
         '--iam-account=mail-sorter@trier-mails.iam.gserviceaccount.com',
         '--project=trier-mails'],
    ]
    
    for cmd in commands:
        try:
            print(f"⏳ Exécution: {' '.join(cmd[:3])}...")
            subprocess.run(cmd, check=False)
        except Exception as e:
            print(f"⚠️  {e}")
    
    if os.path.exists('credentials.json'):
        print("✅ credentials.json créé!")
        return True
    return False

def manual_setup():
    """Instructions manuelles"""
    print("""
╔════════════════════════════════════════════════════════════════════╗
║              SETUP MANUEL - 5 MINUTES                              ║
╚════════════════════════════════════════════════════════════════════╝

1️⃣  Va sur: https://console.cloud.google.com/projectcreate
2️⃣  Crée projet: 'trier-mails'
3️⃣  Va sur: https://console.cloud.google.com/apis/library/gmail.googleapis.com
4️⃣  Clique "ACTIVER"
5️⃣  Va sur: https://console.cloud.google.com/apis/credentials
6️⃣  Clique "+ CRÉER DES IDENTIFIANTS"
7️⃣  Sélectionne:
    - Type: "Identifiants OAuth 2.0"
    - Application: "Application de bureau"
8️⃣  Clique "CRÉER"
9️⃣  Télécharge le JSON
🔟 Renomme en "credentials.json"
""")

if __name__ == '__main__':
    if check_gcloud():
        setup_with_gcloud()
    else:
        manual_setup()
        print("\n📌 gcloud CLI non détecté")
        print("   Installe: https://cloud.google.com/sdk/docs/install")
