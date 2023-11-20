![Logo](https://github.com/CelineBoutinon/bookworms/assets/143210563/7f9f7b60-1be0-4a14-85ad-ded58e218662)



# ANALYSER  LES VENTES D'UNE LIBRAIRIE AVEC PYTHON

Projet realisé en mai 2023 dans le cadre de ma formation Data Analyst avec OpenClassrooms.

## Objectif du projet

Lapage, une grande librairie généraliste en ligne très réputée, était originellement une librairie physique avec plusieurs points de vente. Mais devant le succès de certains de ses produits et l’engouement de ses clients, elle a décidé depuis 2 ans d’ouvrir un site de vente en ligne. Après deux ans d’exercice, l'entreprise souhaite faire le point et pouvoir analyser ses forces, ses
faiblesses, les comportements clients, etc.
Cette analyse doit se composer de deux parties :
* **Une analyse des différents indicateurs de vente :** qui doit inclure notamment différents indicateurs et graphiques autour du chiffre d'affaires et de son évolution dans le temps (avec décomposition en moyenne mobile pour évaluer la tendance globale), ainsi qu'un zoom sur les références (tops & flops, répartition par catégorie) et des informations sur les profils des clients et la répartition du chiffre d'affaires entre eux (courbe de Lorenz); et
* **Une analyse plus ciblée sur les clients :** visant à  comprendre leur comportement en ligne pour pouvoir ensuite le comparer avec la connaissance acquise via les librairies physiques de l'enseigne. On visera en particulier le lien entre le genre d’un client et les catégories des livres achetés, le lien entre l’âge des clients et le montant total des achats, la fréquence d’achat, la taille du panier moyen et les catégories des livres achetés.

## Liste des dossiers & fichiers

* **dossiers :**
  - **donnees-brutes :** fichiers téléchargés depuis les sources (format .xslx) 


* **fichiers :**
	- **notebook_1.ipynb :** code Python permettant l'import des fichiers .xlsx, leur nettoyage et la production des analyses statistiques et graphiques
	- **notebook_2.ipynb :** code Python permettant l'analyse des associations dans les paniers clients comportant au moins un livre figurant au top 10 des ventes
	- **presentation.pdf:** diapositives de présentation du projet
  - **presentation_notes.pdf :** notes d’accompagnement des diapositives de présentation du projet
  - **functions.py :** fichier de fonctions auxquelles les notebooks Jupyter font appel


## Compétences développées

* Réaliser un test statistique
* Réaliser une analyse bivariée pour interpréter des données
* Analyser des séries temporelles



## Langages & software

* Python 3.9.13
  * matplotlib 3.6.2
  * missingno 0.5.1
  * mlxtend 0.21.0
  * numpy 1.24.1
  * pandas 1.5.2
  * scikit-learn 1.2.2
  * scikit-posthocs 0.7.03
  * seaborn 0.12.2
  * statsmodels 0.13.5
 

* Jupyter Notebook 6.4.12








