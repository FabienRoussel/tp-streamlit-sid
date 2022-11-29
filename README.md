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
``` bash
make help
```

**Si la commande ci-dessus ne fonctionne pas, alors utiliser l'alternative aux commandes make pour la suite du TP.**

Télécharger le csv sur [le challenge kaggle](https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data?resource=download) et ajouter le au dossier `data`. 
N'oubliez pas de le *unzip*.

### Création de l'environnement Conda

Le projet utilise `conda` pour gérer les environnements virtuels Python : [Guide d'installation Miniconda](https://docs.conda.io/en/latest/miniconda.html).

Créer un environnement virtuel Python lié au projet :
``` bash
make conda_env
```

**Alternative :** `conda create --name tp-streamlit-sid python=3.9 -y` 


Une fois l'environnement installé, il vous suffit de faire la commande suivante afin de rentrer dans l'environnement :
``` bash
conda activate tp-streamlit-sid
```

### Installation des dépendances

Vous pouvez désormais installer l'ensemble des dépendances du projet dans un environnement isolé.
La commande suivante vous permet d'installer :
1. Le package du projet en mode développement
2. Les dépendances liées au développement (libraries de test, etc.)
```shell
make dependencies
```
**Alternative :** `pip install -e .[dev]` 

Sur windows il faut installer streamlit avec conda également :
``` bash 
conda install -c conda-forge streamlit
```

## Rendre disponible le kernel pour les notebooks
Afin de pouvoir sélectionner, dans nos notebooks, l'environnement que nous venons de créer, il est nécessaire de faire.
``` shell
python -m ipykernel install --user --name=tp-streamlit-sid
```

## Démarrer un notebook
Dans un shell il vous suffit de faire.
``` shell
jupyter notebook
```

Aller dans le dossier `notebook` et ouvrez le premier fichier intitulé `analyse_exploratoire.ipynb`.
Dans la barre en haut, cliquer ensuite sur `kernel` puis `Change kernel` puis sélectionner `tp-streamlit-sid`.


## Lancer l'application streamlit
Ouvrez un second terminal `anaconda prompt` et exécutez les lignes suivante : 

``` bash 
cd tp-streamlit-sid
conda activate tp-streamlit-sid
```

Ensuite, il vous suffit d'éxécuter la commande suivante afin de démarrer l'application streamlit.
```shell
make streamlit
```

**Alternative :** `streamlit run dashboard.py` 

## Questions 

Pour la suite du TP vous allez vous aider de la documentation de [plotly express](https://plotly.com/python/plotly-express/) ainsi que celle de [streamlit](https://docs.streamlit.io/).

Prenez le temps de lire [cette article sur l'usage de streamlit](https://blog.octo.com/creer-une-web-app-interactive-en-10min-avec-streamlit/). 


#### Question 1 : Ajouter des filtres dans l'inteface
Lorsque vous avez démarré streamlit, vous disposez déjà d'un filtre sur le type de véhicules. Ajoutez également les filtres suivants :
- un filtre de type multiselect pour filtrer par constructeur, colonne `manufacturer`.
- un filtre de type range slider sur la date d'annonce, colonne `year`.
- un filtre de type radio sur le type de carburant, colonne `fuel`.
- un filtre de type radio sur l'état du véhicule, colonne `condition`.
- un filtre de type multiselect sur la couleur du véhicule, colonne `paint_color`.
- un filtre de type slider sur la date d'annonce, colonne `posting_date`,
de telle sorte que la valeur sélectionnée permette de ne garder que les véhicules **au dessus de cette valeur**.
- un filtre de type slider sur le kilométrage du véhicule, colonne `odometer`, 
de telle sorte que la valeur sélectionnée permette de ne garder que les véhicules **en dessous de cette valeur**.


#### Question 2 : feature engineering
Pour cette question, il faudra créer et implémenter des méthodes répondant à chacune des étapes dans le fichier `src/utils.py`
et il faudra appeler ces méthodes dans la fonction `_update_columns_type_and_add_columns` dans le fichier `src/data_loading.py`.
On pourra se servir de l'étape 1 en tant qu'exemple.

**Etape 1 :**
Compléter le code de la méthode `get_number_of_cylinders` dans `src/utils.py` afin de récupérer le nombre de cylindres.
Help : Il suffit de `split` sur chaque chaine de caractères non null (not na) de la colonne `cylinder`.
Si l'élément est null alors on indiquera -1.

**Etape 2 :**
Compléter la méthode `drop_vehicules_with_more_than_300_000_kilometers` dans `src/utils.py` 
afin de retirer tous les véhicules ayant plus de 300 000 km.


Pour toutes les questions suivantes, aidez-vous du notebook mis à disposition pour tester vos graphes facilement.

#### Question 3 
Afficher un histogramme sur le kilométrage, colonne `odometer` des véhicules. 
Vous pouvez aider du notebook dans lequel se trouve déjà un histogramme similaire. 

#### Question 4 
De la même façon que la question 3, afficher un histogramme de la colonne `year`. 
N'oubliez par de passer par le même formalisme en créant la ou les méthodes nécessaires.

#### Question 5 
Faites deux diagrammes barres horizontales affichant :
- les occurrences des peintures `paint_color` (le nombre de voitures ayant la même couleur). 
- les occurrences des constructeurs `manufacturer` (le nombre de voitures ayant le même constructeur).

Helper : pensez à utiliser la [méthode `value_counts()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.value_counts.html).

Ordonnez vos deux diagrammes par ordre décroissant des occurrences.

#### Question 6 

Réaliser un graphe faisant apparaitre la proportion de type de carburant `fuel` des véhicules en fonction de leur catégorie `type`.

Helper : un diagramme barre stack serait approprié mais vous pouvez en proposer d'autres.


#### Question 7
A l'aide de la longitude et de la lattitude, afficher une carte plotly avec des points dont la taille dépend du prix total des annonces. 
[Documentation](https://plotly.com/python/bubble-maps/).

#### Question 8

Réaliser une carte affichant le prix moyen des véhicules par État au fil des ans. 

Il n'existe pas qu'une façon de faire, mais vous pourriez suivre celle qui est présente dans cet article : 
https://towardsdatascience.com/simple-plotly-tutorials-868bd0890b8b.
Vous avez également un exemple dans la documentation donnée dans la question 8.

Voici également un geojson https://public.opendatasoft.com/explore/dataset/us-state-boundaries/table/. 
La colonne `stusab` mise en minuscule pourrait faire une bonne correspondance avec notre colonne `state`.
 
#### Question 9 

Réorganiser votre dashboard afin d'améliorer les couleurs des graphes, diminuer ou augmenter la taille de certains graphes si nécessaire.
