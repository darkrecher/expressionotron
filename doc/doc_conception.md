# Document de conception

La page de présentation est toute simple, pas de JS ni de CSS. Elle contient les liens vers les applications qui ont pu être chargées (en Flask, ça s'appelle des [Blueprints](http://flask.pocoo.org/docs/0.12/blueprints/)).

Le Blueprint "expressionotron" contient une page unique, générée dynamiquement, ainsi qu'une tâche planifiée.

Cette page unique affiche une expression ainsi que du texte statique. Elle ne contient pas de JS ou de CSS. Elle accepte un paramètre facultatif, qui est utilisé comme une "seed" permettant de générer une expression spécifique, en utilisant une version spécifique du générateur. Si le paramètre n'est pas présent, l'expression à afficher est générée aléatoirement.

La tâche planifiée exécute le twitter bot. Celui-ci génère aléatoirement une expression en utilisant la version courante du générateur, puis il la met dans un twit via l'API de twitter.

L'autre Blueprint (urluth) contient une page unique. Elle n'est pas décrite dans cette documentation.

Tous les fichiers mentionnés dans cette documentation se trouve dans `repo_git/expressionotron/server/mysite`, ce chemin de base n'est donc pas mentionné à chaque fichier.


## flask_app.py

Fichier principal du site.

### Démarrage du serveur

Lors de l'exécution de ce fichier, les actions suivantes sont effectuées :

 - Tentative d'importation du Blueprint "expressionotron" et stockage dans la variable `app_expressionotron`. Cette tentative est exécutée dans un bloc try-except. Si le Blueprint n'est pas présent (impossible de trouver ou d'importer les fichiers python), l'exécution ne se bloque pas, mais `app_expressionotron` vaut None.

 - Si le chargement a réussi, enregistrement du Blueprint dans le site, avec le préfixe d'url `expressionotron`. Ce qui veut dire que toutes les requêtes HTTP commençant par ce préfixe seront redirigées vers ce Blueprint.

 - Même principe avec urluth. La variable `app_urluth` contient le Blueprint "urluth", ou None si l'import a échoué.

 - Si `app_urluth` ne vaut pas None, enregistrement du Blueprint dans le site, avec le préfixe d'url `urluth`.

 - Lancement de l'application pour démarrer le serveur.

L'application doit avoir une "secret key" pour fonctionner. C'est une chaîne de caractère contenant ce qu'on veut. Je ne sais pas exactement à quoi ça sert, je suppose que c'est pour la sécurité, le HTTPS ou quelque chose comme ça. Cette secret key est importée depuis le fichier `secret_key.py`. Il y a une version de ce fichier dans ce repository, qui n'est bien évidemment pas la même que celle qui est réellement utilisée sur pythonanywhere. La vraie secret key n'est pas disponible publiquement.

### Construction et renvoi de la page de présentation du site

D'autre part, le fichier `flask_app.py` contient la fonction `generate_main_page`, qui est appelée lorsqu'il faut répondre à une requête HTTP sur l'url racine du site (juste un slash, sans préfixe). Cette fonction effectue les actions suivantes :

 - Début de la génération d'une page HTML toute simple.

 - Si le Blueprint `app_expressionotron` existe, écriture d'un lien dans la page HTML. L'url de ce lien est construite de façon à pointer vers la page unique de l'expressionotron.

 - Si le Blueprint `app_urluth` existe, écriture d'un autre lien dans la page HTML, permettant d'aller à la page unique d'urluth.

 - Renvoi de la page, sous forme d'une chaîne de caractères.

Exemple de code HTML renvoyé (lorsque les deux Blueprints sont présents) :

    Il n'y a pas grand-chose ici. Vous pouvez juste :<br/>
     - <a href="/expressionotron/">cliquez ici pour aller &agrave; l'expressionotron</a><br/>
     - <a href="/urluth/">cliquez ici pour consulter urluth</a><br/>

Pas de balise `html`, `body`, `head`, etc. C'est vraiment au plus simple.


## expressionotron/appexpr.py

Fichier principal de l'application expressionotron. Il crée le Blueprint `app_expressionotron`.

Ce fichier contient deux grosses fonctions, et deux petites fonctions de routage d'urls

### Fonction `get_and_increase_nb_visit`

Cette fonction lit, puis réécrit une information dans le fichier texte `/home/Recher/mysite/expressionotron/blorp.txt`, sur le serveur.

L'information lue est le nombre de visites de la page web (depuis la création du site sur pythonanywhere), elle est ensuite incrémentée de 1, puis réécrite dans le fichier. Le fichier contient uniquement ce nombre de visite, stockée sous forme d'une simple chaîne de caractère.

La fonction renvoie, sous forme de int, le nombre de visite après son incrémentation.

Des try-except rendent la lecture et la réécriture dans le fichier non bloquante. (L'affichage final de la page web contenant l'expression est plus important que le comptage des visites). Si la lecture échoue, le nombre de visite prend la valeur par défaut 0, qui devient 1 après incrémentation. C'est ce qui explique pourquoi les tests en local affichent toujours une seule visite, qui n'augmente jamais.

Les accès multiples au fichier ne sont pas gérés. Il est donc possible que certaines visites n'aient pas été comptabilisés, si plusieurs visiteurs arrivent exactement pil poil en même temps.

### Fonction `webpage_expressionotron`

### Fonctions de routage d'urls


## expressionotron/templates/template_expr.html


## expressionotron/common_tools.py


## Génération des expressions


### Fonctionnement générique à toutes les versions

### v001

(Ne sera pas documenté en détail, car osef, un petit peu)

### v002

### expr_generator.py


## Twitter bot

### twit_cron.py

### expressionotron/twit_pass.py

### expressionotron/twit_bot.py

