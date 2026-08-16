#!/bin/bash
# Script pour pusher sur GitHub

echo "📤 Configuration du push GitHub..."

# Ajoute l'origin
git remote remove origin 2>/dev/null
git remote add origin https://github.com/flemops/trier-mes-mails.git

# Renomme master en main
git branch -M main 2>/dev/null

# Push
echo "🚀 Push en cours..."
git push -u origin main

if [ $? -eq 0 ]; then
    echo "✅ Push réussi!"
    echo "   https://github.com/flemops/trier-mes-mails"
else
    echo "❌ Erreur du push"
    echo "   Assure-toi que GitHub est configuré sur ta machine"
fi
