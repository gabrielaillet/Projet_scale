# Projet_scale
## Organisation
### App.py
ce fichier gere la navigation entre toutes les templates
### Templates
Toutes les templates se trouvent dans le fichier Template
### Database
ce ficher contient la creation du model de la database, la database et le dossier querys
#### Querys
ce fichier contient Add/delete/change/get gerant toutes les requetes sur la base de donnée 
### Form
ce fichier contient tous les formulaires de notre projet
## Installation 
il faut s'assurer que le chemin vers la base donné est le bon dans app.py ligne contenant app.config["SQLALCHEMY_DATABASE_URI"]
## Utilisation
On peut se connecter en tant que client ou admin et cela change les actions que nous pouvons effectuer 
