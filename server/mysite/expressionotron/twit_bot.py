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
        print('log impossible')

def twit_expression(unsafe_expr_gen_key=''):
    """
    milles mercis à :
    http://wilsonericn.wordpress.com/2011/08/22/tweeting-in-python-the-easy-way/
    """
    twit_try_left = MAX_TWIT_TRY
    twit_succeeded = False

    while twit_try_left and not twit_succeeded:

        seed, version) = expr_gen.sanitize_key(unsafe_expr_gen_key)
        expr_gen_key = expr_gen.format_key(seed, version)
        # TODO : claquer un format().
        log(''.join((datetime.date.today().isoformat(), ' version:', str(version), ' seed:', str(seed))))
        expression = expr_gen.generate_expression(seed, version)
        log(expression)
        # http://stackoverflow.com/a/730330
        expression = parser.unescape(expression)
        expression = expression[:NB_CHAR_LIMIT_WITHOUT_LINK]
        # TODO : claquer un format().
        # http://sametmax.com/le-formatage-des-strings-en-long-et-en-large/
        twit_text = expression + ' ' + EXPRESSIONOTRON_URL + '?seed=' + expr_gen_key
        log(twit_text)

        try:
            # TODO : nom de variable en PEP8
            my_auth = twitter.OAuth(
                twit_pass.token,
                twit_pass.tokenKey,
                twit_pass.conSecret,
                twit_pass.conSecretKey)
            twit = twitter.Twitter(auth=my_auth)
            twit.statuses.update(status=twit_text)
        except Exception as e:
            twit_try_left -= 1
            log('twit echec')
            # TODO : claquer un format().
            log(''.join(('essais restants : ', str(twit_try_left))))
            log(e)
            # Un peu inutile, mais je préfère nettoyer les variables avant
            # de faire l'essai suivant.
            my_auth = None
            twit = None
            if not twit_try_left:
                raise
        else:
            log('twit reussi')
            twit_succeeded = True

