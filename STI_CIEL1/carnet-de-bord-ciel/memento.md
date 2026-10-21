**Trouver le chemin du dossier courant**

*Entrer la commande : pwd*
Elle permet d'afficher le chemin absolu du dossier dans lequel je me situe


**Afficher le contenu du dossier**

Pour afficher le contenu :
*Entrer la commande : ls*
Elle permet d'afficher le contenu du dossier dans lequel je me situe

Pour afficher le contenu avec fichier cachés :
*Entrer la commande : ls -a*
Les fichiers cachés en question sont tout ceux qui ne sont pas affichés quand on tape la commande pwd, par exemple les dossiers sont cachés.

Pour afficher le contenu avec fichier en version longue (ou détaillée) :
*Entrer la commande : ls -l*
La version longue permet de voir des informations supplémentaires, comme la date et l'heure de création d'un fichier/dossier.

Pour afficher le contenu avec fichier cachés et en version longue (ou détaillée) :
*Entrer la commande : ls -la*
Cela permet la combinaison des deux commandes.


**Affichez l'aide de la commande ls pour dévoiler ses options**

*Entrer la commande ls --help*
En ajoutant --help à une commande, on peut avoir des informations sur celle-ci.
Par exemple, ls à d'autre paramètres, tout comme -r (permet d'inverser l'ordre)


**Aller dans documents et afficher le contenu**

*Entrer la commande : cd Documents*
*Puis, entrer la commande : ls*
La commande cd permet de changer de dossier, si on veut remonter, on doit faire cd ..


**Creer un dossier**

*Entrer la commande : mkdir station_meteo*
*Puis, entrer la commande : cd station_meteo*
*Puis, entrer la commande : mkdir -p brouillon/data*
La commande mkdir permet de créer un dossier dans le dossier dans lequel on se situe. 
La commande mkdir -p permet de créer, en ajoutant des / (slash) à chaque titre de dossier, de créer des dossiers avec leurs sous dossiers.


**Creer trois dossiers en simultané**

*Vérifions qu'on soit bien dans notre dossier, on peut toujours faire la commande pwd !*
*Entrer la commande : mkdir src tests docs*
Sur la commande mkdir, on peut entrer autant de titre de dossiers que l'on veut, les dossiers seront mis dans le même dossiers, au même niveeau (à la racine).


**Creer un fichier dans brouillon et y ajouter une ligne**

*Entrer la commande : cd brouillon*
*Puis, entrer la commande touch main.py*
*Puis, entrer la commande echo "print('Station météo prête')" > main.py*
On change de dossier pour mettre notre fichier.
Notre fichier peut se créer avec la commande touch, ensuite on entre le nom qu'on veut donner à notre fichier, ainsi que son extension (.py, .txt, ...)
Enfin, on peut éditer notre fichier avec la commande echo, notre message entre guillemets vien juste après la commande, puis on ajoute une flèche > pour créer ou écraser un contenu.


**Deplacer le fichier main.py dans src et le dossier data à la racine de station meteo**

*Entrer la commande : mv main.py /Documents/station_meteo/src/*
*Puis, entrer la commande : mv data /Documents/station_meteo*
Il faut retracer le chemin entier pour aller chercher l'endroit ou veut déposer notre dossier ou fichier.


**Supprimer notre dossier brouillon**

*Entrer la commande : rm -r /Documents/station_meteo/brouillon*


**Executer un fichier**

*Entrer la commande : python /Documents/station_meteo/src/main.py*
Il faut bien veiller à retrouver notre fichier.


**Creer deux fichiers dans docs**

*Entrer la commande : touch fichier1.txt (Après être entrer dans notre dossier docs, on peut faire cela en utilisant notre commande cd puis notre chemin d'acces)*
*Entrer la commande : echo "Bonjour !" > fichier1.txt* 

*Entrer la commande : touch fichier2.txt*
*Entrer la commande : echo "Je m'appelle Léandre" > fichier2.txt*


**Fichier résultat**

*Entrer la commande : cat fichier1.txt fichier2.txt > resultat.txt*
Nous n'avons pas besoin de creer le fichier resultat, il se creer tout seul s'il n'existe pas.


**Ajouter du texte**

*Entrer la commande : echo "Fin du test" >> resultat.txt*


**Copier notre fichier**

*Entrer la commande : cp resultat.txt resultat_sauvegarde.txt*
Notre fichier se copie et s'enregistre dans un autre qu'on nomme.


**Retrouver l'historique de nos commandes**

*Entrer la commande : history*
L'historique apparait.


**Retrouver une commande**

*Pour retrouver une commande sans la retaper, on peut appuyer sur la flèche du haut*


**Trouver tout les fichiers en .py**

Il faut retourner à notre racine à Documents, pour ça, on peut retourner sur le debut de notre chemin, en faisant cd /Documents

*Entrer la commande find . -name "*.py"*

On ne trouve que main.py.

