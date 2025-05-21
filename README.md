# 🔐 FTP Hydra Brute Force

Un script Python simple pour exécuter une attaque par force brute sur un serveur FTP en utilisant **Hydra**, tout en affichant chaque tentative de connexion.

---

## 🚀 Fonctionnalités

- Utilise `hydra` pour effectuer une attaque par dictionnaire sur un service FTP.
- Affiche chaque tentative de connexion en temps réel.
- Prend en charge les fichiers de logins et de mots de passe.
- Affiche les erreurs et résultats de l'attaque.

---

## 📦 Prérequis

- Python 3
- [Hydra](https://github.com/vanhauser-thc/thc-hydra)

```bash
sudo apt install hydra
```

---

## ⚙️ Utilisation

```bash
python3 hydra-brute-force-ftp.py -c <IP_CIBLE> -l <fichier_logins> -p <fichier_mots_de_passe>
```

### Exemple :

```bash
python3 hydra-brute-force-ftp.py -c 192.168.1.100 -l logins.txt -p passeword.txt
```

---
