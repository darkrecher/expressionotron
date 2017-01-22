from flask import Blueprint, request, url_for, render_template
import expressionotron.expr_generator
expr_gen = expressionotron.expr_generator


# http://stackoverflow.com/questions/15231359/split-python-flask-app-into-multiple-files
# http://flask.pocoo.org/docs/0.11/api/#flask.render_template
# http://flask.pocoo.org/docs/0.11/blueprints/
app_expressionotron = Blueprint(
    'app_expressionotron',
    __name__,
    template_folder='templates')


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


def expressionotron(unsafe_expr_gen_key):
    nbVisitor = getAndIncreaseNbVisitor()
    (seed, version) = expr_gen.sanitize_key(unsafe_expr_gen_key)
    # la chaîne de caractère 'expression' est déjà encodée en HTML
    # (avec les &eacute; etc). Dans template.html, on a mis 'expression|safe'.
    # http://jinja.pocoo.org/docs/2.9/templates/#working-with-automatic-escaping
    expression = expr_gen.generate_expression(seed, version)
    expr_gen_key = expr_gen.format_key(seed, version)
    # http://flask.pocoo.org/docs/0.12/api/#flask.url_for
    # http://stackoverflow.com/questions/39262172/flask-nginx-url-for-external
    linkOnSelf = url_for(".expressionotronGet", _external=True, seed=expr_gen_key)

    params_template = {
        "expression": expression,
        "permalink_to_expr": linkOnSelf,
        "link_to_get_random_expr": url_for(".expressionotronGet"),
        "link_to_post_specific_expr": url_for(".expressionotronPost"),
        "nb_visitors": nbVisitor,
    }

    return render_template('template.html', **params_template)

# TODO : nom merdiques
@app_expressionotron.route('/', methods=['POST'])
def expressionotronPost():
    unsafe_expr_gen_key = request.form["seedInForm"]
    return expressionotron(unsafe_expr_gen_key)

@app_expressionotron.route('/', methods=['GET'])
def expressionotronGet():
    unsafe_expr_gen_key = request.args.get("seed", "")
    return expressionotron(unsafe_expr_gen_key)

