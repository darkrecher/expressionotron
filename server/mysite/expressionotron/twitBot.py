import random
import twitter
from html.parser import HTMLParser
parser = HTMLParser()

# TODO : line too long. trop de truc importé
from expressionotron.expr_generator import sanitize_key, generate_expression, format_key
import expressionotron.twit_pass

twit_pass = expressionotron.twit_pass
conSecret = twit_pass.conSecret
conSecretKey = twit_pass.conSecretKey
token = twit_pass.token
tokenKey = twit_pass.tokenKey


# Un lien dans twitter ne prend pas trop de place. Mais je laisse une bonne marge.
# Sinon le tweet va planter, et pour l'instant, j'ai aucune gestion d'erreur sur ce point
# (Car je suis un bourrin qui code un peu a l'arrache.)
NB_CHAR_LIMIT_WITHOUT_LINK = 110
MAX_TWIT_TRY = 4

# Je suis obligé de mettre ça en constante, car la tâche planifiée dans
# pythonanywhere est indépendante des tâches du serveur flask. Donc la tâche
# planifiée ne "sait pas" l'url de la machine sur laquelle elle est exécutée
EXPRESSIONOTRON_URL = 'https://recher.pythonanywhere.com/expressionotron'

def log(logInfo):
    """ at the arrache. """
    # TODO : try except de gros sale, sans fallback digne de ce nom.
    # si jamais on essaie d'écrire sur une console qui a un encodage de merde,
    # ça devrait pas planter, mais ça fera pas quelque chose de très classe.
    # On s'en fout, c'est rien qu'une fonction de log.
    try:
        print(str(logInfo))
    except Exception as e:
        # TODO : risque aussi de planter, dans un contexte vraiment pourri.
        print("log impossible")

def twitAnExpression(unsafe_expr_gen_key=''):
    """ many thanks to http://wilsonericn.wordpress.com/2011/08/22/tweeting-in-python-the-easy-way/ """
    nbTwitTry = 0
    twitSucceeded = False
    # oui, inf ou egal, oui. voir plus loin. (alarach, quand meme. je dois avouer)
    while nbTwitTry<=MAX_TWIT_TRY and not twitSucceeded:
        log("".join(("essai numero : ", str(nbTwitTry))))
        (seedDigest, seedVersion) = sanitize_key(unsafe_expr_gen_key)
        strSeed = format_key(seedDigest, seedVersion)
        log("".join(("seedVersion:", str(seedVersion), " seedDigest:", str(seedDigest))))
        expression = generate_expression(seedDigest, seedVersion)
        log(expression)
        # http://stackoverflow.com/a/730330
        uExpr = parser.unescape(expression)
        uExpr = uExpr[:NB_CHAR_LIMIT_WITHOUT_LINK]
        # TODO : claquer un format(). et utiliser strSeed au lieu de recréer à l'arrache.
        # http://sametmax.com/le-formatage-des-strings-en-long-et-en-large/
        textTwit = uExpr + " " + EXPRESSIONOTRON_URL + "?seed=" + str(seedDigest) + "_" + str(seedVersion)
        log(textTwit)
        try:
            my_auth = twitter.OAuth(token,tokenKey,conSecret,conSecretKey)
            twit = twitter.Twitter(auth=my_auth)
            twit.statuses.update(status=textTwit)
            #a = 5 / 0
        except Exception as e:
            log("twit echec")
            log(e)
            if nbTwitTry == MAX_TWIT_TRY:
                raise
        else:
            log("twit reussi")
            twitSucceeded = True
        my_auth = None
        twit = None
        nbTwitTry += 1
