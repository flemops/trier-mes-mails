# trier-mes-mails

> **Statut : ARCHIVÉ (07/10/2026) — lab abandonné, conservé pour mémoire.** Aucun développement, aucune maintenance.

Petit script Python (août 2026) qui triait une boîte **Gmail** via l'API Gmail : les mails marqués importants restaient en place, les autres recevaient un label `a_supprimer` pour relecture avant suppression.

## Pourquoi archivé

- Un usage ponctuel, limité à Gmail ; le tri courant se fait désormais par **règles de messagerie** (Outlook) et par automatisation n8n auto-hébergée, sans code à maintenir ici.
- Le dépôt contient plusieurs scripts d'installation redondants (`auto_setup.py`, `full_setup.py`, `setup_auto.sh`, …) et une authentification par fichier `token.pickle` : ni l'un ni l'autre ne mérite d'être modernisé pour un outil remplacé.
- Aucun autre dépôt ni service ne dépend de celui-ci (vérifié le 07/10/2026).

## Ce que montrait le projet

Premier contact avec une API OAuth (Gmail), un script en ligne de commande et une CI Python minimale (`pip check`, compilation, `pip-audit`). **Lab personnel, pas un produit** ; aucune garantie de fonctionnement.

## Précautions si quelqu'un le réutilise

- Portée OAuth demandée : `gmail.modify` (lecture et modification) — plus large que nécessaire pour un simple étiquetage ; à restreindre.
- Pas de mode « simulation » (dry-run) : le script applique le label directement.
- `token.pickle` et `credentials.json` ne doivent jamais être commités (le `.gitignore` les exclut). Un fichier `credentials.json` composé uniquement de valeurs d'exemple a figuré dans l'historique initial ; il ne contenait aucun identifiant réel.
