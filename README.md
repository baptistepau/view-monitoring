# Monitoring Service Infomatique de ST-JO

# Technologie utilisée 
- Python
- Selenium
- Firefox ESR 

# Installation 
- Installer Python 3.8 ou supérieur
- Installer Firefox ESR
- Installer les dependance sur projet avec la commande suivante:
    ```bash
    pip install -r requirements.txt
    ```
- Cree un script bash sur linux ou bat sur windows pour lancer le Fichier `main.py` avec la commande suivante:
    ```bash
    python main.py
    ```
Ne pas oublier de bien lancer le programme dans le dossier on se trouve le projet

# Configuration 

Pour configurere le programme, il faut editer le fichier `conf_file.json` en modifiant les champs suivants:

---
```json 
"listeURL":["",""]
```
Correspond au liste des URL a surveiller

---
```json
"emplacementFirefox":""
```
Correspond a l'emplacmente de l'executable de Firefox ESR dans le cas de windows par default il se trouve dans `"C:\\Program Files\\Mozilla Firefox ESR\\firefox.exe"`

---
```json
"emplacmentDriver": ""
```

Correspond a l'emplacement du driver geckodriver

---
```json
"emplacementProfile": ""
```
Correspond a l'emplacement du profile de Firefox qui est obligatoire si vous utiliser des site qui on une connection avec user et mdp.

Le profile de Firefox se trouve dans le dossier `C:\Users\<username>\AppData\Roaming\Mozilla\Firefox\Profiles`

---
```json
 "time": 10
```
Correspond a la frequence ou le programme change d'onglets 