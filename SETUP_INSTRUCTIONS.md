# 🔧 Setup Gmail API - Instructions Complètes

## ⚡ Quick Start (2-3 minutes)

### Étape 1: Créer un Projet Google Cloud
1. Va sur: https://console.cloud.google.com/projectcreate
2. Nom du projet: `trier-mails`
3. Clique **"CRÉER"**
4. Attends 30 secondes

### Étape 2: Activer l'API Gmail
1. Va sur: https://console.cloud.google.com/apis/library/gmail.googleapis.com
2. Clique le bouton **"ACTIVER"**
3. Attends le chargement

### Étape 3: Créer les Credentials OAuth2
1. Va sur: https://console.cloud.google.com/apis/credentials
2. Clique **"+ CRÉER DES IDENTIFIANTS"**
3. Sélectionne:
   - Type: **Identifiants OAuth 2.0**
   - Application: **Application de bureau**
4. Clique **"CRÉER"**

### Étape 4: Télécharger le JSON
1. Clique sur ton app créée dans la liste
2. Clique le bouton **"TÉLÉCHARGER JSON"** (icône ⬇️)
3. Tu reçois: `client_secrets_xxx.json`

### Étape 5: Remplacer les Credentials
1. Ouvre le fichier téléchargé
2. Copie son contenu
3. Ouvre `credentials.json` dans ce dossier
4. Remplace tout le contenu
5. Sauvegarde

### Étape 6: Configure l'Écran de Consentement (optionnel mais recommandé)
1. Va sur: https://console.cloud.google.com/apis/credentials/consent
2. Type d'utilisateur: **Externe**
3. Clique **"CRÉER"**
4. Remplis:
   - Nom de l'app: `Trier Mails`
   - Email support: Ton email
   - Clique **"ENREGISTRER ET CONTINUER"**
5. Scopes: Ajoute `gmail.modify` si demandé
6. Utilisateurs de test: Ajoute ton email Gmail
7. Clique **"ENREGISTRER ET CONTINUER"**

### Étape 7: Lance le Script
```bash
python trier_mails.py
```

**Première fois:** S'ouvre un navigateur pour authentification
**Après:** Token sauvegardé, automatique

## 🔐 Sécurité
- ✅ `credentials.json` → dans `.gitignore`
- ✅ `token.pickle` → dans `.gitignore`
- ✅ Ne commit jamais ces fichiers!

## ✅ Prêt?
Une fois les credentials configurés, lance:
```bash
python trier_mails.py
```

## 🆘 Troubleshooting

### "credentials.json not found"
→ Vérifies que le fichier est dans le bon dossier

### "Invalid client credentials"
→ Télécharge à nouveau le JSON depuis Google Cloud Console

### "403 Forbidden"
→ Ajoute ton email comme utilisateur de test dans Google Cloud

