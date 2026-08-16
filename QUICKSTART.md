# 🚀 QUICKSTART - Trier tes mails

## ✅ Ce qui est déjà prêt
- ✓ Script principal: `trier_mails.py`
- ✓ Dépendances: Installées
- ✓ .gitignore: Configuré
- ✓ Structure: Prête

## 📝 Ce qu'il te reste à faire (5 min)

### Étape 1: Créer un Projet Google Cloud
```
https://console.cloud.google.com/projectcreate
```
- Nom: `trier-mails`
- Clique "CRÉER"

### Étape 2: Activer l'API Gmail
```
https://console.cloud.google.com/apis/library/gmail.googleapis.com
```
- Clique "ACTIVER"

### Étape 3: Créer les Credentials OAuth2
```
https://console.cloud.google.com/apis/credentials
```
- Clique "+ CRÉER DES IDENTIFIANTS"
- Type: **Identifiants OAuth 2.0**
- Application: **Application de bureau**
- Clique "CRÉER"

### Étape 4: Télécharger le JSON
1. Clique sur ton app créée
2. Clique "TÉLÉCHARGER JSON" (bouton ⬇️)
3. Tu reçois un fichier (ex: `client_secrets_xxx.json`)

### Étape 5: Remplacer credentials.json
1. Ouvre le fichier téléchargé
2. Copie tout le contenu
3. Ouvre `credentials.json` dans ce dossier
4. Remplace tout
5. Sauvegarde

### Étape 6: Lancer le Script
```bash
python trier_mails.py
```

**Première fois:** 
- S'ouvre un navigateur pour authentification
- Accepte les permissions

**Résultat:**
- Mails importants (starred) → Restent en place
- Autres mails → Label "a_supprimer"
- Token sauvegardé → Prochaines fois plus rapide

## 📊 Exemple de Sortie

```
🔐 Vérification credentials...
🔐 Authentification Gmail...
📂 Vérification labels...
✓ Label créé: a_supprimer

📧 Récupération des mails...
Total mails trouvés: 42

✓ IMPORTANT: Rapport mensuel
✓ IMPORTANT: Réunion demain
→ À supprimer: Newsletter...
→ À supprimer: Promotion...
...

📊 Résumé:
  • Mails importants gardés: 8
  • Mails déplacés: 34

✅ Tri terminé!
```

## 🔒 Sécurité
- `credentials.json` → .gitignore ✓
- `token.pickle` → .gitignore ✓
- Jamais de commit avec ces fichiers

## 🆘 Problèmes?

### "credentials.json contient des placeholders"
→ Tu n'as pas remplacé le contenu avec le vrai JSON

### "Invalid client"
→ Télécharge à nouveau le JSON depuis Google Cloud

### "403 Forbidden"
→ Ajoute ton email comme utilisateur de test

## ✨ C'est tout!

Une fois le setup fait, tout est automatique.

Questions? Vois SETUP_INSTRUCTIONS.md pour plus de détails.
