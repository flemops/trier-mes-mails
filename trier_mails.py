#!/usr/bin/env python3
"""
Script pour trier les mails Gmail
- Mails importants : restent en place
- Autres : déplacés vers dossier "a_supprimer"
"""

import os
import sys
import pickle
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.api_core.exceptions import GoogleAPIError

# Configuration
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']
TOKEN_FILE = 'token.pickle'
CREDENTIALS_FILE = 'credentials.json'

def check_credentials():
    """Vérifie que les credentials existent"""
    if not os.path.exists(CREDENTIALS_FILE):
        print(f"❌ Erreur: {CREDENTIALS_FILE} non trouvé")
        print(f"📍 Cherche dans: {os.getcwd()}")
        print("\n📖 Voir SETUP_INSTRUCTIONS.md pour configurer les credentials")
        sys.exit(1)

    try:
        import json
        with open(CREDENTIALS_FILE) as f:
            creds = json.load(f)
            if 'YOUR_PROJECT_ID' in str(creds):
                print("⚠️  credentials.json contient des placeholders")
                print("📖 Suis les instructions dans SETUP_INSTRUCTIONS.md")
                sys.exit(1)
    except Exception as e:
        print(f"❌ Erreur lecture {CREDENTIALS_FILE}: {e}")
        sys.exit(1)

def authenticate_gmail():
    """Authentification à Gmail"""
    creds = None

    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)

        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)

    return creds

def get_gmail_service(creds):
    """Crée un service Gmail"""
    from googleapiclient.discovery import build
    return build('gmail', 'v1', credentials=creds)

def get_all_labels(service):
    """Récupère tous les labels"""
    results = service.users().labels().list(userId='me').execute()
    return results.get('labels', [])

def create_label(service, label_name):
    """Crée un nouveau label"""
    label_body = {
        'name': label_name,
        'labelListVisibility': 'labelShow',
        'messageListVisibility': 'show'
    }
    try:
        created_label = service.users().labels().create(
            userId='me',
            body=label_body
        ).execute()
        print(f"✓ Label créé: {label_name}")
        return created_label['id']
    except GoogleAPIError as e:
        print(f"✗ Erreur création label: {e}")
        return None

def get_label_id(service, label_name):
    """Récupère l'ID d'un label par son nom"""
    labels = get_all_labels(service)
    for label in labels:
        if label['name'] == label_name:
            return label['id']
    return None

def get_mails(service, query='', max_results=100):
    """Récupère les mails avec une query"""
    try:
        results = service.users().messages().list(
            userId='me',
            q=query,
            maxResults=max_results
        ).execute()
        return results.get('messages', [])
    except GoogleAPIError as e:
        print(f"✗ Erreur récupération mails: {e}")
        return []

def get_mail_details(service, message_id):
    """Récupère les détails d'un mail"""
    try:
        message = service.users().messages().get(
            userId='me',
            id=message_id,
            format='metadata',
            metadataHeaders=['From', 'Subject']
        ).execute()
        return message
    except GoogleAPIError as e:
        print(f"✗ Erreur détails mail: {e}")
        return None

def is_important(service, message_id):
    """Vérifie si un mail est marqué comme important"""
    try:
        message = service.users().messages().get(
            userId='me',
            id=message_id
        ).execute()

        labels = message.get('labelIds', [])
        return 'STARRED' in labels or 'IMPORTANT' in labels
    except GoogleAPIError as e:
        print(f"✗ Erreur vérification importance: {e}")
        return False

def move_to_label(service, message_id, label_id):
    """Déplace un mail vers un label"""
    try:
        service.users().messages().modify(
            userId='me',
            id=message_id,
            body={'addLabelIds': [label_id]}
        ).execute()
        return True
    except GoogleAPIError as e:
        print(f"✗ Erreur déplacement mail: {e}")
        return False

def trier_mails():
    """Fonction principale"""
    print("🔐 Vérification credentials...")
    check_credentials()

    print("🔐 Authentification Gmail...")
    creds = authenticate_gmail()
    service = get_gmail_service(creds)

    print("📂 Vérification labels...")
    label_id = get_label_id(service, 'a_supprimer')
    if not label_id:
        label_id = create_label(service, 'a_supprimer')
        if not label_id:
            print("✗ Impossible de créer le label")
            return

    print("\n📧 Récupération des mails...")
    all_mails = get_mails(service, query='', max_results=100)

    if not all_mails:
        print("ℹ️  Aucun mail trouvé")
        return

    print(f"Total mails trouvés: {len(all_mails)}\n")

    important_count = 0
    to_delete_count = 0

    for mail in all_mails:
        message_id = mail['id']
        details = get_mail_details(service, message_id)

        if not details:
            continue

        headers = details.get('payload', {}).get('headers', [])
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'Sans sujet')

        if is_important(service, message_id):
            print(f"✓ IMPORTANT: {subject[:60]}")
            important_count += 1
        else:
            print(f"→ À supprimer: {subject[:60]}")
            if move_to_label(service, message_id, label_id):
                to_delete_count += 1

    print(f"\n📊 Résumé:")
    print(f"  • Mails importants gardés: {important_count}")
    print(f"  • Mails déplacés: {to_delete_count}")
    print(f"\n✅ Tri terminé!")

if __name__ == '__main__':
    try:
        trier_mails()
    except KeyboardInterrupt:
        print("\n⚠️  Interrompu par l'utilisateur")
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
