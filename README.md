# 4A_ILC_QuickFind_The_Snake
Benjamin GIROD (absent lors de la deuxième séance de TP) - Federico DI SPIRITO  
ILC

# Sujet choisi : Sujet guidé 

L'objectif est de créer une API Flask pour de la gestion CRUD d’un système de transaction. Nous avons choisis ce sujet étant débutant avec l'approche CI/CD.

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

# Réalisation d'une première version de l’API REST  

En utilisant Flask, nous avons réalisé une première version de l’API.  
  
Voici une liste des actions qui ont été mises en place via un appel HTTP sur API:
* E1 - Enregistrer une transaction.
* E2 - Afficher une liste de toutes les transactions dans l’ordre chronologique.
* E3 - Afficher une liste des transactions dans l’ordre chronologique liées à une personne.
* E4 - Afficher le solde du compte de la personne.
* E5 - Importer des données depuis un fichier .csv

Nous avons deux fichiers .csv différents qui utilisent tous deux la bibliothèque pandas : 

personnes.csv : Ce fichier contient deux colonnes 'solde' et 'transactions' séparées avec ';' 

transaction.csv : Ce fichier contient cinq colonnes 'P1', 'P2', 's', 't' et 'h' séparées aussi avec ';' P1 et P2 représentent les personnes liées à la transaction, s la somme d'argent transféré, t l'heure de la transaction et h l'hash.

# Fichier Swagger
  
Le fichier swagger est disponible sur le dépot. Ce fichier détaille les différents endpoints dans un YAML

# Préparer l’intégration continue (CI)

Les trois github actions demandées ont été réalisées :

* Une déclenchée à chaque changement pour builder l’application. 

![example workflow](https://github.com/Tebenj/4A_ILC_QuickFind_The_Snake/actions/workflows/build_application.yml/badge.svg)

* Une déclenchée manuellement pour builder et dockeriser et pousser l’image de l’API.

![example workflow](https://github.com/Tebenj/4A_ILC_QuickFind_The_Snake/actions/workflows/Docker_push_GCR.yml/badge.svg)

* Une déclenchée pour chaque tag semver pour builder et dockeriser et pousser l’image de l’API avec en tag la version semver spécifiée.

![example workflow](https://github.com/Tebenj/4A_ILC_QuickFind_The_Snake/actions/workflows/Docker_push_semver.yml/badge.svg)

# Release de l'API 

Nous possèdons 4 release différentes : 

* v1.0.0 : Cette release contient les différents endpoints, les github actions ainsi que le fichier swagger.

* v1.1.0 : Cette release contient l'ajout de la fonction hachage au projet. Nous avons opté pour la fonction de hachage sha-256 qui est utilisée pour vérifier l'intégrité des données en s'assurant que les données originales n'ont pas été altérées ou corrompues au cours du stockage ou de la transmission. Elle produit un haché de 256 bits.

* v2.0.0 : Cette release ajoute la vérification de l'intégrité des données

* v2.0.1 : Cette release ajoute le paramètre t pour la fonction de hachage 

# Fonctionnement de l'API 

Les données des personnes et des transactions sont stockées dans des fichiers CSV et importées dans des listes Python. L'API définit plusieurs routes pour répondre à des requêtes GET et POST:

* '/' retourne la liste de toutes les transactions triées par temps : appelé dans un aurtre terminal avec la commande: curl -X GET http://localhost:5000

* '/personnes' retourne la liste de toutes les personnes : appelé dans un aurtre terminal avec la commande: curl -X GET http://localhost:5000/personnes

* '/personnes/transactions/&lt;personne&gt; retourne la liste de toutes les transactions pour une personne donnée : appelé dans un aurtre terminal avec la commande: curl -X GET http://localhost:5000/personnes/transactions/ &lt;personne&gt;

 * '/personnes/solde/&lt;personne&gt;' retourne le solde d'une personne donnée : appelé dans un aurtre terminal avec la commande: curl -X GET http://localhost:5000/personnes/solde/ &lt;personne&gt;

 * '/addPersonne' ajoute une nouvelle personne à la liste des personnes via une requête POST : appelé dans un aurtre terminal avec la commande: curl -X GET http://localhost:5000/addPersonne

* '/addTransaction' ajoute une nouvelle transaction à la liste des transactions via une requête POST : appelé dans un aurtre terminal avec la commande: curl -X GET http://localhost:5000/addTransaction

* '/verification' vérifie l'intégrité des données en comparant les hashs des transactions avec les hashs recalculés : : appelé dans un aurtre terminal avec la commande: curl -X GET http://localhost:5000/verification
  
  
