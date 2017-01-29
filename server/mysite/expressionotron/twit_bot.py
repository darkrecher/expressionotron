import logging
import datetime
import random
import twitter
from html.parser import HTMLParser

import expressionotron.expr_generator
expr_gen = expressionotron.expr_generator
import expressionotron.twit_pass
twit_pass = expressionotron.twit_pass

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')
parser = HTMLParser()

# Un lien dans twitter ne prend pas trop de place. Mais je laisse une bonne marge.
# Sinon le tweet va planter, et pour l'instant, j'ai aucune gestion d'erreur sur ce point
# (Car je suis un bourrin qui code un peu a l'arrache.)
NB_CHAR_LIMIT_WITHOUT_LINK = 110
MAX_TWIT_TRY = 4

# Je suis obligé de mettre ça en constante, car la tâche planifiée dans
# pythonanywhere est indépendante des tâches du serveur flask. Donc la tâche
# planifiée ne "sait pas" l'url de la machine sur laquelle elle est exécutée.
EXPRESSIONOTRON_URL = 'https://recher.pythonanywhere.com/expressionotron'


def twit_expression(unsafe_expr_gen_key=''):
    """
    milles mercis à :
    http://wilsonericn.wordpress.com/2011/08/22/tweeting-in-python-the-easy-way/
    """
    twit_try_left = MAX_TWIT_TRY
    twit_succeeded = False

    while twit_try_left and not twit_succeeded:

        (seed, version) = expr_gen.sanitize_key(unsafe_expr_gen_key)
        expr_gen_key = expr_gen.format_key(seed, version)
        logging.debug('%s version: %s seed: %s' % (
            datetime.date.today().isoformat(),
            version,
            seed))
        expression = expr_gen.generate_expression(seed, version)
        logging.debug(expression)
        # http://stackoverflow.com/a/730330
        expression = parser.unescape(expression)
        expression = expression[:NB_CHAR_LIMIT_WITHOUT_LINK]
        # http://sametmax.com/le-formatage-des-strings-en-long-et-en-large/
        twit_text = '%s %s?seed=%s' % (
            expression,
            EXPRESSIONOTRON_URL,
            expr_gen_key)
        logging.debug(twit_text)

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
            logging.error('twit echec')
            logging.error('essais restants: %s' % twit_try_left)
            logging.error(e)
            # Un peu inutile, mais je préfère nettoyer les variables avant
            # de faire l'essai suivant.
            my_auth = None
            twit = None
            if not twit_try_left:
                raise
        else:
            logging.debug('twit reussi')
            twit_succeeded = True

