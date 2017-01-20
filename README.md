# expressionotron
Site web générant des expressions classes "qui poutre du brontosaure triclassé au dénoyauteur de cerise".

Mais pour l'instant y'a vraiment rien dedans.

(Petite précision : les listes de morceaux de phrase ne seront pas publiées pour l'instant).


## TODO list

ajouter les fichiers de vieux_trucs et les enlever juste après, juste pour les avoir dans git

voir si on peut récupérer et versionner ce fichier
`/var/www/recher_pythonanywhere_com_wsgi.py`
(si oui, faudra aussi le versionner dans urluth)

relancer en local et repasser tous les tests, pour vérifier si c'est toujours bon

TODOs de code

 - renommage des variables et des noms de fichiers en respectant le PEP8
 - mettre des simples quote là où il faut
 - `expr_builder.py` : renommer la variables seed_digest
 - `twitBot.py` : import absolus qui font dégueu.
 - `twitBot.py` : fallback pas sérieux dans le try-except de la fonction log
 - mettre makeValidSeed dans une lib commune et s'en servir dans le twitBot et à l'autre endroit où c'est commun
 - La valeur 87295229100 ne devrait pas être un truc en dur. Et faut pas qu'elle soit écrite/calculée plusieurs fois.
 - `twitBot.py` : Le lien vers mon propre site : http://recher.pythonanywhere.com/ est en dur. Pourquoi pas (car la tâche planifiée n'a peut-être pas accès à cette info), mais dans ce cas faut que ce soit dans une sorte de lib de constantes communes.
 - `appexpr.py` : faire un template jinja2 comme il faut
 - `appexpr.py` : Là aussi, le lien vers mon site est en dur : "http://recher.pythonanywhere.com". Mais là c'est carrément vilain.


Faire la même doc que urluth :

 - readme principal
 - Exécution en local
 - Configuration dans l'hébergeur PythonAnywhere
 - Document de conception (en particulier le twitter bot)

