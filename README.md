# Projet View Monitoring

# Technologie utilisée  
- Python
- Selenium
- Firefox ESR 

# Installation 
- De préférence, installer la version 3.13 dans un venv

	[Lien Python 3.13.3 pour Windows](https://www.python.org/ftp/python/3.13.3/python-3.13.3-amd64.exe)
	
	Python 3.13 sur Debian 12
	```bash
	sudo apt install python3.13 python3.13-venv python3.13-dev
	```
- Installer Firefox ESR
-Installer les dépendances sur le projet avec la commande suivante :
    ```bash
    pip install -r requirements.txt
    ```
- Crée un script bash sur Linux ou un script bat sur Windows pour lancer le fichier main.py avec la commande suivante :
    ```bash
    python main.py
    ```
Ne pas oublier de bien lancer le programme dans le dossier où se trouve le projet.

# Configuration 

Pour configurer le programme, il faut éditer le fichier  `conf_file.json`  en modifiant les champs suivants :

---
```json 
"listeURL":["",""]
```
Correspond à la liste des URL à surveiller.

---
```json
"emplacementFirefox":""
```
Correspond à l'emplacement de l’exécutable de Firefox ESR. Dans le cas de Windows, par défaut, il se trouve dans : `"C:\\Program Files\\Mozilla Firefox ESR\\firefox.exe"`

---
```json
"emplacmentDriver": ""
```

Correspond à l'emplacement du driver geckodriver, qui est fourni dans le dépôt de logiciels. (Pourra un jour demander une mise à jour.)

---
```json
"emplacementProfile": ""
```
Correspond à l'emplacement du profil de Firefox, qui est obligatoire si vous utilisez des sites nécessitant une connexion avec un utilisateur et un mot de passe.

Le profil de Firefox se trouve dans le dossier : `C:\Users\<username>\AppData\Roaming\Mozilla\Firefox\Profiles`

---
```json
 "time": 10
```
Correspond à la fréquence à laquelle le programme change d'onglet.