#!/bin/bash

# Script pour setup automatique
echo "🚀 Configuration Gmail API..."
echo ""
echo "1. Ouvre Google Cloud Console"
echo "   https://console.cloud.google.com/projectcreate"
echo ""
echo "2. Crée un nouveau projet: 'trier-mails'"
echo ""
echo "3. Va à l'API Gmail et l'active"
echo "   https://console.cloud.google.com/apis/library/gmail.googleapis.com"
echo ""
echo "4. Crée des identifiants OAuth2"
echo "   https://console.cloud.google.com/apis/credentials"
echo ""
echo "5. Télécharge le JSON et renomme-le 'credentials.json'"
echo ""
echo "6. Place le fichier ici: $(pwd)/credentials.json"
echo ""
read -p "Appuie sur ENTRÉE quand credentials.json est prêt..."

if [ -f credentials.json ]; then
    echo "✅ credentials.json trouvé!"
    pip install -r requirements.txt
    python trier_mails.py
else
    echo "❌ credentials.json introuvable"
    exit 1
fi
