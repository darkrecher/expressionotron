"""
Ce module appelle la bonne version du générateur d'expression,
selon la clé d'expression fournie, et renvoie l'expression.

Il permet également de déterminer des clés d'expression "saine".

Vocabulaire lié à ce module (qu'on retrouve ici et là dans les autres modules).

unsafe_expr_gen_key : variable contenant une clé d'expression, mais "unsafe".
C'est à dire que c'est une chaîne de caractère pouvant potentiellement
contenir n'importe quoi.

expr_gen_key : clé d'expression "safe". C'est une chaîne de caractère
indiquant explicitement la version du générateur d'expression à utiliser,
ainsi que la "seed" à envoyer à ce générateur pour qu'il renvoie la fameuse
phrase d'expression.
Cette chaîne doit respecter le format suivant :
<seed>_<version>

version : version du générateur d'expression. Attention, c'est une
chaîne de caractère, et non pas une valeur numérique.
Actuellement, il existe deux versions différentes : '001' et '002'.

seed / seed_expr : variable permettant au générateur de créer l'expression.
Une même valeur de seed renvoie toujours la même phrase. Mais il est difficile
de déterminer par avance la phrase qui va être générée à partir de la seed.
C'est ce qui permet de donner une impression d'aléatoire, tout en conservant
la reproductibilité. Une seed est une valeur numérique entière >=0.

str_seed : même chose que la seed, mais sous forme d'une string.
Exemple : '1234' au lieu de 1234.
"""

import random

# TODO : Renommer tout ça en "expr_generator". "Builder", ça fait bizarre.
import expressionotron.v001.expr_builder
# TODO : du coup, renommer ces "b_" qui ne veulent rien dire.
b_v1 = expressionotron.v001.expr_builder
import expressionotron.v002.expr_builder
b_v2 = expressionotron.v002.expr_builder

# TOOD : Renommer ça en "generate_expression"
FUNCTION_GEN_FROM_VERSION = {
    b_v1.version: b_v1.build_expression,
    b_v2.version: b_v2.build_expression,
}

VALID_VERSION_NUMBERS = FUNCTION_GEN_FROM_VERSION.keys()
# Version courante du générateur d'expression : '002'
# C'est la version qui est utilisée lorsqu'il n'est pas possible de déterminer
# la version choisie à partir de unsafe_expr_gen_key.
CURRENT_EXPR_VERSION = b_v2.version
CURRENT_EXPR_SEED_MAX = b_v2.seed_max
SEPARATOR_SEED = '_'


def sanitize_key(unsafe_expr_gen_key):
    """
    Transforme une unsafe_expr_gen_key en une expr_gen_key.

    Plusieurs cas sont possibles, selon le format de unsafe_expr_gen_key :

    <seed>_<version>, avec une version inconnue : génération aléatoire d'une
    seed, utilisation de la version courante.

    <seed>_<version>, avec une seed non numérique : génération aléatoire d'une
    seed, utilisation de la version courante.

    <seed>, avec une seed numérique : utilisation de la seed fournie et de la
    version courante.

    <n_importe_quoi> : génération aléatoire d'une seed,
    utilisation de la version courante.

    Les différents cas possibles ne permettent pas de générer aléatoirement
    une seed en utilisant une version précédente de l'expressionotron.
    C'est bien dommage mais c'est comme ça.
    Et de toutes façon on n'en a pas besoin.
    """
    version = CURRENT_EXPR_VERSION
    seed = 0

    if unsafe_expr_gen_key.isdigit():
        # On a uniquement la seed, sans la version. C'est pas grave.
        # On prend cette seed, et on utilisera la version courante
        seed =  int(unsafe_expr_gen_key)
        version = CURRENT_EXPR_VERSION
        return (seed, version)

    # On verifie que la seed respecte le format <digits>_<num_version>
    # Si ce n'est pas le cas, on prendra un seed au hasard,
    # et la version courante.
    str_seed, sep, version = unsafe_expr_gen_key.partition(SEPARATOR_SEED)
    is_safe = all((
        sep == SEPARATOR_SEED,
        version in VALID_VERSION_NUMBERS,
        str_seed.isdigit(),
    ))

    if not is_safe:
        version = CURRENT_EXPR_VERSION
        seed = random.randrange(CURRENT_EXPR_SEED_MAX)
    else:
        seed = int(str_seed)

    return (seed, version)


def generate_expression(seed, version):
    """
    Les paramètres seed et version sont supposés safe.
    Si ça ne l'est pas, ça fera des exceptions diverses.
    """
    function_expr_generator = FUNCTION_GEN_FROM_VERSION[version]
    return function_expr_generator(seed)


def format_key(seed, version):
    """
    fonction recréant une expr_gen_key à partir de seed/seed_str
    et de gen_version.
    """
    return SEPARATOR_SEED.join((str(seed), version))
