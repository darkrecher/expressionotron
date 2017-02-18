# Document de conception

Les pages de l'expressionotron ne contiennent ni JS, ni CSS.

La page de présentation est toute simple, elle contient les liens vers les applications qui ont pu être chargées (en Flask, ça s'appelle des [Blueprints](http://flask.pocoo.org/docs/0.12/blueprints/)).

Le Blueprint "expressionotron" contient une page unique, générée dynamiquement, ainsi qu'une tâche planifiée.

Cette page unique affiche une expression ainsi que du texte. Elle accepte un paramètre facultatif contenant une "seed" et une version, ce qui permet de générer une expression spécifique. Si le paramètre n'est pas présent, l'expression est générée aléatoirement, avec la version courante du générateur.

La tâche planifiée exécute le twitter bot. Celui-ci génère aléatoirement une expression, puis il l'envoie dans un twit via l'API de twitter.

L'autre Blueprint (urluth) contient également une page unique. Il n'est pas décrit dans cette documentation.

Tous les fichiers mentionnés dans cette documentation se trouve dans `repo_git/expressionotron/server/mysite`, ce chemin de base n'est donc pas reprécisé à chaque fois.


## flask_app.py

Fichier principal du site.

### Démarrage du serveur

Lors de l'exécution de ce fichier, les actions suivantes sont effectuées :

 - Tentative d'importation du Blueprint "expressionotron" et stockage dans la variable `app_expressionotron`. Cette tentative est exécutée dans un bloc try-except. Si le Blueprint n'est pas présent (impossible de trouver ou d'importer les fichiers python), l'exécution ne se bloque pas, mais `app_expressionotron` vaut None.

 - Si le chargement a réussi, enregistrement du Blueprint dans le site, avec le préfixe d'url `expressionotron`. Ce qui veut dire que toutes les requêtes HTTP commençant par ce préfixe seront redirigées vers ce Blueprint.

 - Même principe avec urluth. La variable `app_urluth` contient le Blueprint "urluth", ou None si l'import a échoué.

 - Si `app_urluth` ne vaut pas None, enregistrement du Blueprint dans le site, avec le préfixe d'url `urluth`.

 - Lancement de l'application pour démarrer le serveur.

L'application doit avoir une "secret key" pour fonctionner. C'est une chaîne de caractère contenant ce qu'on veut. Je ne sais pas exactement à quoi ça sert, je suppose que c'est pour la sécurité, le HTTPS ou quelque chose comme ça. Cette secret key est importée depuis le fichier `secret_key.py`. Il y a une version de ce fichier dans ce repository, qui n'est bien évidemment pas la même que celle réellement utilisée sur pythonanywhere. La vraie secret key n'est pas disponible publiquement.

### Construction et renvoi de la page de présentation du site

D'autre part, le fichier `flask_app.py` contient la fonction `generate_main_page`, qui est appelée lorsqu'il faut répondre à une requête HTTP sur l'url racine du site (juste un slash, sans préfixe). Cette fonction effectue les actions suivantes :

 - Début de la génération d'une page HTML toute simple.

 - Si le Blueprint `app_expressionotron` existe, écriture d'un lien dans la page HTML. L'url de ce lien est construite de façon à pointer vers la page unique de l'expressionotron.

 - De même, si le Blueprint `app_urluth` existe, écriture d'un autre lien dans la page HTML.

 - Renvoi de la page, sous forme d'une chaîne de caractères.

Exemple de code HTML renvoyé (lorsque les deux Blueprints sont présents) :

    Il n'y a pas grand-chose ici. Vous pouvez juste :<br/>
     - <a href="/expressionotron/">cliquez ici pour aller &agrave; l'expressionotron</a><br/>
     - <a href="/urluth/">cliquez ici pour consulter urluth</a><br/>

Pas de balise `html`, `body`, `head`, etc. C'est vraiment au plus simple.


## expressionotron/appexpr.py

Fichier principal de l'application expressionotron. Il crée le Blueprint `app_expressionotron`.

Ce fichier contient deux grosses fonctions et deux petites fonctions de routage d'urls.

### Fonction `get_and_increase_nb_visit`

Cette fonction lit, puis réécrit une information dans le fichier texte `/home/Recher/mysite/expressionotron/blorp.txt`, sur le serveur.

L'information lue est le nombre de visites de la page web (depuis la création du site sur pythonanywhere), elle est ensuite incrémentée de 1, puis réécrite dans le fichier. Le fichier contient uniquement ce nombre de visite, stockée sous forme d'une simple chaîne de caractère.

La fonction renvoie, sous forme de int, le nombre de visite après son incrémentation.

Des try-except rendent la lecture et la réécriture dans le fichier non bloquante. (L'affichage final de la page web est plus important que le comptage des visites). Si la lecture échoue, le nombre de visite prend la valeur par défaut 0, qui devient 1 après incrémentation. C'est ce qui explique pourquoi les tests en local affichent toujours "1", sans que ça n'augmente.

Les accès multiples au fichier ne sont pas gérés. Il est donc possible que certaines visites n'aient pas été comptabilisées.

### Fonction `webpage_expressionotron`

C'est la "fonction principale" de l'expressionotron, elle construit son unique page HTML. Celle-ci est générée et renvoyée avec le moteur de template "jinja2", intégré à Flask. Le fichier de template utilisé est `expressionotron/templates/template_expr.html`.

Elle nécessite le paramètre `unsafe_expr_gen_key` : une chaîne de caractère censée définir la seed et la version de l'expression à générer (voir plus loin). Ce paramètre provient de l'extérieur, car c'est une information contenue dans la requête HTTP. Il peut donc potentiellement contenir n'importe quoi, être vide, etc. La fonction en tient compte.

La fonction effectue les actions suivantes :

 - augmentation du nombre de visite du site, et récupération du nombre actuel.
 - création d'une seed et d'une version de générateur correcte en utilisant, si c'est possible, les infos de `unsafe_expr_gen_key`.
 - génération de l'expression. Cellec-ci est déjà encodée en HTML, avec les `&eacute;`, etc.
 - génération d'un permalink permettant de retrouver l'expression. Pour plus d'info concernant la méthode de génération des urls, voir : http://flask.pocoo.org/docs/0.12/api/#flask.url_for et http://stackoverflow.com/questions/7478366/create-dynamic-urls-in-flask-with-url-for .
 - génération de la page HTML avec le template et toutes les infos précédentes.

### Fonctions de routage d'urls

Il s'agit des fonctions `expressionotron_post` et `expressionotron_get`. Elles sont censées répondre à une requête HTTP ayant l'url "/" (url racine). Dans les faits, l'url de départ est "/expressionotron". Le fichier `flask_app.py` l'intercepte et détecte la présence du préfixe. Ce préfixe est supprimé, puis la requête est transmise à `appexpr.py`. L'url résultante est donc l'url racine, qui est interceptée par l'une de ces deux fonctions.

La fonction `expressionotron_get` est associée à la méthode HTTP "GET". Le paramètre `unsafe_expr_gen_key` est récupéré depuis le paramètre HTTP "seed", contenu dans l'url. Si "seed" n'est pas présent, `unsafe_expr_gen_key` devient une chaîne vide. Le reste du code est capable de gérer ce cas.

La fonction `expressionotron_post` est associée à la méthode HTTP "POST". Le paramètre `unsafe_expr_gen_key` est récupéré depuis le paramètre de formulaire "seedInForm".

Comme c'est un POST, ce paramètre est censé être toujours présent. S'il ne l'est pas, une exception est levée et le résultat final est une erreur HTTP 400. J'aurais pu faire en sorte que ce cas soit mieux géré, mais il n'y a que maintenant que je le découvre. Tant pis, ce sera pour la prochaine version !


## expressionotron/templates/template_expr.html

Template de la page HTML. Il est assez simple.

La variable de template dans laquelle est placée l'expression est notée `{{expression|safe}}`. Le "safe" permet d'indiquer que le texte est déjà encodé en HTML. Sinon, les `&eacute;` de l'expression seraient re-convertis en `&amp;eacute;`

Le template contient un formulaire avec un champ de type texte, intitulé "seedInForm". C'est ce formulaire qui permet de faire une requête "POST", qui sera ensuite récupérée par la fonction `expressionotron_post`.

**Attention aux noms des fichiers de templates !!** Dans Flask, lorsqu'on déclare un répertoire de templates via la fonction `Blueprint(template_folder='aaa')`, celui-ci est globalement accessible, y compris par les autres Blueprint.

Par exemple, avec l'arborescence suivante :

 - mysite
   + expressionotron
     * templates
       - template.html
   + urluth
     * templates
       - template.html

Si chaque Blueprint déclare son propre sous-répertoire "templates", ça risque de se mélanger. C'est à dire que les pages de urluth seront générées avec le template de l'expressionotron, et vice-versa.

Pour régler ce problème, les deux templates ont des noms différents : `template_expr.html` et `template_urluth.html`. On aurait pu également créer un sous-dossier dans chaque dossier de template.

Pour plus de précisions concernant cette subtilité de templates : http://stackoverflow.com/questions/7974771/flask-blueprint-template-folder


## expressionotron/common_tools.py

Contient une seule fonction toute simple, utilisée un peu partout (y compris dans les scripts de tests).

Fonction `tuple_from_raw_str` : Renvoie un tuple à partir d'une string multi-ligne, en éliminant les espaces avant et après chaque string, et en éliminant les lignes vides.


## Génération des expressions

### Fonctionnement générique à toutes les versions

Chaque version du générateur d'expression est placée dans un sous-répertoire. Pour l'instant, il y en a deux : "expressionotron/v001" et "expressionotron/v002".

Rien n'est imposé concernant l'organisation interne d'un sous-répertoire de version, excepté qu'il doit obligatoirement comporter un fichier `expr_generator.py`, avec les éléments suivants :

 - `version` : chaîne de caractère. Indique la version du générateur.
 - `generate_expression` : fonction nécessitant un paramètre `seed` (valeur numérique) et renvoyant une chaîne de caractère (l'expression). La même seed doit toujours renvoyer la même expression. L'expression doit être encodée avec les HTML entities (`&eacute;`, etc.).
 - `seed_max` : valeur numérique. Elle renseigne sur la quantité d'expression qui peuvent être générées. Idéalement, si on fait varier le paramètre `seed` de 0 à `seed_max`, on devrait couvrir toutes les expressions possibles, sans qu'il y ait de doublons. Concrètement, cette consigne est respectée pour la version 'v002', mais pas la 'v001'.

En général, les morceaux de phrase des expressions sont tous stockés dans un fichier `dataphrase.py`, mais ce n'est pas une obligation.

### expressionotron/v001

La première version du générateur. Elle n'est pas documentée en détail, car son code est un peu moche, et il n'est pas prévu de le modifier.

Sa version vaut `001`. Son seed_max vaut 300000000, mais c'est une valeur arbitraire.

### expresionotron/v002

#### Structure d'une expression

La génération d'une expression est effectuée en prenant un élément dans chacune des 5 listes suivantes : verbe, sujet, adjectif, n'importe quoi, interjection.

Il y a également un éventuel préfixe à l'adjectif, mais celui-ci n'est pas totalement pris au hasard, et il ne dépend pas directement de la seed (voir plus loin).

Exemple :

> Ça broute-minoutte du space marine interopérable au shpocker !! Même que !!1!

 - verbe = Ça broute-minoutte
 - sujet = du space marine
 - adjectif = interopérable
 - n'importe quoi = au shpocker
 - interjection = Même que

Les points d'exclamation et le "1" sont fixe, et ajoutés systématiquement à chaque expression.

La génération d'une expression consiste donc, à partir de la seed, à choisir un numéro d'élément dans chaque liste.

Sa version vaut `002`. Son seed_max est égal au produit de la taille des 5 listes d'éléments, soit : 151 * 141 * 173 * 158 * 150 = 87295229100.

#### Méthode de sélection des éléments à partir de la seed

Pour les exemples de ce chapitre, on va supposer que chaque liste comporte seulement 3 éléments.

La méthode de sélection la plus simple serait la suivante :

    seed = 0 -> index des éléments = [0, 0, 0, 0, 0]
    -> on prend le verbe numéro 0, le sujet 0, l'adjectif 0, le n'importe quoi 0 et l'interjection 0.

    seed = 1 -> [0, 0, 0, 0, 1]
    seed = 2 -> [0, 0, 0, 0, 2]
    seed = 3 -> [0, 0, 0, 1, 0]
    seed = 4 -> [0, 0, 0, 1, 1]
    ...

Mais ce ne serait pas très amusant, car ça voudrait dire que deux seeds proches génèrent deux phrases très semblables. Par exemple, entre seed=0 et seed=1, seule l'interjection change.

Pour régler ce problème, on peut décider de faire avancer tous les index à chaque itération. Une fois qu'un "tour d'index" a été fait, on les fait tous avancer sauf le premier (afin de créer un décalage), puis on refait tout avancer de un, et ainsi de suite. Le tout en prenant en compte les remise de compteur à 0 lorsqu'un index est dépassé.

Ça donnerait donc quelque chose comme ça :

    seed = 0 -> [0, 0, 0, 0, 0]
    seed = 1 -> [1, 1, 1, 1, 1]
    seed = 2 -> [2, 2, 2, 2, 2]

Là, on remet à 0, et on fait tout avancer de 1 sauf le premier index.

    seed = 3 -> [0, 1, 1, 1, 1]

On refait un tour.

    seed = 4 -> [1, 2, 2, 2, 2]
    seed = 5 -> [2, 0, 0, 0, 0]

On a fini le tour. On re-remet à 0 et on fait tout avancer de 2 sauf le premier index.

    seed = 6 -> [0, 2, 2, 2, 2]

On refait un tour.

    seed = 7 -> [1, 0, 0, 0, 0]
    seed = 8 -> [2, 1, 1, 1, 1]

Si on refait pareil mais en faisant tout avancer de 3 sauf le premier index, on retombera sur une sélection existante. Donc on remet à 0 et on crée un décalage un cran plus loin : on fait tout avancer de 1 sauf les deux premiers.

    seed = 9 -> [0, 0, 1, 1, 1]
    seed =10 -> [1, 1, 2, 2, 2]
    seed =11 -> [2, 2, 0, 0, 0]

Là, on peut revenir sur un décalage comme avant. On fait tout avancer de 1 sauf le premier. Et ainsi de suite.

Pour avoir encore plus d'aléatoire, on mélange les valeurs d'avancement. Au lieu d'avancer de 1 à chaque fois, on prend un peu n'importe quel index. On mélange également les valeurs d'avancement lorsqu'on fait des décalages. Il suffit de s'assurer que même mélangé, tous les index possibles sont couverts.

Ce mélange supplémentaire est effectué par des "shufflers". Il y a un shuffler par liste d'élément. Il s'agit d'une suite de nombre indiquant dans quelle ordre prendre les index.

Par exemple, si la première liste a pour shufflers [2, 1, 0] et la deuxième [1, 0, 2]. (les autres ne sont pas shufflées, sinon ça va encore plus compliquer l'exemple).

    seed= 0 -> [2, 0 (2+1), 0 (2+1), 0 (2+1), 0 (2+1)]
    seed= 1 -> [1, 2 (1+1), 2 (1+1), 2 (1+1), 2 (1+1)]
    seed= 2 -> [0, 1 (0+1), 1 (0+1), 1 (0+1), 1 (0+1)]

On remet à 0 et on fait tout avancer de un sauf le premier, en utilisant le deuxième shuffler.

    seed= 3 -> [2, 2 (2+0), 2 (2+0), 2 (2+0), 2 (2+0)]
    seed= 4 -> [1, 1 (1+0), 1 (1+0), 1 (1+0), 1 (1+0)]
    seed= 4 -> [0, 0 (0+0), 0 (0+0), 0 (0+0), 0 (0+0)]

Cette méthode à la garantie de couvrir toutes les valeurs possibles, tout en maximisant les différences entre deux seeds proches. (Je suppose qu'il faudrait une petite démo de matheux pour prouver tout ça, mais j'ai pas le temps ni les compétences pour la faire).

#### Gestion du préfixe d'adjectif

Les préfixes d'adjectifs, c'est amusant, mais il ne faut en mettre que sur les adjectifs composés d'un seul mot, sinon ça fait bizarre. De plus, il ne faut pas en mettre systématiquement, car ça serait un peu lourd. Les phrases sont déjà assez chargées de lolitude même sans préfixe.

D'après des estimations effectuées au pifomètre, il a été établi que le bon dosage de lol serait atteint lorsqu'un préfixe est ajouté dans un cas sur trois (après exclusion des cas où l'adjectif est composés de plusieurs mots).

Mais si on ajoute un index en plus pour gérer les préfixes, qui prendrait en compte les cas où on n'en met pas, on risque de se retrouver avec deux seeds différentes qui généreraient la même expression, et je voulais éviter ça.

C'est pour ça que j'ai ajouté les interjections (qui n'étaient pas du tout présentes dans la version 001 du générateur).

On utilise l'index de l'interjection pour déterminer s'il faut ajouter un préfixe ou pas, et quel préfixe ajouter. La méthode est assez simple, si `index_interjection` ne dépasse pas le nombre de préfixes possibles, alors : `index_prefixe = index_interjection`, sinon pas de préfixe.

Il y a environ trois fois plus d'interjections que de préfixes. C'est fait exprès pour mettre un préfixe dans un cas sur trois.

Du coup, on ne peut pas avoir toutes les combinaisons possibles de couples (interjections, préfixes). Mais on s'en fout. Les interjections ont été ajoutées pour permettre une probabilité de 1 préfixe sur 3.

#### Implémentation

La sélection des index d'éléments à partir de la seed est effectuée par la fonction `data_indexes_from_seed`, dans le fichier `expressionotron/v002/seeder.py`.

Il n'y a pas de contrôle sur la valeur de la seed. Si elle est trop grande par rapport aux `data_lengths`, ça se règle tout seul. Car on applique des opérations successives de modulo sur la seed pour obtenir les `data_indexes`.

Les shufflers sont à fournir en paramètre à la fonction. Ce paramètre est facultatif, puisque la méthode de sélection marcherait sans les shufflers.

Pour plus de détails, voir les commentaires de la fonction.

Le reste de l'algorithme est implémenté dans le module `expressionotron/v002/expr_generator.py`. Il effectue les actions suivantes.

 - au chargement du module : détermination des shufflers, de manière aléatoire, mais avec une seed de shufflers fixe. C'est à dire qu'on obtient les mêmes shufflers à chaque chargement du module.
 - Lors d'un appel à la fonction `generate_expression` :
   + Sélection des index d'éléments à partir de la seed passée en paramètre.
   + Récupération des éléments d'expression à partir des index d'éléments.
   + Appel de la fonction `_get_adjective_prefix`. Cette fonction renvoie None (pas de préfixe d'adjectif) ou bien le préfixe choisi.
   + Construction de l'expression en assemblant tous les éléments ensemble (avec ou sans préfixe).
   + Renvoi de l'expression.

Pour plus de détails, voir les commentaires dans le module.

### expressionotron/expr_generator.py

Ce module fait l'interface entre d'une part les différentes versions du générateur d'expression et d'autre part le code extérieur. Il a le même nom que les modules `expr_generator.py` des sous-répertoires `v001`, `v002`, ... C'est fait exprès.

Les commentaires au début du module expliquent les différentes données manipulées : `expr_gen_key`, `seed`, `version`, ...

Ce module contient les fonctions suivantes :

`sanitize_key` : crée une `expr_gen_key` correcte à partir de `unsafe_expr_gen_key`, une chaîne de caractère quelconque. Si la chaîne ne contient pas toutes les informations nécessaires, la version choisie est la plus récente (002), et la seed est choisie au hasard entre 0 et `seed_max`.

`generate_expression` : détermine le générateur d'expression à utiliser, en fonction du paramètre `version`, et exécute sa fonction de génération, afin de renvoyer l'expression. Les différentes versions du générateur nécessite uniquement le paramètre `seed`. Il n'est pas nécessaire de leur transmettre le paramètre `version`.

`format_key` : recrée une `expr_gen_key` correcte à partir d'une `seed` et d'une `version`. C'est utile pour créer un permalien vers l'expression.


## Le twitter bot

### twit_cron.py

Script tout simple, qui importe le code du twitter bot et qui exécute la fonction principale pour émettre un twit.

L'hébergeur pythonanywhere est configuré avec une tâche planifiée quotidienne, qui exécute ce script.

### expressionotron/twit_pass.py

Module tout simple lui aussi, contenant uniquement la définitio nde 4 variables. Il s'agit des clés secrètes de l'API twitter, qui correspondent au compte que le twitter bot va utiliser pour émettre les twits.

L'utilisation d'un compte de manière automatisée, via l'API, ne nécessite pas le mot de passe du compte, mais les clés de l'API (qui sont récupérables après s'être connectés au compte).

Pour plus de détail sur la manière de récupérer les clés, voir : https://wilsonericn.wordpress.com/2011/08/22/tweeting-in-python-the-easy-way/ .

Au cas où le lien se perdrait, le contenu de la page a été sauvegardé dans ce repository. Voir : `repo_git/expressionotron/doc/tweeting_in_python_the_easy_way.md`.

Bien évidemment, le fichier stocké dans ce repository ne contient pas les vraies clés, mais des valeurs fictives. Les vraies clés sont stockées uniquement sur le site pythonanywhere et ne sont pas disponibles publiquement. (Pas la peine de fouiller l'historique de git, je n'y ai jamais mis ces clés !).

### expressionotron/twit_bot.py

Module principale du twitter bot.

Il effectue les actions suivantes :

 - Vérification que les clés d'API ne sont pas les clés bidons du repository. Dans le cas contraire, envoi d'un message d'avertissement sur la sortie standard.
 - Démarrage d'une boucle, afin de tester plusieurs fois de suite l'émission d'un twit. (Comme c'est une action nécessitant un ters externe, on considère que sa réussite n'est pas garantie, donc ça vaut le coup de le tenter plusieurs fois).
 - Génération d'une expression. Le fichier `twit_cron.py` ne définit pas le paramètre facultatif lors de l'exécution de la fonction `twit_expression`. La clé de génération d'expression est donc vide. Dans ce cas, le générateur utilise la version courante ('002') et une seed aléatoire.
 - Récupération de la clé de génération d'expression (pour faire un permalink).
 - Conversion de l'expression encodée en HTML en une string en unicode.
 - Définition du texte du twit, avec l'expression unicode et le permalink (qui est déjà en unicode dès le départ), en tronquant le texte de l'expression si nécessaire. Le texte d'un twit peut comporter 180 caractères, mais il faut laisser de la marge pour le permalink (qui est plus important que l'expression). L'expression est donc tronquée arbitrairement à 110 caractères.
 - Envoi du twit, via un appel à l'API twitter, via-via la librairie python 'twitter'. Cet envoi est effectué dans un bloc try-except, car c'est ça qui a le plus de chances d'échouer.
 - Si exception (on catche tout), écriture du message d'erreur dans le log de pythonanywhere, et retour au début de la boucle : on génère une nouvelle expression, que l'on tente de retweeter.
 - Si pas d'exception, tout va bien, on sort tout de suite de la boucle, et on termine la fonction.

La boucle compte le nombre d'essais restant, au bout de 4 essais, on abandonne. On re-raise l'exception qui a été levée et qui a provoqué l'échec du twit, afin de quitter directement le processus et de permettre éventuellement à du code extérieur de récupérer cette exception pour en faire ce qu'il veut.

Durant toutes ces étapes, du log est écrit dans la sortie standard (texte de l'expression, texte du twit, message de l'exception, ...). Ce log est effectué à l'aide de la librairie standard `logging`. Il est accessible à l'adresse "recher.pythonanywhere.com.error.log" (non accessible publiquement). Je ne sais pas exactement où atterrit le log dans l'arborescence de fichier de pythonanywhere, mais l'important est qu'il soit récupérable.

## Modules non documentés

Les tests sont non documentés. Il s'agit des fichiers suivants :

    test_dataphrase_v2.py
    test_expre_v1.py
    test_expre_v2.py
    test_seeder_v2.py

Le fichier `sort_data.py` n'est pas documenté non plus. Il a été utilisé ponctuellement, pour classer par ordre alphabétique tous les éléments constitutifs des expressions. Le but était de parcourir manuellement cette liste classée afin de repérer les doublons, les fautes d'orthographe, etc.

Tous ces fichiers ne sont pas indispensable pour le fonctionnement du site, et n'ont pas été placés sur le serveur de pythonanywhere.


