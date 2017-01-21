# expressionotron
Site web générant des expressions classes "qui poutre du brontosaure triclassé au dénoyauteur de cerise".

Mais pour l'instant y'a vraiment rien dedans.

(Petite précision : les listes de morceaux de phrase ne seront pas publiées pour l'instant).


## TODO list

TODOs de code :

 - mettre makeValidSeed dans une lib commune et s'en servir dans le twitBot et à l'autre endroit où c'est commun
 - `twitBot.py` : import absolus qui font dégueu.
 - `appexpr.py` : faire un template jinja2 comme il faut
 - La valeur 87295229100 ne devrait pas être un truc en dur. Et faut pas qu'elle soit écrite/calculée plusieurs fois.
 - `test_expre_v2.py` : y'a du code à factoriser.
 - renommage des variables et des noms de fichiers en respectant le PEP8
 - mettre des simples quote là où il faut
 - `expr_builder.py` : renommer la variables seed_digest
 - `twitBot.py` : fallback pas sérieux dans le try-except de la fonction log

Faire la même doc que urluth :

 - readme principal
 - Exécution en local
 - Configuration dans l'hébergeur PythonAnywhere
 - Document de conception (en particulier le twitter bot)

