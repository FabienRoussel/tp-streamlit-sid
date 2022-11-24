# TP Streamlit SID

Projet streamlit afin d'explorer les données des ventes de voitures d'occasion ainsi que de présenter les résultats..

## Quickstart

Démarrer l'invit de commande Anaconda (anaconda prompt) sur vos machines.

Cloner ce répertoire à l'aide la commande : 
``` bash 
git clone https://github.com/FabienRoussel/tp-streamlit-sid
```

Puis aller dans le répertoire éponyme :
``` bash 
cd tp-streamlit-sid
```

Pour faciliter l'installation de l'environnement de développement, un [Makefile](Makefile) automatise certaines actions
que vous pouvez découvrir grâce à la commande suivante :
```shell
$ make help
```

Télécharger le csv sur [le challenge kaggle](https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data?resource=download) et ajouter le au dossier `data`.

### Création de l'environnement Conda

Le projet utilise `conda` pour gérer les environnements virtuels Python : [Guide d'installation Miniconda](https://docs.conda.io/en/latest/miniconda.html).

Créer un environnement virtuel Python lié au projet :
```shell
$ make conda_env
```

Une fois l'environnement installé, il vous suffit de faire la commande suivante afin de rentrer dans l'environnement:
```shell
$ conda activate tp-streamlit-sid
```

### Installation des dépendances

Vous pouvez désormais installer l'ensemble des dépendances du projet dans un environnement isolé.
La commande suivante vous permet d'installer :
1. Le package du projet en mode développement
2. Les dépendances liées au développement (libraries de test, etc.)
```shell
$ make dependencies
```

### Lancer l'application streamlit
Il vous suffit d'éxécuter la commande suivant afin de démarrer l'application streamlit.
```shell
$ make streamlit
```

## Questions 

Pour la suite du TP vous allez vous aider de la documentation de [plotly express](https://plotly.com/python/plotly-express/) ainsi que celle de [streamlit](https://docs.streamlit.io/).

Prenez le temps de lire [cette article sur l'usage de streamlit](https://blog.octo.com/creer-une-web-app-interactive-en-10min-avec-streamlit/) 

