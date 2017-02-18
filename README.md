# Expressionotron


Site web générant des expressions amusantes "qui poutrent du brontosaure triclassé au dénoyauteur de cerise".

Le site possède également un "twitter bot" : une tâche planifiée se déclenchant une fois par jour, pour générer une expression et l'envoyer dans un tweet.


## Installation actuelle

Le site fonctionne sur un serveur Python, avec la lib Flask.

Il est actuellement en production sur la plate-forme d'hébergement [pythonanywhere](http://recher.pythonanywhere.com/).

Le code n'est pas exactement le même entre ce repository et la production, car pythonanywhere héberge deux applications différente, qui sont chacune dans un "Blueprint" :

 - urluth (https://github.com/darkrecher/urluth).
 - expressionotron.

Ce repository contient uniquement le code de l'application expressionotron, ainsi que le fichier python principal `repo_git/expressionotron/server/mysite/flask_app.py`.


## Exécution en local

Voir : [doc/exec_en_local.md](doc/exec_en_local.md)


## Configuration dans l'hébergeur PythonAnywhere

Voir : [doc/mise_en_prod_pythonanywhere.md](doc/mise_en_prod_pythonanywhere.md)


## Document de conception

Voir : [doc/doc_conception.md](doc/doc_conception.md)


## Crédits

Créé par Réchèr.

Le code et cette doc sont sous une double licence : Art Libre ou Creative Commons CC-BY (au choix). N'hésitez pas à en faire ce que vous voulez.

Repository : https://github.com/darkrecher/expressionotron

Mon blog : http://recher.wordpress.com

J'accepte les dons en diverses crypto-monnaies.

 - Bitcoin (BTC) : 12wF4PWLeVAoaU1ozD1cnQprSiKr6dYW1G
 - Litecoin (LTC) : LQfceQahHPwXS9ByKF8NtdT4TJeQoDWTaF
 - Dogecoin (Ð) : DKQUVP7on5K6stnLffKp3mHJor3nzYTLnS
 - Next (NXT) : 12693681966999686910


## TODO list

Faire la même doc que urluth :

 - relire tout ce bazar.
