import random
import twitter
from html.parser import HTMLParser
parser = HTMLParser()

# REC TODO : import absolus qui font dégueu.
import expressionotron.v002.expr_builder
import expressionotron.twit_pass

exprBuilder = expressionotron.v002.expr_builder
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

def twitAnExpression(seedVersion="002", seedDigest=None):
    """ many thanks to http://wilsonericn.wordpress.com/2011/08/22/tweeting-in-python-the-easy-way/ """
    nbTwitTry = 0
    twitSucceeded = False
    chooseRandomDigest = seedDigest is None
    # oui, inf ou egal, oui. voir plus loin. (alarach, quand meme. je dois avouer)
    while nbTwitTry<=MAX_TWIT_TRY and not twitSucceeded:
        log("".join(("essai numero : ", str(nbTwitTry))))
        # TODO : appeler makeValidSeed ici, quand on l'aura mis dans une lib commune.
        if chooseRandomDigest:
            # REC TODO : v001 = 300000000 (un peu arbitraire). v002 = 87295229100.
            # Faudrait juste que ce soit pas en dur. Vilain.
            seedDigest = random.randrange(87295229100)
        log("".join(("seedVersion:", str(seedVersion), " seedDigest:", str(seedDigest))))
        expression = exprBuilder.buildExpression(seedDigest)
        log(expression)
        # http://stackoverflow.com/a/730330
        uExpr = parser.unescape(expression)
        uExpr = uExpr[:NB_CHAR_LIMIT_WITHOUT_LINK]
        # TODO : lien vers mon propre site ecrit en dur, a l'arrache. Arranger ca a l'occasion.
        textTwit = uExpr + u" http://recher.pythonanywhere.com/expressionotron?seed=" + str(seedDigest) + "_" + str(seedVersion)
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
