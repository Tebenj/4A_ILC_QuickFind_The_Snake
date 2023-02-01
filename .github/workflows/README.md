# Workflows réalisé pour le TD : 


hello_there.yml : Action qui se déclenche à chaque pull request sur la branche main qui exécute la commande python main.py. Ce script python affichait "Hello there" initialement pour le TD mais nous l'avons modifié afin qu'il corresponde maintenant à notre projet.

![example workflow](https://github.com/Tebenj/4A_ILC_QuickFind_The_Snake/actions/workflows/hello_there.yml/badge.svg)

blank.yml : Action qui se déclenche manuellement afin d'éxecuter la commande curl sur l'adresse wttr.in/Moon 

![example workflow](https://github.com/Tebenj/4A_ILC_QuickFind_The_Snake/actions/workflows/blank.yml/badge.svg)

new_push.yml : Action qui se déclenche à chaque push sur la branche main pour exécuter la commande "echo "New push!""

![example workflow](https://github.com/Tebenj/4A_ILC_QuickFind_The_Snake/actions/workflows/Docker_push_GCR.yml/badge.svg)

# Workflows réalisés pour le projet : 

build_application.yml : Action qui se déclenche à chaque push. Elle va pip3 install flask dans un premier temps, puis installer la bibliothèque pandas et enfin va build notre app main.py. (Correspond à la 1ère github action demandé)

![example workflow](https://github.com/Tebenj/4A_ILC_QuickFind_The_Snake/actions/workflows/build_application.yml/badge.svg)

Docker_push_GCR.yml : Action qui se déclenche manuellement. Elle permet de dockeriser notre image. (Correspond à la 2ème github action demandé)

![example workflow](https://github.com/Tebenj/4A_ILC_QuickFind_The_Snake/actions/workflows/Docker_push_GCR.yml/badge.svg)

Docker_push_semver.yml : Action qui se déclenche à chaque release. Elle possède la même fonctionnalité que l'action précèdente mais elle permettra en plus d'ajouter le bon tag semver dans notre image poussé sur le registre (Correspond à la 3ème github action demandé)

![example workflow](https://github.com/Tebenj/4A_ILC_QuickFind_The_Snake/actions/workflows/Docker_push_semver.yml/badge.svg)
