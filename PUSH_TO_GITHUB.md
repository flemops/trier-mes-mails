# 📤 Push vers GitHub

## Configuration du repo Git

```bash
git remote add origin https://github.com/flemops/trier-mes-mails.git
git branch -M main
git push -u origin main
```

## Points importants
- ✅ `.gitignore` protège `credentials.json` et `token.pickle`
- ✅ Ne push JAMAIS tes credentials
- ✅ Le repo ne contient que le code

## Push les mises à jour
```bash
git add .
git commit -m "message"
git push
```

## Cloner sur un autre ordi
```bash
git clone https://github.com/flemops/trier-mes-mails.git
cd trier-mes-mails
pip install -r requirements.txt
python trier_mails.py
```
