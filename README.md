# Trier mes Mails 📧

Script Python pour trier automatiquement tes mails Gmail.

## 🎯 Ce qu'il fait
- ✅ Garde les mails **importants** (starred/marked as important) dans ta boîte
- 📤 Déplace les autres dans un dossier `a_supprimer`
- ✏️ Tu peux vérifier avant de vraiment les supprimer

## 📋 Prérequis
- Python 3.7+
- Compte Gmail
- Accès API Gmail (setup ci-dessous)

## ⚙️ Installation

### 1. Cloner le repo
```bash
git clone https://github.com/flemops/trier-mes-mails.git
cd trier-mes-mails
```

### 2. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 3. Configuration Gmail API
1. Va sur [Google Cloud Console](https://console.cloud.google.com/)
2. Crée un nouveau projet
3. Active l'API Gmail
4. Crée des identifiants (OAuth 2.0 - Application de bureau)
5. Télécharge le JSON → renomme-le `credentials.json`
6. Place-le dans le dossier du projet

## 🚀 Utilisation
```bash
python trier_mails.py
```

### Au premier lancement
- Ouverture navigateur pour authentification
- Token sauvegardé automatiquement

### Résultat
- Mails importants : restent en place
- Autres : label `a_supprimer`
- Résumé du tri affiché

## 🛡️ Sécurité
- `token.pickle` → ne pas commiter
- `credentials.json` → ne pas commiter
- Fichier `.gitignore` pré-configuré

## 📝 Note
Modification facile des critères dans le code si besoin.
