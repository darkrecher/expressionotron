import datetime
import random
import twitter
from html.parser import HTMLParser
import expressionotron.expr_generator
expr_gen = expressionotron.expr_generator
import expressionotron.twit_pass
twit_pass = expressionotron.twit_pass


parser = HTMLParser()

# Un lien dans twitter ne prend pas trop de place. Mais je laisse une bonne marge.
# Sinon le tweet va planter, et pour l'instant, j'ai aucune gestion d'erreur sur ce point
# (Car je suis un bourrin qui code un peu a l'arrache.)
NB_CHAR_LIMIT_WITHOUT_LINK = 110
MAX_TWIT_TRY = 4

# Je suis obligé de mettre ça en constante, car la tâche planifiée dans
# pythonanywhere est indépendante des tâches du serveur flask. Donc la tâche
# planifiée ne "sait pas" l'url de la machine sur laquelle elle est exécutée
EXPRESSIONOTRON_URL = 'https://recher.pythonanywhere.com/expressionotron'

def log(log_data):
    """ at the arrache. """
    # TODO : try except de gros sale, sans fallback digne de ce nom.
    # si jamais on essaie d'écrire sur une console qui a un encodage de merde,
    # ça devrait pas planter, mais ça fera pas quelque chose de très classe.
    # On s'en fout, c'est rien qu'une fonction de log.
    try:
        print(str(log_data))
    except Exception as e:
        # TODO : risque aussi de planter, dans un contexte vraiment pourri.
        print("log impossible")

def twit_expression(unsafe_expr_gen_key=''):
    """ many thanks to http://wilsonericn.wordpress.com/2011/08/22/tweeting-in-python-the-easy-way/ """
    nbTwitTry = 0
    twitSucceeded = False
    # oui, inf ou egal, oui. voir plus loin. (alarach, quand meme. je dois avouer)
    while nbTwitTry<=MAX_TWIT_TRY and not twitSucceeded:
        # TODO : claquer un format().
        log("".join(("essai numero : ", str(nbTwitTry))))
        (seed, version) = expr_gen.sanitize_key(unsafe_expr_gen_key)
        expr_gen_key = expr_gen.format_key(seed, version)
        # TODO : claquer un format().
        log("".join((datetime.date.today().isoformat(), " version:", str(version), " seed:", str(seed))))
        expression = expr_gen.generate_expression(seed, version)
        log(expression)
        # http://stackoverflow.com/a/730330
        uExpr = parser.unescape(expression)
        uExpr = uExpr[:NB_CHAR_LIMIT_WITHOUT_LINK]
        # TODO : claquer un format(). et utiliser expr_gen_key au lieu de recréer à l'arrache.
        # http://sametmax.com/le-formatage-des-strings-en-long-et-en-large/
        textTwit = uExpr + " " + EXPRESSIONOTRON_URL + "?seed=" + str(seed) + "_" + str(version)
        log(textTwit)
        try:
            my_auth = twitter.OAuth(
                twit_pass.token,
                twit_pass.tokenKey,
                twit_pass.conSecret,
                twit_pass.conSecretKey)
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
