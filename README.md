# Expressionotron


## Description

Site web générant des expressions amusantes "qui poutrent du brontosaure triclassé au dénoyauteur de cerise".

Le site possède également un "twitter bot" : une tâche planifiée se déclenchant une fois par jour, pour générer une expression qui est ensuite envoyée dans un tweet.


## Installation actuelle en production

Le site fonctionne sur un serveur Flask.

Il est actuellement en production sur la plate-forme d'hébergement pythonanywhere, à l'adresse : [http://recher.pythonanywhere.com/](http://recher.pythonanywhere.com/).

Le code n'est pas exactement le même, car Pythonanywhere héberge deux applications différente, qui sont chacune dans un "Blueprint" :

 - urluth (https://github.com/darkrecher/urluth).
 - expressionotron.

Ce repository contient uniquement le code de l'application expressionotron, ainsi que le fichier python principal `repo_git/expressionotron/server/mysite/flask_app.py`.


## Exécution en local

Voir : [doc/exec_en_local.md](doc/exec_en_local.md)


## Configuration dans l'hébergeur PythonAnywhere

Voir : [doc/mise_en_prod_pythonanywhere.md](doc/mise_en_prod_pythonanywhere.md)


## Document de conception

REC TODO


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

 - Document de conception, avec en particulier :
     - le twitter bot.
     - Ce truc là dans la v002 : "Il n'y a pas les adj_prefixes dans le tuple sur lequel on boucle, c'est normal. On ne les choisit pas raiment aléatoirement. Enfin si, mais pas directement aléatoirement."
     - y'a pas de check sur la valeur max de la seed, ni de modulo, car ça se fait tout seul. (Faut juste retrouver comment)
     - le coup des templates qui doivent être nommés différemment même si ils sont pas dans le même rep : http://stackoverflow.com/questions/7974771/flask-blueprint-template-folder
 - Les liens dans le readme principal

