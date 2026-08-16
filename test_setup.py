#!/usr/bin/env python3
"""
Test du setup - Génère un test environment
"""

import json
import os

print("""
╔════════════════════════════════════════════════════════════════════╗
║              CONFIGURATION FINALE DU PROJET                        ║
╚════════════════════════════════════════════════════════════════════╝
""")

# Vérifier les dépendances
print("📦 Vérification des dépendances...")
try:
    import google.auth
    import googleapiclient
    print("✓ Google API Python Client installé")
except ImportError:
    print("❌ Manque: google-api-python-client")
    print("   Lance: pip install -r requirements.txt")
    exit(1)

# Vérifier credentials.json
print("\n🔐 Vérification credentials.json...")
if not os.path.exists('credentials.json'):
    print("❌ credentials.json manquant!")
    exit(1)

with open('credentials.json') as f:
    creds = json.load(f)
    
if 'YOUR_PROJECT_ID' in str(creds) or 'REPLACE' in str(creds):
    print("⚠️  credentials.json contient des placeholders")
    print("\n📋 PROCHAINES ÉTAPES:")
    print("1. Va sur: https://console.cloud.google.com")
    print("2. Crée un projet 'trier-mails'")
    print("3. Active l'API Gmail")
    print("4. Crée des credentials OAuth2 (Desktop App)")
    print("5. Télécharge le JSON")
    print("6. Remplace le contenu de credentials.json")
    print("7. Relance ce script")
    exit(1)

print("✓ credentials.json valide")

# Afficher le résumé
print("\n📊 Configuration:")
print(f"   • Script: trier_mails.py")
print(f"   • Credentials: credentials.json")
print(f"   • Token: token.pickle (sera créé)")
print(f"   • Label: a_supprimer (sera créé)")

print("\n✅ Setup prêt!")
print("\n🚀 Lancement: python trier_mails.py")
