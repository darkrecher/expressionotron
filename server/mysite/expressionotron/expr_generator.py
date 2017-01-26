"""
TODO : docstring expliquant le vocabulaire des noms de variable relative à la seed.
unsafe_expr_gen_key
expr_gen_key
version
seed
str_seed
"""

import random
# Renommer tout ça en "expr_generator". "Builder", ça fait bizarre.
import expressionotron.v001.expr_builder
b_v1 = expressionotron.v001.expr_builder
import expressionotron.v002.expr_builder
b_v2 = expressionotron.v002.expr_builder

FUNCTION_GEN_FROM_VERSION = {
    b_v1.version: b_v1.buildExpression,
    b_v2.version: b_v2.buildExpression,
}

VALID_VERSION_NUMBERS = FUNCTION_GEN_FROM_VERSION.keys()
CURRENT_EXPR_VERSION = b_v2.version
CURRENT_EXPR_SEED_MAX = b_v2.seed_max
SEPARATOR_SEED = "_"


def sanitize_key(unsafe_expr_gen_key):
    """
    TODO : docstring expliquant les différents formats possibles de unsafe_expr_gen_key
    on peut pas demander du random sur une version précédente de l'expressionotron.
    C'est bien dommage mais c'est comme ça. Et de toutes façon on n'en a pas besoin.
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
