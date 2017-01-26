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


def get_and_increase_nb_visit():
    """
    Lit, puis reecrit des infos dans un fichier texte, sur le serveur.
    En espérant que si plusieurs visiteurs viennent sur le site en meme temps,
    ça fasse pas tout planter.
    J'y connais rien, je sais du tout si c'est comme ça qu'on doit faire.
    Au pire, ca finira dans les except.
    """
    # FUTURE : ouvrir le fichier une seule fois au début et le fermer à la fin.
    # revenir au début du fichier entre la lecture et l'écriture.
    # ouvrir le fichier en le créant s'il n'existe pas.

    filename_visit_count = "/home/Recher/mysite/expressionotron/blorp.txt"

    try:
        file_visit_read = open(filename_visit_count, "r")
        str_nb_visit = file_visit_read.read()
        file_visit_read.close()
    except IOError:
        str_nb_visit = "0"

    if str_nb_visit.isdigit():
        nb_visit = int(str_nb_visit)
    else:
        nb_visit = 0
    nb_visit += 1
    str_nb_visit = str(nb_visit)

    try:
        file_visitor_write = open(filename_visit_count, "w")
        file_visitor_write.write(str_nb_visit)
        file_visitor_write.close()
    except IOError:
        # Woups. Fail dans la mise a jour du fichier des nombres de visites.
        # C'est pas grave, on laisse tomber.
        pass

    return nb_visit


def webpage_expressionotron(unsafe_expr_gen_key):
    nb_visit = get_and_increase_nb_visit()
    (seed, version) = expr_gen.sanitize_key(unsafe_expr_gen_key)
    # la chaîne de caractère 'expression' est déjà encodée en HTML
    # (avec les &eacute; etc). Dans template.html, on a mis 'expression|safe'.
    # http://jinja.pocoo.org/docs/2.9/templates/#working-with-automatic-escaping
    expression = expr_gen.generate_expression(seed, version)
    expr_gen_key = expr_gen.format_key(seed, version)
    # http://flask.pocoo.org/docs/0.12/api/#flask.url_for
    # http://stackoverflow.com/questions/39262172/flask-nginx-url-for-external
    permalink = url_for(
        ".expressionotron_get",
        _external=True,
        seed=expr_gen_key)

    params_template = {
        "expression": expression,
        "permalink_to_expr": permalink,
        "link_to_get_random_expr": url_for(".expressionotron_get"),
        "link_to_post_specific_expr": url_for(".expressionotron_post"),
        "nb_visitors": nb_visit,
    }

    return render_template('template.html', **params_template)

@app_expressionotron.route('/', methods=['POST'])
def expressionotron_post():
    unsafe_expr_gen_key = request.form["seedInForm"]
    return webpage_expressionotron(unsafe_expr_gen_key)

@app_expressionotron.route('/', methods=['GET'])
def expressionotron_get():
    unsafe_expr_gen_key = request.args.get("seed", "")
    return webpage_expressionotron(unsafe_expr_gen_key)

