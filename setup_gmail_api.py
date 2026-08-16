#!/usr/bin/env python3
"""
Setup script pour configurer Gmail API
- Crée un projet Google Cloud
- Active l'API Gmail
- Récupère les credentials OAuth2
"""

import webbrowser
import os

def print_instructions():
    """Affiche les instructions de setup"""
    print("""
╔════════════════════════════════════════════════════════════════════╗
║          SETUP GMAIL API - INSTRUCTIONS COMPLÈTES                  ║
╚════════════════════════════════════════════════════════════════════╝

📋 ÉTAPES À SUIVRE:

1️⃣  CRÉER UN PROJET GOOGLE CLOUD
   • Va sur: https://console.cloud.google.com/projectcreate
   • Crée un nouveau projet (ex: "trier-mails")
   • Attends quelques secondes que le projet se crée

2️⃣  ACTIVER L'API GMAIL
   • Va sur: https://console.cloud.google.com/apis/library/gmail.googleapis.com
   • Clique "ACTIVER"
   • Attends le chargement

3️⃣  CRÉER LES CREDENTIALS OAUTH2
   • Va sur: https://console.cloud.google.com/apis/credentials
   • Clique "+ CRÉER DES IDENTIFIANTS"
   • Sélectionne: Identifiants OAuth 2.0
   • Sélectionne: "Application de bureau"
   • Clique "CRÉER"
   • Clique sur l'élément créé
   • Clique "TÉLÉCHARGER JSON"
   • Renomme le fichier en "credentials.json"
   • Place-le dans ce dossier (trier-mes-mails/)

4️⃣  CONFIGURE LE CONSENTEMENT OAUTH
   • Va sur: https://console.cloud.google.com/apis/credentials/consent
   • Type: "Utilisateur"
   • Crée l'écran de consentement
   • Remplis: "Nom de l'application" = "Trier Mails"
   • Enregistre et continue

5️⃣  UNE FOIS CREDENTIALS.JSON PRÉSENT
   • Lance: python trier_mails.py
   • Première fois: s'ouvre un navigateur pour authentication
   • Token sauvegardé automatiquement

🔒 SÉCURITÉ
   • credentials.json et token.pickle sont dans .gitignore
   • Ne les commit jamais!

✅ PRÊT? Lance: python trier_mails.py
""")

if __name__ == '__main__':
    print_instructions()
    
    # Ouvre le Google Cloud Console
    print("\n🌐 Ouverture Google Cloud Console...")
    webbrowser.open('https://console.cloud.google.com/projectcreate')
