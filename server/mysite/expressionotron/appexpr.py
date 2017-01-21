from flask import Blueprint, request, url_for
import random
from .v001.exprBuilder import buildExpression as buildExpression_001
from .v002.expr_builder import buildExpression as buildExpression_002

# http://stackoverflow.com/questions/15231359/split-python-flask-app-into-multiple-files
app_expressionotron = Blueprint('app_expressionotron', __name__)

CURRENT_EXPR_VERSION = "002"
SEPARATOR_SEED = "_"

FUNC_BUILDER_FROM_VERSION = {
    "001": buildExpression_001,
    "002": buildExpression_002,
}

def getAndIncreaseNbVisitor():
    """ Lit, puis reecrit des infos dans un fichier texte, sur le serveur.
    En esperant que si plusieurs visiteurs viennent sur le site en meme temps, ca fait pas tout planter.
    J'y connais rien, je sais du tout si c'est comme ca qu'on doit faire. Au pire, ca finira dans les except."""
    filenameVisitor = "/home/Recher/mysite/expressionotron/blorp.txt"

    try:
        fileVisitorRead = open(filenameVisitor, "r")
        strNbVisitor = fileVisitorRead.read()
        fileVisitorRead.close()
    except IOError:
        strNbVisitor = "0"

    if strNbVisitor.isdigit():
        nbVisitor = int(strNbVisitor)
    else:
        nbVisitor = 0
    nbVisitor += 1
    strNbVisitor = str(nbVisitor)

    try:
        fileVisitorWrite = open(filenameVisitor, "w")
        fileVisitorWrite.write(strNbVisitor)
        fileVisitorWrite.close()
    except IOError:
        # Woups. Fail dans la mise a jour du fichier des nombres de visites.
        # C'est pas grave, on laisse tomber.
        pass

    return nbVisitor

def getWebPageTemplate():
    # ouh que c'est vilain d'avoir mis du code HTML directement dans un fichier python !!
    # Nous ferons mieux plus tard.
    return """

    <h1>%s</h1>

    <br/>
    <h3>Partagez cette expression avec vos amis !</h3>
    <p>
        Envoyez-leur ce lien : <a href="%s">%s</a>
    </p>

    <br/>
    <h3>Vous en voulez encore ?</h3>
    <form method="GET" action="%s">
        <input type="submit" value="Oui, je veux une expression au hasard !" />
    </form>
    <form method="POST" action="%s">
        Ou bien, entrez un nombre entre 0 et beaucoup : <input name="seedInForm" />
        <br/>
        <input type="submit" value="Parce qu'en fait, je veux une expression pas au hasard !" />
        <br/>
        (pour utiliser la version pr&eacute;c&eacute;dente, ajouter "_001" apr&egrave;s votre nombre)
    </form>
    J'en veux une dose r&eacute;guli&egrave;re, tous les jours &agrave; 16:64.<br/>
    Je vais suivre ce compte twitter :
    <a href="https://twitter.com/expressionotron">https://twitter.com/expressionotron</a>

    <br/>
    <h3>Quelques liens</h3>
    <p>
        Ce truc est librement et &eacute;hont&eacute;ment inspir&eacute; de l'expressionotron de nioutaik
        <br/>
        <a href="http://www.nioutaik.fr/index.php/2007/09/06/386-l-expressionotron">http://www.nioutaik.fr/index.php/2007/09/06/386-l-expressionotron</a>
    </p>
    <p>
        Mon blog (images NSFW) : <a href="http://recher.wordpress.com">http://recher.wordpress.com</a>
        <br/>
        Mon twitter : <a href="https://twitter.com/_Recher_">https://twitter.com/_Recher_</a>
    </p>
    <p>
        Des gens biens (images NSFW non plus) : <a href="http://sametmax.com">http://sametmax.com</a>
    </p>
    <p>
        Lien &agrave; pub, qui vous fera perdre du temps de cerveau,
        <br/>
        mais qui me fera gagner des bitcoins : <a href="http://recher.pythonanywhere.com/urluth/?u=yns">http://recher.pythonanywhere.com/urluth/?u=yns</a></p>
    </p>

    <br/>
    <h3>Statistiques super utiles</h3>
    <p>
        Cette page a &eacute;t&eacute; vue %s fois.
    </p>
    """

def makeValidSeed(strSeed):
    rebuildSeed = False
    strVersion = CURRENT_EXPR_VERSION
    digest = 0

    if strSeed.isdigit():
        # On a uniquement le digest, sans la version. C'est pas grave.
        # On prend ce digest, et on utilisera la version courante
        digest =  int(strSeed)
    else:
        # On verifie que la seed respecte le format 000...000_<num_version>
        # Si ce n'est pas le cas, on prendra un digest au hasard, et la version courante.
        strDigest, sep, strVersion = strSeed.partition(SEPARATOR_SEED)
        if sep != SEPARATOR_SEED:
            rebuildSeed = True
        elif strVersion not in FUNC_BUILDER_FROM_VERSION.keys():
            rebuildSeed = True
        elif not strDigest.isdigit():
            rebuildSeed = True
        if rebuildSeed:
            strVersion = CURRENT_EXPR_VERSION
            # REC TODO : v001 = 300000000 (un peu arbitraire). v002 = 87295229100.
            # faudrait juste que ce soit pas en dur. Vilain.
            digest = random.randrange(87295229100)
        else:
            digest = int(strDigest)

    strSeed = SEPARATOR_SEED.join( (str(digest), strVersion) )
    return (strVersion, digest, strSeed)

def expressionotron(strSeed):
    nbVisitor = getAndIncreaseNbVisitor()
    (seedVersion, seedDigest, strSeed) = makeValidSeed(strSeed)
    func_builder = FUNC_BUILDER_FROM_VERSION[seedVersion]
    expression = func_builder(seedDigest)
    # http://flask.pocoo.org/docs/0.12/api/#flask.url_for
    # http://stackoverflow.com/questions/39262172/flask-nginx-url-for-external
    linkOnSelf = url_for(".expressionotronGet", _external=True, seed=strSeed)
    tupleDynamicData = (
        expression,
        linkOnSelf,
        linkOnSelf,
        url_for(".expressionotronGet"),
        url_for(".expressionotronPost"),
        str(nbVisitor))
    return getWebPageTemplate() % tupleDynamicData

@app_expressionotron.route('/', methods=['POST'])
def expressionotronPost():
    strSeed = request.form["seedInForm"]
    return expressionotron(strSeed)

@app_expressionotron.route('/', methods=['GET'])
def expressionotronGet():
    strSeed = request.args.get("seed", "")
    return expressionotron(strSeed)

