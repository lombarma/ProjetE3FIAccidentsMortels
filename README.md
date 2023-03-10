# Etudes des accidents en France en 2021

## Description
Nous avons choisi de travailler sur les accidents de la route en France sur l'année 2021. Pour cela, nous avons utilisé
des données provenant du site data.gouv.fr. Nous avons choisi de travailler sur les accidents de la route, car nous
sommes tous les deux utilisateurs de la route et nous trouvions intéressant d'étudier des données sur ce sujet. De plus,
il s'agit d'un sujet possédant une grande importance au vu du nombre d'accidents en France.

## User Guide

### Architecture du projet
```mermaid
graph TD
A[scripts] --> B[main.py]
C[data] --> A
D[get_data.py] --> C
```

### Installation et exécution
- (1) Cloner le projet sur votre ordinateur en utilisant la commande suivante : `git clone https://github.com/lombarma/ProjetE3FIAccidentsMortels.git`
- (2) Récupérer tous les packages additionnels en utilisant la commande suivante : `python -m pip install -r requirements.txt`
- (3) Récupérer les datasets en utilisant la commande suivante : `python get_data.py`
- (4) Lancer le programme en utilisant la commande suivante : `python main.py`

### Copyright
Nous déclarons sur l’honneur que le code fourni a été produit par Maxime LOMBARDO et Joël MBIAPA.


## Rapport d'analyse
Grâce à cette visualisation de données, nous pouvons tirer une conclusion de l'accident 'typique' qui peut se produire
avec un profil type de conducteur. Les accidents les plus récurrents sont les suivants :
- sexe : masculin
- âge : 20-24 ans
- type de véhicule : voiture
- gravité de l'accident : indemne
- heure de l'accident : 16h-18h
- lieu : Paris et sa banlieue
- avec principalement un fort taux d'accidents au début de l'été et au retour des vacances


## Developer Guide
L'architecture du projet est la suivante :
- `main.py` : Fichier principal du projet
- `get_data.py` : Fichier permettant de récupérer les données
- `data` : Dossier contenant les données
- `scripts` : Dossier contenant les scripts de traitement des données

Le fichier `main.py` est le fichier principal du projet. C'est dans ce fichier que le dashboard est créé.
C'est également ici que les fonctions sont appelées. Les données sont traitées dans différents fichiers
situés dans le dossier `scripts`. Ces fichiers sont appelés dans le fichier `main.py`. Dans le dossier `script`,
chaque fichier correspond à un traitement différent. Les fichiers sont nommés en fonction de la donnée et du graphique
qu'ils traitent. Par exemple, le fichier `pie_chart_accident_by_ages.py` est un fichier qui traite le nombre d'accidents
en fonction de l'âge des conducteurs. Il retourne un pie chart (camembert) qui est affiché dans le dashboard.

Pour étendre le projet, il suffit de créer un nouveau fichier dans le dossier `scripts` et de l'appeler dans le fichier `main.py`.
Il faut également modifier la fonction dash_project() dans le fichier `main.py` pour ajouter le nouveau graphique au dashboard.

## Authors
- Joël MBIAPA
- Maxime LOMBARDO
